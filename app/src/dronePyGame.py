import pygame
import time
from pyardrone import ARDrone

class DronePyGame:
    def __init__(self, drone: ARDrone = ARDrone()) -> None:
        pygame.init()
        W, H = 320, 240
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

        # self.drone = drone
        self.speed = 0.1
        self.running = True

        self.forwardKeyBind = pygame.K_w # Key W is pressed
        self.backwardKeyBind = pygame.K_s # Key S is pressed
        self.leftKeyBind = pygame.K_a # Key A is pressed
        self.rightKeyBind = pygame.K_d # Key D is pressed
        self.upKeyBind= pygame.K_UP # Key UP is pressed
        self.downKeyBind = pygame.K_DOWN # Key DOWN is pressed
        self.cwKeyBind = pygame.K_e # Key E is pressed
        self.ccwKeyBind = pygame.K_q # Key Q is pressed

    def captureInput(self):
        while self.running:
            for event in pygame.event.get():
                print(f"Event: {event}")
                pressed_keys = pygame.key.get_pressed()

                if hasattr(event, 'type'):

                    if event.type == pygame.QUIT:
                        self.running = False

                    elif event.type == pygame.KEYUP:
                        print('Hovering')
                        # self.drone.hover()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print('Takeoff')
                            # self.drone.takeoff()
                else:
                    print('No type attribute')

                if (hasattr(event, 'text')):

                    if pressed_keys[pygame.K_SPACE]:
                        print('Drone Landed')
                        # self.drone.land()

                    

                    # speed
                    if event.text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        self.speed = int(event.text)/10 if event.text != "0" else 1
                        print(f'Speed set to: {self.speed}')
                    
                
            #     else:
            #         print('Has no text attribute')


                #     elif event.key == pygame.K_UP:
                #         print("CIMA")
                #         self.drone.move(up=speed)
                #     elif event.key == pygame.K_DOWN:
                #         print("BAIXO")
                #         self.drone.move(down=speed)

                # elif event.type == pygame.TEXTINPUT:
                #     print(f"Key Pressed! -> {event.text}")

                #     if event.text == chr(pygame.K_SPACE):
                #         self.drone.land()
                #     # emergency
                #     elif event.text == chr(pygame.K_BACKSPACE):
                #         # self.drone.reset()
                #         print('Drone reseted')
                #     # forward / backward
                #     elif event.text == chr(pygame.K_w):
                #         print("FRENTE")
                #         self.drone.move(forward=speed)
                #     elif event.text == chr(pygame.K_s):
                #         print("TRAS")
                #         self.drone.move(backward=speed)
                #     # left / right
                #     elif event.text == chr(pygame.K_a):
                #         print("ESQUERDA")
                #         self.drone.move(left=speed)
                #     elif event.text == chr(pygame.K_d):
                #         print("DIREITA")
                #         self.drone.move(right=speed)
                #     # up / down

                #     # turn left / turn right
                #     elif event.text == chr(pygame.K_q):
                #         print("GIRAR ANTI-HORARIO")
                #         self.drone.move(ccw=speed)
                #     elif event.text == chr(pygame.K_e):
                #         print("GIRAR HORARIO")
                #         self.drone.move(cw=speed)
                        
            # try:
            #     surface = pygame.image.fromstring(self.drone.image, (W, H), 'RGB')
            #     # battery status
            #     hud_color = (255, 0, 0) if self.drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
            #     bat = self.drone.navdata.get(0, dict()).get('battery', 0)
            #     f = pygame.font.Font(None, 20)
            #     hud = f.render('Battery: %i%%' % bat, True, hud_color)
            #     self.screen.blit(surface, (0, 0))
            #     self.screen.blit(hud, (10, 10))
            # except:
            #     pass

            pygame.display.flip()
            self.clock.tick(50)
            pygame.display.set_caption("FPS: %.2f" % self.clock.get_fps())

        print ("Shutting down...", self.drone.halt())
        print ("Ok.")

    def moveDrone(self):
        forward=0 # Key W is pressed
        backward=0 # Key S is pressed
        left=0 # Key A is pressed
        right=0 # Key D is pressed
        up=0 # Key UP is pressed
        down=0 # Key DOWN is pressed
        cw=0 # Key E is pressed
        ccw=0 # Key Q is pressed