import cv2

def play_videoFile(filePath, mirror=False):
    try:
        cap = cv2.VideoCapture(filePath)
        cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)

        while True:
            ret_val, frame = cap.read()
            if mirror:
                frame = cv2.flip(frame, 1)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # esc to quit
        cv2.destroyAllWindows()
    except Exception as e:
        print("An error occurred:", str(e))

play_videoFile('video.avi', mirror=False)
