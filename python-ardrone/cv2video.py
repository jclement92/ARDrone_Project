import cv2

class CV2Drone:
	def main():
		cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
		running = True
		while running:
    			running, frame = cam.read()
    			if running:
				cv2.imshow('frame', frame)
        		if cv2.waitKey(1) & 0xFF == 27:
            			running = False
		cam.release()
		cv2.destroyAllWindows()


if __name__ == '__main__':
	main()

