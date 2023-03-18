import cv2
# Load img
img = cv2.imread("src/lena.jpg")
if img is None:
    print("Img not found")
cv2.imshow("lena", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
