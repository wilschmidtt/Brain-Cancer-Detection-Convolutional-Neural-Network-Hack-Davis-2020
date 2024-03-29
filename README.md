# Brain Cancer Detection Convolutional Neural Network - HackDavis 2020
#### The Event 
UC Davis's Premir Hack-A-Thon for social good! On January 18-19, over 600 students, hackers, and creators came together for 24 hours of hacking. For the 5th year in a row, the most talented students in California come together to address the world’s most pressing issues. Participants are able to build projects that address any social good initiatives.
#### Team's Solution
Build and train a Convolutional Neural Network to detect if brain scans show signs of cancer. [View Project Website Here](https://devpost.com/software/ml-diagnose)

### Prerequisites
* Python 3.7
 
## Libraries
* keras - neural network library

## Running the Program

* First, download the files titled brain_tumor_model.json and brain_tumor_model.h5 and save them to a desired directory.
* Next, run the program titled: brain_tumor_prediction_regression.py
  - NOTE: There is another file titled Brain_Hemorrhage_CNN.py. This file contains much of the same code as brain_tumor_prediction_regression.py; however, this is the module that was used to train the CNN, and running it will take a significant amount of time. The regression equation has been exported to the brain_tumor_prediction_regression.py file, so this one will be much quicker to run.
* Next, user will need to change the program lines containing the directories of the .json and .h5 files that were used to store the regression equation. The line used to open the .json file looks as follows: `json_file = open('/content/drive/My Drive/Brain Tumor CNN/brain_tumor_model.json', 'r')`. As you can see, I had this file saved to a folder in my Google Drive; nevertheless, the user will have to change the specified directory to match that of where the .json file is located for them. Next, the code used to import the .h5 file is as follows: `loaded_model.load_weights("/content/drive/My Drive/Brain Tumor CNN/brain_tumor_model.h5")`. This too will need to be changed to match the directory that the user saved the .h5 file in.
* Finally, the user will need to obtain an image of a brain scan in question. How to go about obtaining this image is up to the user's disgression. The image can be of any format. Once obtained, save the image to a desired directory. The line of code within the program used to make a prediction about the image is as follows: `user_data = test_datagen.flow_from_directory('/content/drive/My Drive/Brain Tumor CNN/User-Data/test', target_size = (64, 64), batch_size = 1, class_mode = 'binary')`. As can be seen, the image that I used was located inside of my Google Drive. This directory will need to be changed to match the directory of the user's image.
* Once the program is run, the user can expect to see one of two messages: 
  1) The convolutional neural network predicts that that this immage doesn't show signs of hemorrhage.
  2) The convolutional neural network predicts that this image shows signs of a brain-hemorrhage!

## Final Thoughts
* The model was trained using the free Google Colaboratory service and their remote GPU, but the time required to train this model was still substantial. If the user has access to more computing power, then this model can be trained with more data and epochs, and reach even higher accuracy. The file used to train the neurl network is titled "Brain_Hemorrhage_CNN.py", and users can feel free to run this program on their own GPU, tune the parameters differently, and use any training data desired.

## Authors

* **William Schmidt** - [Wil's LinkedIn](https://www.linkedin.com/in/william-schmidt-152431168/)
* **Danial Khan** - [Danial's LinkedIn](https://www.linkedin.com/in/danial-khan-98415b18b/), [Danial's GitHub](https://github.com/danialk1?tab=repositories)
* **Matthew Meer** - [Matt's LinkedIn](https://www.linkedin.com/in/matthew-meer-8356b572/), [Matt's GitHub](https://github.com/meerkat1293?tab=repositories)
* **Awen Li** - [Awen's GitHub](https://github.com/BabyMochi)

## Acknowledgments

* Thank you to UC Davis and Major League Hacking for hosting this event!
  - [HackDavis 2020 Website](https://hackdavis2020.devpost.com/?ref_content=default&ref_feature=challenge&ref_medium=discover)
