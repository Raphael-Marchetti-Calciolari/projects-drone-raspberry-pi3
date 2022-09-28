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
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.KEYUP:
                drone.hover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # drone.reset()
                    print('Drone reseted')
                    running = False
                # takeoff / land
                elif event.key == pygame.K_RETURN:
                    drone.takeoff()
                elif event.key == pygame.K_SPACE:
                    drone.land()
                # emergency
                elif event.key == pygame.K_BACKSPACE:
                    # drone.reset()
                    print('Drone reseted')
                # forward / backward
                elif event.key == pygame.K_w:
                    drone.move(forward=speed)
                elif event.key == pygame.K_s:
                    drone.move(backward=speed)
                # left / right
                elif event.key == pygame.K_a:
                    drone.move(left=speed)
                elif event.key == pygame.K_d:
                    drone.move(right=speed)
                # up / down
                elif event.key == pygame.K_UP:
                    drone.move(up=speed)
                elif event.key == pygame.K_DOWN:
                    drone.move(down=speed)
                # turn left / turn right
                elif event.key == pygame.K_q:
                    drone.move(ccw=speed)
                elif event.key == pygame.K_e:
                    drone.move(cw=speed)
                # speed
                elif event.key == pygame.K_1:
                    speed = 0.1
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_2:
                    speed = 0.2
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_3:
                    speed = 0.3
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_4:
                    speed = 0.4
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_5:
                    speed = 0.5
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_6:
                    speed = 0.6
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_7:
                    speed = 0.7
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_8:
                    speed = 0.8
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_9:
                    speed = 0.9
                    print(f'Current speed: {speed}')
                elif event.key == pygame.K_0:
                    speed = 1.0
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