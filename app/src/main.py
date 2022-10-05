from dis import findlinestarts
import time
from pyardrone import ARDrone, at
from sample import sample
from dronePyGame import DronePyGame

drone = ARDrone()
drone.send(at.CONFIG('general:navdata_demo', True))
landed_flag = False

try:
    print('Main program')
    dronePyGame = DronePyGame(drone)
    dronePyGame.captureInput()
    
    # sample(drone)
    # drone.navdata_ready.wait()

    # print('Decolando...')
    # while not drone.state.fly_mask:
    #     drone.takeoff()

    # print('Decolou!')
    # time.sleep(5)
    # print('Pousando...')

    # while drone.state.fly_mask:
    #     drone.land()
    #     landed_flag = True

    # print('Pousou!')

except KeyboardInterrupt:
    print('Pouso forçado por interrupção do keyboard')
    drone.land()
    landed_flag = True

finally:
    if not landed_flag:
        print('Finally interrupt')
        drone.emergency()
    else:
        print('Drone already landed')

