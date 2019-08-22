from darknet import *
import os
with open('test.txt','r') as f:
    S = f.readlines()
    S = [X.rstrip('\n') for X in S ]
    #print(S)
'''for i in S:
    a = performDetect(i)
    #print(a)
    print(list(a['detections'][0][2]))
    break'''

def convert(bbox):
    bounds = bbox
    #shape = image.shape
    # x = shape[1]
    # xExtent = int(x * bounds[2] / 100)
    # y = shape[0]
    # yExtent = int(y * bounds[3] / 100)
    yExtent = int(bounds[3])
    xEntent = int(bounds[2])
    # Coordinates are around the center
    xCoord = int(bounds[0] - bounds[2]/2)
    yCoord = int(bounds[1] - bounds[3]/2)
    boundingBox = [
        [xCoord, yCoord],
        [xCoord, yCoord + yExtent],
        [xCoord + xEntent, yCoord + yExtent],
        [xCoord + xEntent, yCoord]
    ]
    return boundingBox


with open('test_label.csv','w+') as f1:
    str1 = "image_name" + ',' + 'x1' +','+ 'x2' + ',' + 'y1' + ','+ 'y2' + '\n'
    f1.write(str1)
for i in S:
    dirname,filename = os.path.split(i)
    a = performDetect(i)
    print(a)
    print(filename)
    try:
        b = convert(list(a['detections'][0][2]))
        c = tuple(b[0])
        d = tuple(b[2])
        with open('test_label.csv','a') as f1:
            str1 = filename + ',' + str(c[0]) + ',' +str(d[0]) + ',' + str(c[1]) + ',' + str(d[1]) + '\n'
            f1.write(str1)
    except:
        with open('test_label.csv','a') as f1:
            str1 = filename + ',' + str(0) + ',' +str(0) + ',' + str(0) + ',' + str(0) + '\n'
            f1.write(str1)
