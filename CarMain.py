import pygame
from Motor import Motor
import keypressModule as kp
from time import sleep
from WebCamModule import getImg
import JoyStickModule as js
from time import sleep
##################################################
#llantas traseras
motor1 = Motor(2,3,4)
#llantas delanteras
motor2 = Motor(22,17,27)
#runCamera = False
movement = 'JoyStick' #['KeyBoard']

##################################################
kp.init()
#if runCamera:getImg(x=200,y=200)
#pygame.mixer.init()
#pygame.mixer.music.load("Pito.mp3")

def main():
    if movement == 'JoyStick':
        jsVal = js.getJS()
        #axis2, backward-forward
        #aqui poner la condicion de que si el valor del eje es mayor a cero se va a delante, si es menor se va para atras
        if jsVal['axis2'] < 0:
            motor1.moveAdelante((jsVal['axis2'])*-30,0.1)#se mueve para adelante
        elif jsVal['axis2'] > 0:
            motor1.moveAtras((jsVal['axis2'])*30,0.1)#se mueve para atras
            pygame.mixer.init()
            pygame.mixer.music.load("Pito.mp3")
            pygame.mixer.music.play()
            pygame.mixer.stop()
        #axis1, left and right
        #insted of axis1 => axis3
        elif jsVal['axis3'] > 0:
            motor2.moveAdelante((jsVal['axis3'])*70,0.1)#right
        elif jsVal['axis3'] < 0:
            motor2.moveAtras((jsVal['axis3'])*-70,0.1)#left
        #direccionales con R2-> right // L2-> left
        #elif jsVal['R2'] > 0:
         #   motor2.moveAdelante((jsVal['R2'])*70,0.1)#right
        #elif jsVal['x'] < 0:
        #    motor2.moveAtras((jsVal['x'])*-70,0.1)#left
        else:
            motor1.stop(1)
            motor2.stop(1)
        #sleep(0.05)
    else:
        if kp.getKey('DOWN'):
                #motor1.moveAtras(100,0.01)
                pygame.mixer.init()
                pygame.mixer.music.load("Pito.mp3")
                pygame.mixer.music.play()
                pygame.mixer.stop()
                motor1.moveAtras(28,0.01)
                print("DOWN was pressed")
        elif kp.getKey('UP'):
                motor1.moveAdelante(25,0.01)
                print("UP was pressed")
        elif kp.getKey('LEFT'):
                motor2.moveAtras(100,0.1)
                print("LEFT was pressed")
        elif kp.getKey('RIGHT'):
                motor2.moveAdelante(100,0.1)
                print("RIGHT was pressed")
        else:
            motor1.stop(1)
            motor2.stop(1)

if __name__ == '__main__':
    while True:
        main()