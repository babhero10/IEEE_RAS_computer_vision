import cv2

image = cv2.imread('images/astronaut.png')

if image is None:
    print("Error: Could not read the image. Verify the file path.")
else:
    cv2.imshow('Image Window', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
