import cv2
import imutils #to resize images
import pytesseract


pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"


image  = cv2.imread('numberplate3.jpg')
image = imutils.resize(image, width=500)


#now we will convert the image to grayscale and canny algorithm works only on grayscale images
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#now we need to remove noise from our image and make it smooth
gray = cv2.bilateralFilter(gray,11,17,17)

#now we will find the edges of the images
edged = cv2.Canny(gray,170,200)

#now we will find the countours based on the images
cnts, new = cv2.findContours(edged.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



image1 = image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3) #these values are fixed


#now we want only the numebr plate contours but we cannot select it so we will sort based on locations to find the number plate contours






cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:30]
NumberPlateCount = None

image2 = image.copy()
cv2.drawContours(image2, cnts, -1,(0,255,0),3)

#now we will run a for loop 
count = 0
name = 1 #name of our image
for i in cnts:
    perimeter = cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,0.02*perimeter,True)
    if(len(approx)==4): #4 means 4 cornors which will most probably be our number plate
        NumberPlateCount = approx
        #now we will crop that rectangle file
        x,y,w,h = cv2.boundingRect(i)
        crp_img = image[y:y+h,x:x+w]
        cv2.imwrite(str(name) + '.png',crp_img)
        name+=1
        break






 #now we will draw countours on our main image that we have identified as our numberplate
cv2.drawContours(image, [NumberPlateCount], -1 , (0,255,0), 3)
# cv2.imshow("Final Image", image)
# cv2.waitKey(0)
# cv2.imshow("Final Image", gray)
# cv2.waitKey(0)
# cv2.imshow("Final Image", edged)
# cv2.waitKey(0)


crop_img_loc = '1.png'
cv2.imshow("Cropped Image", cv2.imread(crop_img_loc))



# cv2.imshow("Final Image", image)

text = pytesseract.image_to_string(crop_img_loc,lang='eng')
print("Licence Number is : ", text) 
cv2.waitKey(0)



