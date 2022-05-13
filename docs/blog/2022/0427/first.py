# copied from https://karobben.github.io/2021/04/10/Python/opencv-v-paste/
"""
$ virtualenv -p python3 env
$ pip install opencv-python
"""

import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',nargs='+',
                    help='Input video file')
parser.add_argument('-o','-U','--output', default="combine_result.avi",
                    help='Output video file, default as "combine_result.avi"')
parser.add_argument('-f','-F','--FPS', type = int,
                    help='Start from X second. default is the same as the first video')
parser.add_argument('-w','-W','--window', nargs='?',
                    help='1920x1080 default is the combined size of two videos')

args = parser.parse_args()
input_files = args.input
Window = args.window
fps = args.FPS

# function for combined two frames.
def Fram_connect(frame1, frame2, w1, h1,  w2, h2):
  frame2 = cv2.resize(frame2, (int(w2), int(h1)), interpolation = cv2.INTER_AREA)
  BG = cv2.resize(frame1, (int(w1 + w2), int(h1)), interpolation = cv2.INTER_AREA)
  BG[0:int(h1),0:int(w1)] = frame1
  BG[0:int(h1),int(w1):int(w1 + w2)] = frame2
  return (BG)

cap1 = cv2.VideoCapture(input_files[0])
cap2 = cv2.VideoCapture(input_files[1])

# The video 1 set the video 1 as the default size and fps
fps_c = cap1.get(cv2.CAP_PROP_FPS)
h1 = cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
w1 = cap1.get(cv2.CAP_PROP_FRAME_WIDTH)

fps_c2 = cap2.get(cv2.CAP_PROP_FPS)
h2 = cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)
w2 = cap2.get(cv2.CAP_PROP_FRAME_WIDTH)


# args for the video output
fps = fps_c

if Window == None:
  size = (int(w1+w2), int(h1))
else:
  size = (int(Window.split("x")[0]), int(Window.split("x")[1]))

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(args.output, fourcc, fps, size)


while True:
  ret, frame1 = cap1.read()
  if not ret:
      print("Read failure in {}".format(input_files[0]))
      break
  ret, frame2 = cap2.read()
  if not ret:
      print("Read failure in {}".format(input_files[1]))
      break
  img = Fram_connect(frame1, frame2, w1, h1,  w2, h2)
  img = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
  videowriter.write(img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break

# videowriter.write(frame)
