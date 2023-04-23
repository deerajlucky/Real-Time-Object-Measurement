import cv2
import u
import numpy as np

webcam = False
path = '1b.jpeg'
cap = cv2.VideoCapture(1)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)
scale = 3
wP = 210 * scale
hP = 297 * scale


while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    imgContours, conts, can = u.getContours(img, minArea=50000, filter=4)
    #print(str(len(can)))
    #cv2.drawContours(img, can, -1, (0, 255, 0), 3)
    if len(conts) != 0:
        biggest = conts[0][2]
        #print(biggest)
        imgWarp = u.warpImg(img, biggest, wP, hP)
        imgContours2, conts2, can = u.getContours(imgWarp, minArea=2000, filter=4)

        # c = max(can,key=cv2.contourArea)
        # x,y,w,h=cv2.boundingRect(c)
        # cv2.rectangle(imgWarp,(x,y),(x+w,y+h),(0,255,0),5)


        #print(can)
        #im = cv2.imread(imgWarp)
        #cv2.imwrite('d.jpeg', imgWarp)


        # if len(conts) != 0:
        #     for obj in conts2:
        #         cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
        #         npoints = u.reorder(obj[2])
        #         # print(u.findDis(npoints[0][0]//scale,npoints[1][0]//scale))
        #         print(npoints)

        #print(str(len(can)))

        for cnt in can:


            rect = cv2.minAreaRect(cnt)

            (x, y), (w, h), angle = rect



            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.circle(imgWarp, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(imgWarp, [box], True, (255, 0, 0), 2)
            cv2.putText(imgWarp,"Width {}".format(round(w)), (int(x-20), int(y-15)), cv2.FONT_HERSHEY_PLAIN,2, (0,0,0),2)
            cv2.putText(imgWarp,"Height {}".format(round(h)), (int(x-20), int(y+15)), cv2.FONT_HERSHEY_PLAIN,2, (0,0,0),2)

            #print(box)



        #cv2.drawContours(imgWarp, can, -1, (255, 0, 0), 3)
        # rect = cv2.minAreaRect(can)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        #cv.drawContours(imgWarp, [box], 0, (0, 0, 255), 2)
        cv2.imshow('A4', imgWarp)



    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.imshow('Original', img)
    cv2.waitKey(1)


# img = cv2.imread('a.jpeg')
#
# cv2.imshow('img',img)
# cv2.waitKey(0)
