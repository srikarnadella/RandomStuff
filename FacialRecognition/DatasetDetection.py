import cv2, glob
import os

displayWidth = 800
disdplayHeight = 800
#Imports all the jpg files in the folder
images = glob.glob("*.jpg")

if not images:
    print("No images found in the directory.")
    exit()

print(f"Found {len(images)} images")



detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Loops through the image list
for image in images: 
    #Reads the image
    img = cv2.imread(image)
    #Converts to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Uses a histogram to reduce contrast
    gray = cv2.equalizeHist(gray_img)
    #Detects the x and y coordinates
    faces = detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Check if faces were detected
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Draw rectangles on the original image
            cv2.rectangle(img, (x, y), (x+w, y+h), (22, 100, 78), 2)

        #Resize image to make them all the same size
        resizedImgage = cv2.resize(img, (displayWidth, disdplayHeight))


        # Display the image with face detection
        cv2.imshow("Face Detection", resizedImgage)
        cv2.waitKey(2000)  
        cv2.destroyAllWindows()

    else:
        print("No faces detected in", image)
    