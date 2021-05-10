import cv2

cap = cv2.VideoCapture(2)
# cap = cv2.VideoCapture("http://192.168.1.1:8080/video")


while True:
    _, image = cap.read()
    image = cv2.resize(image, (640,400))

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    ret, chess = cv2.findChessboardCorners(grey, (7, 7), None)
    draw = cv2.drawChessboardCorners(image, (7,7), chess, ret)
    cv2.imshow('img', image)
    print(chess)
    if ret == True:

        corners = cv2.cornerSubPix(grey, chess, (10, 10), (-1, -1), criteria)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()