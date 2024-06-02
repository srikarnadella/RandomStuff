import cv2
import os

casecasdeFile = os.path.join(os.getcwd(), "haarcascade_frontalface_default.xml")
detect = cv2.CascadeClassifier(casecasdeFile)

#Connects to camera
#For image move file into directory and add the file name instead of the 0
inputimage = cv2.VideoCapture(0)

if not inputimage.isOpened():
    print("Error: Could not open webcam.")
    
while True:
    #This method checks to see if there is an input image and if there is then returns the image size and a boolean value of if the image is there
    res, img = inputimage.read()

    #We now convert the img to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #We can also apply a histogram to reduce the contrast of the image
    gray = cv2.equalizeHist(gray)

    #method finds the x,y coordinates of the face
    #the way these coordinates work is by finding the bottom left coordinates of the face and using w and h to mark the other points to make the box
    faces = detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)


    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (22.4, 100, 7.8), 2)

    cv2.imshow("Test", img)

    #Needed for the code at all times as it terminates the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

inputimage.release()
cv2.destroyAllWindows()