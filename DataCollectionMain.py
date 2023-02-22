import WebCamModule as wM
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
    if joyVal['axis3'] > 0:
        steeringRight = 0
        steeringRight = joyVal['axis3']#derecha 
        #print("R: ",steeringRight)
    elif joyVal['axis3'] < 0:
        steeringLeft = 0
        steeringLeft = joyVal['axis3']#izquierda 
        #print("L: ",steeringLeft)
    throttle = joyVal['o']*maxThrottle
    if joyVal['share'] == 1:
        if record == 0:
            print("REcording has started...")
            record += 1
            sleep(0.300)
    if record == 1:
        img = wM.getImg(True,size=[240,120])
        if joyVal['axis3'] > 0:
            dcM.saveData(img, steeringRight)
        elif joyVal['axis3'] < 0:
            steeringLeft = -1*steeringLeft#hago la conversinpor el angulo negativo 
            dcM.saveData(img, steeringLeft)
        record =2
    elif record == 2: #stop the recording
        dcM.saveLog()
        record = 0 
        print("fin record")
    motor1.moveAdelante(throttle,0.1)#mover adelante
    if joyVal['axis3'] > 0:
        motor2.moveAdelante(steeringRight,0.1)#mover Derecha
    elif joyVal['axis3'] < 0:
        #steeringLeft = -1*steeringLeft
        motor2.moveAtras(steeringLeft,0.1)#mover izquierda
    cv2.waitKey(1)