import cv2

# path of video
vidcap = cv2.VideoCapture("Video path destination")
success, frame = vidcap.read()
success
count = 0
#success = True

while vidcap.isOpened():
    success, frame = vidcap.read()
    if success:
        cv2.imwrite('Video path destination/%d.jpg' %count, frame)
        count+= 1
    else:
        break