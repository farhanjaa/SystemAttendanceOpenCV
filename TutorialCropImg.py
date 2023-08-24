import cv2 

img = cv2.imread("Images/farhan.jpg")
# crop_img = img[500:600+216, 100:100+216]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)
# Shape of the image
print(type(img))
print("Shape of the image", img.shape)
  
# [rows, columns]
crop = img[500:600+216, 100:100+216]  
  
cv2.imshow('original', img)
cv2.imshow('cropped', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()