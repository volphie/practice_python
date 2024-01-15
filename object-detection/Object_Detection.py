# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:25:12 2021

@author: 04440
"""


import cv2
import numpy as np

net = cv2.dnn.readNet('./object-detection/yolov3-tiny.weights','./object-detection/yolov3-tiny.cfg')

classes=[]
with open('./object-detection/coco','r') as f:
    classes = f.read().splitlines()

print(classes)

img = cv2.imread('./object-detection/image.jpg')
height, width, _ = img.shape

# Normalize the image
blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)

#for b in blob:
#    for n, img_blob in enumerate(b):
#        cv2.imshow(str(n),img_blob)

# dnn 모델에 이미지를 넣어 결과 얻어내기
net.setInput(blob)
output_layers_names = net.getUnconnectedOutLayersNames()
layerOutputs = net.forward(output_layers_names)

boxes = []
confidences = []
class_ids = []

for output in layerOutputs:
    for detection in output:
        scores = detection[5:] # 6번째 element 부터 class마다의 score(confidence)이므로 list slicing
        class_id = np.argmax(scores) # 최고점을 받은 element의 index를 반환
        confidence = scores[class_id] # 최고점을 받은 index의 값을 반환
        if confidence > 0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)
            
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            
            boxes.append([x, y, w, h])
            # confidences가 float type list 이어야 함, if not cv2.dnn.NMSBoxes 실행 시 에러남
            # https://github.com/opencv/opencv/issues/12789
            confidences.append(confidence.item())
            class_ids.append(class_id)
            
#print(len(boxes))
#print(type(confidences[0]))
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#print(indexes.flatten())

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(boxes), 3))

for i in indexes.flatten():
    x, y, w, h = boxes[i]
    label = str(classes[class_ids[i]])
    confidence = str(round(confidences[i],2))
    color = colors[i]
    cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
    cv2.putText(img, label+" "+confidence, (x, y+10), font, 1, (0,0,0), 2)
    

cv2.imshow('People in the office',img)
cv2.waitKey(0)