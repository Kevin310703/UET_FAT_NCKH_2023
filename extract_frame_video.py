import cv2
import time

output_folder = 'Output_Frames/'

# path of video
vidcap = cv2.VideoCapture("Video path destination")

# Get the video properties
total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)

# Initialize variables
frame_count = 0
start_time = time.time()


#success = True

while vidcap.isOpened():
    success, frame = vidcap.read()
    if success:
        cv2.imwrite('Video path destination/%d.jpg' %frame_count, frame)
        frame_count += 1
    else:
        break

    # Save the extracted frame to the output folder
    # cv2.imwrite(output_folder + 'frame_{}.jpg'.format(frame_count), frame)

    # frame_count += 1

# Calculate the elapsed time and FPS
end_time = time.time()
elapsed_time = end_time - start_time
extracted_fps = frame_count / elapsed_time

# Print the results
print("Total Frames: ", total_frames)
print("Extracted Frames: ", frame_count)
print("Elapsed Time: ", elapsed_time, " seconds")
print("Extracted FPS: ", extracted_fps)

# Release the video object
vidcap.release()

