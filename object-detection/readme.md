# Object-Detection
OpenCV와 Yolov3 모델을 활용한 Obejct-Detection Example 실행해보기


## Source
Youtube https://www.youtube.com/watch?v=1LCb1PVqzeY 


## 필요 도구
1. OpenCV 설치
```
cmd> pip install opencv-python
```


2. coco.names
```
https://github.com/pjreddie/darknet/blob/master/data/coco.names
```
* Yolo v3는 Coco Dataset(https://cocodataset.org)을 기반으로 Train된 모델이므로 Coco Dataset의 분류 값을 데이터로 갖고 있어야 한다.
* coco.names 파일은 Yolo v3가 인식하는 사물의 classification 목록

3. Yolo v3 weights 파일 및 config 파일
```
http://pjreddie.com/darknet/yolo/
```
* 적당한 weights 파일과 config 파일을 다운받는다.
* weights 파일은 너무 커서 github에 올려 놓지 않았다. 
* 직접 다운 받아야 한다.


## 해 본 것
* 이미지 파일과 동영상 파일에서 사물을 인식해서 box 표시하고 인식된 사물의 명칭과 인식률을 표시한다.
* 이미지 파일은 googling해서 아무거나 테스트를 해 보았는데, 저작권 문제가 있을 수 있어서 github에는 올리지 않았다.
* 동영상 파일은 youtube에서 traffic 관련한 동영상을 mp4 파일로 다운 받아서 테스트해 보았다.(파일 크기가 커서 github에 올리지 않았으니 직접 찾아서 아무거나 해 봐도 좋을 듯하다.)
