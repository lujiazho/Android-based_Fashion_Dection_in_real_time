# Android-based Fashion Dection in real time
This repository applies transfer-learning-based object detection on [Color-Fashion Dataset](https://sites.google.com/site/fashionparsing/dataset) and deployed the .tflite model on Android to detect in real time.

# Download and Requirements
```
$ git clone https://github.com/leaving-voider/Android-based_Fashion_Dection_in_real_time.git

Python 3.8 or later with all requirements.txt dependencies installed, including tensorflow>=2.4.0 To install run:

$ pip install -r requirements.txt
```

# Example for Custom Dataset
- Download Color-Fashion Dataset
$ cd Android-based_Fashion_Dection_in_real_time
# if needed
# !chmod +x download.sh
$ ./download.sh

$ mv data ../code/data.zip

$ unzip ../code/data.zip > /dev/null 

- Dataset Format Transformation
Packing training and testing data into a specific file format which is ".tfrecord", you can do this by run 
```
$ cd ../code
-- Transform test data
$ python generate_tfrecord.py --csv_input ../sources/test_labels.csv --output_path test.record
-- Transform train data
$ python generate_tfrecord.py --csv_input ../sources/train_labels.csv --output_path train.record
```

# Tutorial Colab
Follow [colab for whole process](https://github.com/leaving-voider/Android-based_Fashion_Dection_in_real_time/blob/master/code/jupyter%20notebook.ipynb) to train your model on custom dataset on lolab
