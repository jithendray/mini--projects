from imutils import paths
import imutils
import cv2
import os

imagesPath = "downloads"
outputPath = "dataset" # where annotations are saved

# grab the image paths
imagesPaths = list(paths.list_images(imagesPath))
counts = {}

# loop over the image paths
for i, imagePath in enumerate(imagesPaths):
    # display an update to the user
    print("[INFO] processing image "+ str(i+1) + "/" + str(len(imagesPaths)))

    try:
        # load the image and convert it to grayscale
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)

        # thresholding the image
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        # finding contours and keeping only the four largest ones
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:4]
        # loop over the contours
        for cnt in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            roi = gray[y - 5:y + h + 5, x - 5:x + w + 5]
            cv2.imshow("ROI", roi)
            key = cv2.waitKey(1) & 0xFF
            if key == ord(";"):
                print("[INFO] ignoring character")
                continue

            key = char(key).upper()
            dirPath = os.path.sep.join([outputPath, key])

            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            count = counts.get(key, 1)
            p = os.path.sep.join([dirPath, "{}.png".format(str(count).zfill(6))])
            cv2.imwrite(p, roi)
            counts[key] = count + 1

    except KeyboardInterrupt:
        print("[INFO] manually leaving script")
        break
    except:
        print("[INFO] skipping image...")
