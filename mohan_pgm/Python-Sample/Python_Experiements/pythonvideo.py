##with open('a.mp4', 'rb') as file_open:
##  print(file_open.read())
import requests

##var = requests.get(r"C:\Users\Mohan S\Desktop\socketsample\a.mp4")
##print(var)

import cv2
import cv2
##cap = cv2.VideoCapture('C:\Users\Mohan S\Desktop\socketsample\a.MP4')
##print(type(cap))
##while(cap.isOpened()):
##  print("ww")
##  ret, frame = cap.read()
##  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##  print(gray)
##  cv2.imshow('frame',gray)
##  if cv2.waitKey(1) & 0xFF == ord('q'):
##    break
##print("www")
##cap.release()
##cv2.destroyAllWindows()

#------------------------------

##cap = cv2.VideoCapture('a.mp4')
##
##while(cap.isOpened()):
##    ret, frame = cap.read()
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##    cv2.imshow('frame',gray)
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##
##cap.release()
##cv2.destroyAllWindows()

#-----------------------

##import numpy as np
##import cv2
##
##cap = cv2.VideoCapture('F:\Family_Photos\New folder (2)\pugazh.MP4')
##
### Define the codec and create VideoWriter object
##fourcc = cv2.VideoWriter_fourcc(*'MJPG')
##out = cv2.VideoWriter('outpuTt.mp4',fourcc, 20.0, (640,480))
##
##while(cap.isOpened()):
##    ret, frame = cap.read()
##    if ret==True:
##        #frame = cv2.flip(frame,0)
##        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##
##        # write the flipped frame
##        
##
##        cv2.imshow('frame',gray)
##        out.write(gray)
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##            break
##    else:
##        break
##
### Release everything if job is finished
##cap.release()
##out.release()
##cv2.destroyAllWindows()

#------------------------

##import cv2
##
##cap = cv2.VideoCapture('a.mp4')
##
##fourcc = cv2.VideoWriter_fourcc(*'DIVX')
##out = cv2.VideoWriter('g.mp4',-fourcc, 25, (640,480))
##
###writer=cv2.VideoWriter("test1.avi", cv2.CV2_FOURCC(*'DIVX'), 25, (640,480))
##
##while(cap.isOpened()):
##    ret, frame = cap.read()
##    if ret:
##        #gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
##        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
##       
##
##        cv2.imshow('frame', gray)
##        print(gray)
##        #frame = cv2.resize(frame,(800,600))
##        out.write(gray)
##        print("llllllll")
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##            break
##    else:
##        break
##
##cap.release()
##out.release()
##cv2.destroyAllWindows()


#---------------------------

import cv2


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'h263')
out = cv2.VideoWriter('muthu_mohan.mp4',fourcc, 20.0, (800,600))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
##    cv2.imshow('gray', gray)
    frame = cv2.resize(frame,(800,600))
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

#-->https://stackoverflow.com/questions/45741780/python-output-by-opencv-videowriter-empty

