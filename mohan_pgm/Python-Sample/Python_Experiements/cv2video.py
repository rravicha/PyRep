
import cv2


cap = cv2.VideoCapture("a.mp4")

fourcc = cv2.VideoWriter_fourcc(*'h263')
out = cv2.VideoWriter('cv2_cameraaa_output.mp4',fourcc, 20.0, (800,600))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    frame = cv2.resize(frame,(800,600))
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
