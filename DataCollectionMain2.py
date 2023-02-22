import WebCamModule as wM
import pygame
import DataCollectionModule as dcM
import JoyStickModule as jsM
import Motor as mM 
import cv2
from time import sleep

maxThrottle = 0.25#acelerador 
# llantas traseras
motor1 = mM.Motor(2,3,4)
#llantas delanteras
motor2 = mM.Motor(22,17,27)

record = 0 
while True: 
    joyVal = jsM.getJS()#get the value of the js
    #print(joyVal)
    angulo = 0 
    anguloDer = 0 
    anguloIzq = 0
    if joyVal['axis3']>0: 
        anguloDer=joyVal['axis3']
        angulo=anguloDer
    else:
        anguloIzq=joyVal['axis3']
        angulo=anguloIzq
    throttle = joyVal['o']*maxThrottle
    if joyVal['share'] == 1:
        if record == 0: print('Recording started...')
        record +=1
        sleep(0.300)
    if record == 1:
        img = wM.getImg(True,size=[240,120])
        dcM.saveData(img,angulo)
    elif record == 2:
        dcM.saveLog()
        record=0
    #llantes de traseras 
    if joyVal['axis2'] < 0: 
        motor1.moveAdelante((joyVal['axis2'])*-30,0.1)#adelante
    if joyVal['axis2'] > 0: 
        motor1.moveAtras((joyVal['axis2'])*30,0.1)
        
    #llantas delanteras
    if joyVal['axis3'] > 0:
        motor2.moveAdelante((joyVal['axis3'])*70,0.1)#mover Derecha
    elif joyVal['axis3'] < 0:
        #steeringLeft = -1*steeringLeft
        motor2.moveAtras((joyVal['axis3'])*-70,0.1)#mover izquierda
    else:
            motor1.stop(1)
            motor2.stop(1)

    cv2.waitKey(1)


