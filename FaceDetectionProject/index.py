import cv2
from random import randrange

# load som3e pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# choose an image to detect faces
# img=cv2.imread('manyface.png')
webcam = cv2.VideoCapture(0)

# Must convert into greyscale image
# grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# itterate over frame for webcam
while True:
    # Read current Frame
    successful_frame_read, frame = webcam.read()

    # must convert into grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (randrange(256), randrange(256), randrange(256)), 10)

    cv2.imshow('Face Detector', frame)

    key=cv2.waitKey(1)

    ##stop if Q key is Pressed
    if key==81 or key==113:
        break



# detect faces
# face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

# Draw a rectangle around the faces
# for(x,y,w,h) in face_coordinates:
#     cv2.rectangle(img,(x,y),(x+w,y+h),( randrange(256),randrange(256),randrange(256)),10)


# showing the image
# cv2.imshow('Face Detector', img)

# wait for any button to click
# cv2.waitKey()

print("code completed")
