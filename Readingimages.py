import cv2

img=cv2.imread("C:/Users/akash.patwa/Downloads/Ranjana information/Ranjana-pic.jpeg")

cv2.imshow("Display image",img)

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img)
cv2.waitKey(0)