from time import sleep
import pygame
from pyardrone import ARDrone, at
import json
from requests_futures.sessions import FuturesSession

def parse_navdata(navdata):
    parsed_navadata = {
        "vx": int(navdata.demo.vx),
        "vy": int(navdata.demo.vy),
        "altitude": navdata.demo.altitude,
        "bat_level": navdata.demo.vbat_flying_percentage
    }
    return parsed_navadata

def make_request(session, data):
    print(f"Entrou na request -> {parse_navdata(data)}")
    url = "http://localhost:1880/navdata"
    session.post(url, data=parse_navdata(data))

class DronePyGame:
    def __init__(self, drone) -> None:
        print('Iniciando pygame')
        pygame.init()
        print("Pygame iniciado")

        W, H = 320, 240
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

        self.drone = drone
        self.speed = 0.1
        self.isMoving = False
        self.running = True

        self.takeoffKeyBind = pygame.K_RETURN
        self.landKeyBind = pygame.K_SPACE

        self.forwardKeyBind = pygame.K_w
        self.backwardKeyBind = pygame.K_s
        self.leftKeyBind = pygame.K_a
        self.rightKeyBind = pygame.K_d
        self.upKeyBind = pygame.K_i
        self.downKeyBind = pygame.K_k
        self.cwKeyBind = pygame.K_e
        self.ccwKeyBind = pygame.K_q

        # Intanciar http session
        print('Instanciado sessão http')
        self.session = FuturesSession()
        print('Sessao http iniciada')
        print('Finalizada instanciação do DronePyGame')

    # def getAltitude(self):
    #     return self.drone.navdata.demo.altitude

    def getBatteryLevel(self):
        return self.drone.navdata.demo.vbat_flying_percentage

    def captureInput(self):
        print('Iniciando captuda de entrada')
        cont = 0
        while self.running:
            # print(self.getAltitude())
            # print(f"Altitude: {self.drone.navdata.demo.altitude}")
            # print(f"PARSED: {parse_navdata(self.drone.navdata)}")

            if cont >= 50:
                print("Enviando dados ao node-red")
                make_request(self.session, self.drone.navdata)
                cont = 0
            cont += 1

            for event in pygame.event.get():
                pressed_keys = pygame.key.get_pressed()

                # Special events
                if hasattr(event, 'type'):
                    if event.type == pygame.QUIT:
                        self.running = False
                else:
                    pass

                # Speed management
                if hasattr(event, 'text'):
                    if event.text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        self.speed = int(event.text) / 10 if event.text != "0" else 1
                        print(f'Speed set to: {self.speed}')

                # Start and stop flying
                if pressed_keys[self.takeoffKeyBind]:
                    self.drone.takeoff()
                    pass
                if pressed_keys[self.landKeyBind]:
                    self.drone.land()
                    pass

                # Movement management
                if (
                        pressed_keys[self.forwardKeyBind] or
                        pressed_keys[self.backwardKeyBind] or
                        pressed_keys[self.leftKeyBind] or
                        pressed_keys[self.rightKeyBind] or
                        pressed_keys[self.upKeyBind] or
                        pressed_keys[self.downKeyBind] or
                        pressed_keys[self.cwKeyBind] or
                        pressed_keys[self.ccwKeyBind]
                ):
                    self.isMoving = True
                    self.drone.move(
                        forward=pressed_keys[self.forwardKeyBind] * self.speed,
                        backward=pressed_keys[self.backwardKeyBind] * self.speed,
                        left=pressed_keys[self.leftKeyBind] * self.speed,
                        right=pressed_keys[self.rightKeyBind] * self.speed,
                        up=pressed_keys[self.upKeyBind] * self.speed,
                        down=pressed_keys[self.downKeyBind] * self.speed,
                        cw=pressed_keys[self.cwKeyBind] * self.speed,
                        ccw=pressed_keys[self.ccwKeyBind] * self.speed
                    )

                else:
                    self.isMoving = False
                    self.drone.hover()

                # Debug logs
                # print(f"F={pressed_keys[self.forwardKeyBind] * self.speed} B={pressed_keys[self.backwardKeyBind] * self.speed} L={pressed_keys[self.leftKeyBind] * self.speed} R={pressed_keys[self.rightKeyBind] * self.speed} U={pressed_keys[self.upKeyBind] * self.speed} D={pressed_keys[self.downKeyBind] * self.speed} CW={pressed_keys[self.cwKeyBind] * self.speed} CCW={pressed_keys[self.ccwKeyBind] * self.speed}")
               # pprint(self.drone.navdata)

            pygame.display.flip()
            self.clock.tick(50)
            pygame.display.set_caption("FPS: %.2f" % self.clock.get_fps())

        print("Shutting down...", self.drone.halt())
        print("Ok.")
