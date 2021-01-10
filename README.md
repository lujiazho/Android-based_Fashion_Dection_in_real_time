# Android-based Fashion Dection in real time
This repository applies transfer-learning-based object detection on [Color-Fashion Dataset](https://sites.google.com/site/fashionparsing/dataset) and deployed the .tflite model on Android to detect in real time.

# Requirements
```
Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.7. To install run:

$ pip install -r requirements.txt
```

# Download this project and satisfy the requirements
```
$ git clone https://github.com/leaving-voider/Android-based_Fashion_Dection_in_real_time.git
```

# Process
- Dataset Format Transformation
Packing training and testing data into a specific file format which is ".tfrecord", you can do this by run 
```
%cd code
!python generate_tfrecord.py
```

then uploading them and its’ corresponding bounding box labels on Google Cloud Storage. After configuring the pre-trained model and training parameter, the training process follows with Tensorflow Object Detection which is Google’s deep learning open-source API. Finally, under particular conditions, this model achieves good prediction performance on Color-Fashion Dataset. Besides, this work includes employing a light-weight model on the Android platform with Android Studio, which allows visualization of this work.
