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
		elif key == 97:
		    print("pressed a")
		elif key == 115:
		    print("pressed s")
		elif key == 100:
		    print("pressed d")	
		elif key == 119:
		    print("pressed w")
		elif key == 81:
		    print("pressed left")
		elif key == 82:
		    print("pressed up")
		elif key == 83:
		    print("pressed right")
		elif key == 84:
		    print("pressed down")

		else:
		    print(key)
    else:
        # error reading frame
        print 'error reading video feed'
cam.release()
cv2.destroyAllWindows()
print ("Shutting down...",
    drone.halt())

