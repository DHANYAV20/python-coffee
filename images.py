import cv2
img = cv2.imread("chickencurryinabowl.jpg", 0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

cv2.imshow("Chickencurryinabowl", img)
cv2.waitKey(2000)
cv2.destroyAllWindows()


#https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
#https://docs.python.org/3/library/time.html
