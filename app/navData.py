import ardrone # https://github.com/lilyinstarlight/python-ardrone

drone = ardrone.ARDrone()

drone.takeoff()
drone.land()

print(drone.navdata)

drone.image.show()

drone.halt()