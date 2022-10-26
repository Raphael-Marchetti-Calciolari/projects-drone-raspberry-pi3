import time
from dronePyGame import DronePyGame
from pyardrone import ARDrone, at

drone = ARDrone()
print('Drone instanciado')
print('Esperando navdata...')
drone.navdata_ready.wait()
print('Configurando navdata')
drone.send(at.CONFIG('general:navdata_demo', True))
print('Aguardando navdata')
time.sleep(3)
print(f'Drone navdata pós configuração {drone.navdata.demo.altitude}')

landed_flag = False

try:
    print('Iniciando programa principal')
    print('Instanciando DronePyGame')
    dronePyGame = DronePyGame(drone)
    print('Iniciando captura de input')
    dronePyGame.captureInput()

except KeyboardInterrupt:
    print('Pouso forçado por interrupção do keyboard')
    drone.land()
    landed_flag = True

except Exception as e:
    print(f"Erro: {e.with_traceback()}")

finally:
    if not landed_flag:
        print('Finally interrupt')
        drone.emergency()
    else:
        print('Drone already landed')

