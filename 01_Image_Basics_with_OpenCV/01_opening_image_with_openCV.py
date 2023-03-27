import cv2

img=cv2.imread("C:\\Users\\Emirhan\\Desktop\\DeepLearning\\Computer_Vision_with_OpenCV_and_DeepLearing\\My_CV_Course\\DATA\\00-puppy.jpg")
new_img=cv2.resize(img,(640,480))

cv2.imshow('puppy',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()