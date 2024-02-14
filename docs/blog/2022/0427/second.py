from pathlib import Path
import cv2
import numpy as np

filename1 = str(Path('~/Videos/20220427/video-1650779715.mp4').expanduser())
filename2 = str(Path('~/Videos/20220427/2022-04-25-120810.webm').expanduser())

cap1 = cv2.VideoCapture(filename1, 0)
cap2 = cv2.VideoCapture(filename2, 0)

# The video 1 set the video 1 as the default size and fps
fps1 = cap1.get(cv2.CAP_PROP_FPS)
h1 = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
w1 = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)

fps2 = cap2.get(cv2.CAP_PROP_FPS)
h2 = cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)
w2 = cap2.get(cv2.CAP_PROP_FRAME_WIDTH)

size = (int(w1 + w2), int(h1 + h2))

print("{}: {}x{} ({} fps)".format(filename1, h1, w1, fps1))
print("{}: {}x{} ({} fps)".format(filename2, h2, w2, fps2))

fps = fps1

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter("output.avi", fourcc, fps, size)

while (cap1.isOpened()):

    ret, frame1 = cap1.read()
    if not ret:
        print("Read failure in {}".format(filename1))
        break
    ret, frame2 = cap2.read()
    if not ret:
        print("Read failure in {}".format(filename2))
        break
    both = np.concatenate((frame1, frame2), axis=1)

    cv2.imshow('Frame', both)
    out.write(both)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
out.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
