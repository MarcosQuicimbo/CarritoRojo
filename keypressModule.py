import pygame

def init(): #abrimos una ventana
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(keyname):#obtenemos la tecla del teclado: arriba, abajo, izq, der
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}'.format(keyname))
    if keyInput [mykey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey('LEFT'):
        print('key LEFT was pressed')

if __name__ == '__main__':
    init()
    while True:
        main()
