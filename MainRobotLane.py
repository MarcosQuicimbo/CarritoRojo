from Motor import Motor 
from LaneDetectionModule import getLaneCurve
import WebCamModule
import cv2
#==============
# llantas traseras
motor1 = Motor(2,3,4)
#llantas delanteras
motor2 = Motor(22,17,27)
#==============
def main ():
    img = WebCamModule.getImg()#get the image of the webcam 
    #curveVal = getLaneCurve #send the img to get the curve 
    curveVal = getLaneCurve(img,2)
    #get the curve value, 1 display just the result, 2 display the stack
    


    sen = 1.3 #sensitivity -> how much we want to have impact on the curve
    maxVAL = 0.3 #max speed


    #define the max speed # speed value is in range [0,1]
    if curveVal > maxVAL:
        curveVal = maxVAL
    if curveVal <- maxVAL:
        curveVal = -maxVAL

    #Dead zone - va recto, si no se define seguirá moviendose right-left
    if curveVal > 0: #right
        sen = 1.7 #jugar con este valor, 1 no afecta en nada
        if curveVal <0.05:
            curveVal = 0
    else:            #left
        if curveVal >-0.08:
            curveVal = 0

    motor1.moveAdelante(10,0.05)
    #el carro no se mueve para atrás
    if curveVal > 0:
        #motor2.moveAdelante(-curveVal*sen,0.1)
        motor2.moveAdelante(curveVal*sen,0.1)
    if curveVal > 0:
        motor2.moveAtras(curveVal*sen,0.1)

    cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()