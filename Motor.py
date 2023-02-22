#hasta aquí los pines de los pines de los motores
#funcionan como deberían
#motor1 = motor(2,3,4)
#motor1 = motor(22,17,27)
import RPi.GPIO as GPIO #importo para poder usar la librería de los pines
from time import sleep

GPIO.setmode(GPIO.BCM) #nomenclatura de los pines
GPIO.setwarnings(False) #apago los warnings

class Motor():
    def __init__(self,Ena,In1,In2): #constructor para el motor
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(10)

    def moveAdelante(self,x=0,t=0):#x= velocidad, t= tiempo de sleep
        self.pwm.ChangeDutyCycle(x) #cambiar la frecuencia
        GPIO.output(self.In1,GPIO.HIGH) #arriba
        GPIO.output(self.In2,GPIO.LOW) #abajo
        sleep(t)
    def moveAtras(self,x=0,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        sleep(t)
    def stop(self,x=0,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.LOW)
        sleep(t)

def main():
    print("")
    #llantas traseras
    #motor1 = Motor(2,3,4)
    #llantas delanteras
    #motor2 = Motor(22,17,27)


    #CÓDIGO DE LLANTAS TRASERA BIEN HECHO

    #motor2.moveAdelante(100,1) #ir a la derecha
    #motor2.stop(2)
    #motor2.moveAtras(100,1) #ir a la izquierda
    #motor2.stop(2)


    #CÓDIGO DE LLANTAS TRASERA BIEN HECHO

    #motor1.moveAdelante(50,1) #adelante
    #motor1.stop(2)
    #motor1.moveAtras(20,1) #atras
    #motor1.stop(2)


if __name__ == '__main__':
    while True:
        main()
        #hola