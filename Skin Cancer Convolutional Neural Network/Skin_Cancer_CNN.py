# Training the CNN

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid')) #softmax

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']) #categorical_crossentropy

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('/content/drive/My Drive/Skin Cancer CNN/skin-cancer-malignant-vs-benign.zip (Unzipped Files)/train',
                                                 target_size = (64, 64), # make sure to change target_size if you altered input_shape above
                                                 batch_size = 32,
                                                 class_mode = 'binary')
test_set = test_datagen.flow_from_directory('/content/drive/My Drive/Skin Cancer CNN/skin-cancer-malignant-vs-benign.zip (Unzipped Files)/test',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set,
                         samples_per_epoch = 2637,
                         nb_epoch = 25,
                         validation_data = test_set,
                         nb_val_samples = 660)

# saving model to JSON
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# saving weights to HDF5
classifier.save_weights("model.h5")

# Making prediction about user data
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator

# load json and create model
json_file = open('/content/drive/My Drive/Skin Cancer CNN/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/content/drive/My Drive/Skin Cancer CNN/model.h5")

from keras.preprocessing.image import ImageDataGenerator
test_datagen = ImageDataGenerator(rescale = 1./255)
user_data = test_datagen.flow_from_directory('/content/drive/My Drive/Skin Cancer CNN/User-Data/test',
                                            target_size = (64, 64),
                                            batch_size = 1,
                                            class_mode = 'binary')
 
# evaluate loaded model on user data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(user_data)
if score[1] == 0:
  print('The convolutional neural network predicts that this tumor is malignant!')
else:
  print('The convolutional neural network predicts that this tumor is benign.')
