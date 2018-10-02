import cv2
import libardrone


cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
running = True
drone = libardrone.ARDrone()
while running:
    # get current frame of video
    running, frame = cam.read()
    if running:
        cv2.imshow('frame', frame)
	key = cv2.waitKey(1)
	if (key != -1):
        key = key & 0xFF 
		if key == 27: 
		    # escape key pressed
			running = False
		elif key == 10:
			print("pressed Enter")
			drone.takeoff()
		elif key == 32:
			print("pressed space")
			drone.land()
		elif key == 8:
			print("pressed backspace")
			drone.reset()
		elif key == 97:
			print("pressed a")
			drone.move_left()
		elif key == 115:
			print("pressed s")
			drone.move_backward()
		elif key == 100:
			print("pressed d")
			drone.move_right()	
		elif key == 119:
			print("pressed w")
			drone.move_up()
		elif key == 81:
			print("pressed left")
			drone.turn_left()
		elif key == 82:
			print("pressed up")
			drone.move_up()
		elif key == 83:
			print("pressed right")
			drone.turn_right()
		elif key == 84:
			print("pressed down")
			drone.move_down()
		elif key == 48:
			drone.speed = 0.1
		elif key == 49:
			drone.speed = 0.2
		elif key == 50:
			drone.speed = 0.3
		elif key == 51:
			drone.speed = 0.4
		elif key == 52:
			drone.speed = 0.5
		elif key == 53:
			drone.speed = 0.6
		elif key == 54:
			drone.speed = 0.7
		elif key == 55:
			drone.speed = 0.8
		elif key == 56:
			drone.speed = 0.9
		elif key == 57:
			drone.speed = 1.0
		else:
		    print(key)
	else:
		print(drone.navdata.get(0, dict()))		
    else:
        # error reading frame
        print 'error reading video feed'
cam.release()
cv2.destroyAllWindows()
print ("Shutting down...",
    drone.halt())

