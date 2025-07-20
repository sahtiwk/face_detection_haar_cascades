import cv2 as cv

image_file = './input_image.jpeg'
cascade_file = './haar_face.xml'

img = cv.imread(image_file)

if img is None:
    print(f"Error: Could not find '{image_file}'")
    print("Make sure the image is in the same folder as the script and has the correct name.")
else:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier(cascade_file)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    print(f"Found {len(faces_rect)} face(s).")

    for (x, y, w, h) in faces_rect:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv.imshow("Detected Faces", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
