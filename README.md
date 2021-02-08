# Face Detection and Anonymisation

Detect and blur/scramble faces in images or webcam footage. Could be used in an AWS Lamba to automatically anonymise faces in uploaded images.

## Image Files
![faces](https://github.com/memsb/FaceDetection/blob/main/faces/faces.png?raw=true)

```
python anonymise.py --input faces/faces.png --output faces/blurred.png
```

![blurred faces](https://github.com/memsb/FaceDetection/blob/main/faces/blurred.png?raw=true)

```
python anonymise.py --input faces/faces.png --output faces/pixelated.png --method pixelate
```

![pixelated faces](https://github.com/memsb/FaceDetection/blob/main/faces/pixelated.png?raw=true)

## Webcam Video
```
python webcam.py
```


![Blurred webcam image](https://github.com/memsb/FaceDetection/blob/main/faces/webcam_blurred.png?raw=true)
```
python webcam.py --method pixelate
```

![Pixelated webcam image](https://github.com/memsb/FaceDetection/blob/main/faces/webcam_pixelated.png?raw=true)



