# Rice Grain Purity Analysis Using Deep Learning
In this repository we present the paper ```A Deep Convolutional Neural Network Approach To Rice Grain Purity Analysis	``` .One of the significant factor of a rice grain purity is measured by the percentage of foreign grains mixture. Most of the Rice traders used to verify the purity of rice grain by Manual annotations done by labours with the years of experience. But this process is Costly and produce erronous result in most cases. Which also takes very long time. So ths work is going find the purity of a Rice sample within a few seconds and with a very good accuracy from a scanned image of the sample. 
The ultimate result will detect each grains and classify it to its corresponding grain type. 

<img src="https://github.com/Mushahid2521/Rice-Grain-Purity-Analysis-Using-Deep-Learning/blob/master/images/Test15.jpg?raw=1" alt="Image" height="300" width="200"/> <img src="https://github.com/Mushahid2521/Rice-Grain-Purity-Analysis-Using-Deep-Learning/blob/master/images/predicted_img.jpg?raw=1" alt="Image" height="300" width="200"/> 

## Dataset
We are publishing a Dataset for rice grain classification for further improvement. **Note: This Dataset can be only used for research purposes**. You can have a look at the ```sample images``` folder to have a glipse of the dataset. 
If you want to access the full Dataset please email me at ```mushahidshamim@gmail.com``` mentioning in the following informations.

```
Subject: Rice Grain Dataset
Name of your Institution:
Affiliation:  
```

## Usage
You can use the pretrained model downloading from this [link](https://drive.google.com/open?id=1Pw7f619X7WqKxGbhvGJdiTpUu2QqJhXe). After downloading the model you can run the following command to prodcude the result.

```python3 predict.py model.py Test.jpg```

## Training and Dataset Preparation
You can use the ```Rice_Grain_Analysis.ipynb``` notebook to train the model from scratch. All the codes are documented well. You can also run the code in Google ```Colab``` after uploading the Dataset in Google Drive and mounting the drive. To do this you need to run the following code snippet.
```
from google.colab import drive
drive.mount('/content/drive/')
cd /content/drive/My Drive/folder_name
```

