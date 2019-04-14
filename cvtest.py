import cv2 as cv
img = cv.imread('image.jpg')
while True:
    cv.imshow('mandrill', img)

    if cv.waitKey(1) & 0xFF == 27:
        break
cv.destroyAllWindows()
