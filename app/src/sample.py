import pygame
from pyardrone import ARDrone



def sample(drone: ARDrone):
    pygame.init()
    W, H = 320, 240
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    speed = 0.1
    running = True
    while running:
        for event in pygame.event.get():
            print(f"Event: {event}")
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.KEYUP:
                drone.hover()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    drone.takeoff()

                elif event.key == pygame.K_UP:
                    print("CIMA")
                    drone.move(up=speed)
                elif event.key == pygame.K_DOWN:
                    print("BAIXO")
                    drone.move(down=speed)


            elif event.type == pygame.TEXTINPUT:

                print(f"Key Pressed! -> {event.text}")


                if event.text == chr(pygame.K_SPACE):
                    drone.land()
                # emergency
                elif event.text == chr(pygame.K_BACKSPACE):
                    # drone.reset()
                    print('Drone reseted')
                # forward / backward
                elif event.text == chr(pygame.K_w):
                    print("FRENTE")
                    drone.move(forward=speed)
                elif event.text == chr(pygame.K_s):
                    print("TRAS")
                    drone.move(backward=speed)
                # left / right
                elif event.text == chr(pygame.K_a):
                    print("ESQUERDA")
                    drone.move(left=speed)
                elif event.text == chr(pygame.K_d):
                    print("DIREITA")
                    drone.move(right=speed)
                # up / down

                # turn left / turn right
                elif event.text == chr(pygame.K_q):
                    print("GIRAR ANTI-HORARIO")
                    drone.move(ccw=speed)
                elif event.text == chr(pygame.K_e):
                    print("GIRAR HORARIO")
                    drone.move(cw=speed)
                # speed
                elif event.text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    speed = int(event.text)/10 if event.text != "0" else 1
                    print(f'Current speed: {speed}')


        try:
            surface = pygame.image.fromstring(drone.image, (W, H), 'RGB')
            # battery status
            hud_color = (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
            bat = drone.navdata.get(0, dict()).get('battery', 0)
            f = pygame.font.Font(None, 20)
            hud = f.render('Battery: %i%%' % bat, True, hud_color)
            screen.blit(surface, (0, 0))
            screen.blit(hud, (10, 10))
        except:
            pass

        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

    print ("Shutting down...", drone.halt())
    print ("Ok.")