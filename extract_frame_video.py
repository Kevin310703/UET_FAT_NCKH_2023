# import cv2
# import time

# output_folder = 'Output_Frames/'

# # path of video
# vidcap = cv2.VideoCapture('videoplayback.mp4')

# # Get the video properties
# total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
# fps = vidcap.get(cv2.CAP_PROP_FPS)

# # Initialize variables
# frame_count = 0
# start_time = time.time()

# #success = True

# while vidcap.isOpened():
#     success, frame = vidcap.read()
#     if success:
#         cv2.imwrite('Video path destination/%d.jpg' %frame_count, frame)
#         frame_count += 1
#     else:
#         break

#     # Save the extracted frame to the output folder
#     # cv2.imwrite(output_folder + 'frame_{}.jpg'.format(frame_count), frame)

#     # frame_count += 1

# # Calculate the elapsed time and FPS
# end_time = time.time()
# elapsed_time = end_time - start_time
# extracted_fps = frame_count / elapsed_time

# # Print the results
# print("Total Frames: ", total_frames)
# print("Extracted Frames: ", frame_count)
# print("Elapsed Time: ", elapsed_time, " seconds")
# print("Extracted FPS: ", extracted_fps)

# # Release the video object
# vidcap.release()

import cv2
import time

output_folder = 'Output_Frames/'

# FPS mục tiêu
target_fps = 60

# Tính thời gian giữa các khung hình
frame_interval = 1.0 / target_fps

# Bắt đầu thời điểm
start_time = time.time()

# Đếm khung hình
frame_count = 0

vidcap = cv2.VideoCapture('videoplayback.mp4')

while vidcap.isOpened():
    # Xử lý khung hình
    # ...
    success, frame = vidcap.read()

    if success:
        cv2.imwrite('Video path destination/%d.jpg' %frame_count, frame)
        frame_count += 1
    else:
        break

    # Tính thời gian đã trôi qua
    elapsed_time = time.time() - start_time

    # Kiểm tra nếu đã đủ thời gian giữa các khung hình
    if elapsed_time > frame_count * frame_interval:
        # Ghi lại thời điểm bắt đầu xử lý khung hình
        frame_start_time = time.time()

        # Xử lý khung hình
        # ...

        # Đếm khung hình đã xử lý
        frame_count += 1

        # Tính thời gian xử lý khung hình
        frame_elapsed_time = time.time() - frame_start_time

        cv2.imwrite(output_folder + 'frame_{}.jpg'.format(frame_count), frame)

        # Delay để giữ số lượng khung hình đạt được FPS mục tiêu
        delay_time = frame_interval - frame_elapsed_time
        if delay_time > 0:
            time.sleep(delay_time)

# Calculate the elapsed time and FPS
end_time = time.time()
elapsed_time = end_time - start_time
extracted_fps = frame_count / elapsed_time

# Print the results
# print("Total Frames: ", total_frames)
print("Extracted Frames: ", frame_count)
print("Elapsed Time: ", elapsed_time, " seconds")
print("Extracted FPS: ", extracted_fps)

# Release the video object
vidcap.release()

