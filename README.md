Still in process of creating this repo

# Brain Cancer Detection Convolutional Neural Network - HackDavis 2020
![Image](Images/catalog.png)
#### The Event 
UC Davis's Premir Hack-A-Thon for social good! On January 18-19, over 600 students, hackers, and creators will came together for 24 hours of hacking. For the 5th year in a row, the most talented students in California come together to address the world’s most pressing issues. Participants are able to build projects that address any social good initiatives.
#### Team's Solution
Build and train a Convolutional Neural Network to detect if brain scans show signs of a malignant tumor. 
[Project Website](https://devpost.com/software/ml-diagnose)

### Prerequisites
* Anaconda (Python 3.7 Version)
  - [Anaconda Instillation Instructions](https://docs.anaconda.com/anaconda/install/)
  - Chosing to use Anaconda is optional; however, the Spyder environment included is very useful for Machine Learning projects

## Libraries to Install
* keras - neural network library
  - `conda install -c conda-forge keras`

## Running the tests

* First, download the files titled brain_tumor_model.json and brain_tumor_model.h5 and save them to a desired directory.
* Next, open Anaconda, launch Spyder (used version 3.3.6 to create this program), and run the program titled: brain_tumor_prediction_regression.py
  - NOTE: There is another file titled Brain_Hemorrhage_CNN.py. This file contains much of the same code as brain_tumor_prediction_regression.py; however, this is the module that was used to train the CNN, and running it will take a significant amount of time. The regression equation has been exported to the brain_tumor_prediction_regression.py file, so this one will be much quicker to run.
* Next, user will need to change the directory of the .json and .h5 files that were used to store the regression equation. The line used to open the .json file looks as follows: `json_file = open('/content/drive/My Drive/Brain Tumor CNN/brain_tumor_model.json', 'r')`. As you can see, I had this file saved to a folder in my Google Drive; nevertheless, the user will have to change the specified directory to match that of where the .json file is located. The code used to import the .h5 file is as follows: `loaded_model.load_weights("/content/drive/My Drive/Brain Tumor CNN/brain_tumor_model.h5")`. This too will need to be changed to match the directory that you saved the .h5 file in.
* Finally, the user will need to obtain an image a brain scan in question. How to go about obtaining this image is up to the user's disgression. The image can be of any format. Once obtained, save the image to a desired directory. The line of code to make a prediction about the image is as follows: `user_data = test_datagen.flow_from_directory('/content/drive/My Drive/Brain Tumor CNN/User-Data/test', target_size = (64, 64), batch_size = 1, class_mode = 'binary')`. As can be seen, the image that I used was located inside of my Google Drive. This directory will need to be changed to match the directory of your image.
* Once the program is run, the user can expect to see one of two messages: 
  1) The convolutional neural network predicts that that this immage doesn't show signs of hemorrhage.
  OR 
  2) The convolutional neural network predicts that this image shows signs of a brain-hemorrhage!

## Final Thoughts
* After training the model, our team was able to get it to classify images in the test set with 99.12% accuracy. The model was trained using the free Google Colaboratory service and their remote GPU, but the time required to train this model was still substantial. If the user has access to more computing power, then this model can be trained with more data and epochs, and reach even closer to perfect accuracy. The file used to train the neurl network is titled "Brain_Hemorrhage_CNN.py", and users can feel free to run this program on their own GPU and use any training data desired. Our group was limited by the computing power available to us at the time.

## Authors

* **William Schmidt** - [Wil's LikedIn](https://www.linkedin.com/in/william-schmidt-152431168/)
* 

## Acknowledgments

* Thank you to UC Davis for hosting this event!
  - [HackDavis 2020 Website](https://hackdavis2020.devpost.com/?ref_content=default&ref_feature=challenge&ref_medium=discover)
