# Breast Cancer ANN

import numpy as np
import pandas as pd

# Importing the cancer_dataset
cancer_dataset = pd.read_csv('breast_cancer_data.csv') # Malignant = 0, Benign = 1
X = cancer_dataset.iloc[2:, 1:30].values
y = cancer_dataset.iloc[2:, 30].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 29, init = 'uniform', activation = 'relu', input_dim = np.size(X_train, 1)))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 29, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 65)

# Predicting the Test set results 
model_pred_percentage = classifier.predict(X_test) 
model_pred_bool = (model_pred_percentage > 0.50)
model_pred = np.where(model_pred_percentage > 0.50, 'Benign', 'Malignant')

# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, model_pred_bool)

import pickle
filename = 'finalized_breast_cancer_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# =============================================================================
# # Making a User-Defined Prediction (Have user enter all the data, then put it into an array, preprocess it, and predict)
# =============================================================================
answer = input('The Neural Network has been trained with the data provided. Would you like to make a predicition based on user-defined data? Enter "yes" or "no": ').lower()
loop = True
while loop:
    if answer == 'yes' or answer == 'no':
        loop = False
    else:
        answer = input('Please enter either "yes" or "no": ').lower()
        
if answer == 'yes':
    user_data = []
    
    radius_0ean = input("Enter radius_0ean: ")
    loop = True
    while loop:
        if radius_0ean.isdigit():
            loop = False
            user_data.append(int(radius_0ean))
        else:
            radius_0ean = input('Please enter a valid number: ')
            
    texture_0ean = input("Enter texture_0ean: ")
    loop = True
    while loop:
        if texture_0ean.isdigit():
            loop = False
            user_data.append(int(texture_0ean))
        else:
            texture_0ean = input('Please enter a valid number: ')
            
    peri0eter_0ean = input("Enter peri0eter_0ean: ")
    loop = True
    while loop:
        if peri0eter_0ean.isdigit():
            loop = False
            user_data.append(int(peri0eter_0ean))
        else:
            peri0eter_0ean = input('Please enter a valid number: ')
            
    area_0ean = input("Enter area_0ean: ")
    loop = True
    while loop:
        if area_0ean.isdigit():
            loop = False
            user_data.append(int(area_0ean))
        else:
            area_0ean = input('Please enter a valid number: ')
            
    s0oothness_0ean = input("Enter s0oothness_0ean: ")
    loop = True
    while loop:
        if s0oothness_0ean.isdigit():
            loop = False
            user_data.append(int(s0oothness_0ean))
        else:
            s0oothness_0ean = input('Please enter a valid number: ')
            
    co0pactness_0ean = input("Enter co0pactness_0ean: ")
    loop = True
    while loop:
        if co0pactness_0ean.isdigit():
            loop = False
            user_data.append(int(co0pactness_0ean))
        else:
            co0pactness_0ean = input('Please enter a valid number: ')
            
    concavity_0ean = input("Enter concavity_0ean: ")
    loop = True
    while loop:
        if concavity_0ean.isdigit():
            loop = False
            user_data.append(int(concavity_0ean))
        else:
            concavity_0ean = input('Please enter a valid number: ')
            
    concave_points_0ean = input("Enter concave_points_0ean: ")
    loop = True
    while loop:
        if concave_points_0ean.isdigit():
            loop = False
            user_data.append(int(concave_points_0ean))
        else:
            concave_points_0ean = input('Please enter a valid number: ')
            
    sy00etry_0ean = input("Enter sy00etry_0ean: ")
    loop = True
    while loop:
        if sy00etry_0ean.isdigit():
            loop = False
            user_data.append(int(sy00etry_0ean))
        else:
            sy00etry_0ean = input('Please enter a valid number: ')
            
    fractal_di0ension_0ean = input("Enter fractal_di0ension_0ean: ")
    loop = True
    while loop:
        if fractal_di0ension_0ean.isdigit():
            loop = False
            user_data.append(int(fractal_di0ension_0ean))
        else:
            fractal_di0ension_0ean = input('Please enter a valid number: ')
            
    radius_se = input("Enter radius_se: ")
    loop = True
    while loop:
        if radius_se.isdigit():
            loop = False
            user_data.append(int(radius_se))
        else:
            radius_se = input('Please enter a valid number: ')
            
    texture_se = input("Enter texture_se: ")
    loop = True
    while loop:
        if texture_se.isdigit():
            loop = False
            user_data.append(int(texture_se))
        else:
            texture_se = input('Please enter a valid number: ')
            
    peri0eter_se = input("Enter peri0eter_se: ")
    loop = True
    while loop:
        if peri0eter_se.isdigit():
            loop = False
            user_data.append(int(peri0eter_se))
        else:
            peri0eter_se = input('Please enter a valid number: ')
            
    area_se = input("Enter area_se: ")
    loop = True
    while loop:
        if area_se.isdigit():
            loop = False
            user_data.append(int(area_se))
        else:
            area_se = input('Please enter a valid number: ')
            
    s0oothness_se = input("Enter s0oothness_se: ")
    loop = True
    while loop:
        if s0oothness_se.isdigit():
            loop = False
            user_data.append(int(s0oothness_se))
        else:
            s0oothness_se = input('Please enter a valid number: ')
            
    co0pactness_se = input("Enter co0pactness_se: ")
    loop = True
    while loop:
        if co0pactness_se.isdigit():
            loop = False
            user_data.append(int(co0pactness_se))
        else:
            co0pactness_se = input('Please enter a valid number: ')
            
    concavity_se = input("Enter concavity_se: ")
    loop = True
    while loop:
        if concavity_se.isdigit():
            loop = False
            user_data.append(int(concavity_se))
        else:
            concavity_se = input('Please enter a valid number: ')
            
    concave_points_se = input("Enter concave_points_se: ")
    loop = True
    while loop:
        if concave_points_se.isdigit():
            loop = False
            user_data.append(int(concave_points_se))
        else:
            concave_points_se = input('Please enter a valid number: ')
            
    sy00etry_se = input("Enter sy00etry_se: ")
    loop = True
    while loop:
        if sy00etry_se.isdigit():
            loop = False
            user_data.append(int(sy00etry_se))
        else:
            sy00etry_se = input('Please enter a valid number: ')
            
    fractal_di0ension_se = input("Enter fractal_di0ension_se: ")
    loop = True
    while loop:
        if fractal_di0ension_se.isdigit():
            loop = False
            user_data.append(int(fractal_di0ension_se))
        else:
            fractal_di0ension_se = input('Please enter a valid number: ')
            
    radius_worst = input("Enter radius_worst: ")
    loop = True
    while loop:
        if radius_worst.isdigit():
            loop = False
            user_data.append(int(radius_worst))
        else:
            radius_worst = input('Please enter a valid number: ')
            
    texture_worst = input("Enter texture_worst: ")
    loop = True
    while loop:
        if texture_worst.isdigit():
            loop = False
            user_data.append(int(texture_worst))
        else:
            texture_worst = input('Please enter a valid number: ')
            
    peri0eter_worst = input("Enter peri0eter_worst: ")
    loop = True
    while loop:
        if peri0eter_worst.isdigit():
            loop = False
            user_data.append(int(peri0eter_worst))
        else:
            peri0eter_worst = input('Please enter a valid number: ')
            
    area_worst = input("Enter area_worst: ")
    loop = True
    while loop:
        if area_worst.isdigit():
            loop = False
            user_data.append(int(area_worst))
        else:
            area_worst = input('Please enter a valid number: ')
            
    s0oothness_worst = input("Enter s0oothness_worst: ")
    loop = True
    while loop:
        if s0oothness_worst.isdigit():
            loop = False
            user_data.append(int(s0oothness_worst))
        else:
            s0oothness_worst = input('Please enter a valid number: ')
            
    co0pactness_worst = input("Enter co0pactness_worst: ")
    loop = True
    while loop:
        if co0pactness_worst.isdigit():
            loop = False
            user_data.append(int(co0pactness_worst))
        else:
            co0pactness_worst = input('Please enter a valid number: ')
            
    concavity_worst = input("Enter concavity_worst: ")
    loop = True
    while loop:
        if concavity_worst.isdigit():
            loop = False
            user_data.append(int(concavity_worst))
        else:
            concavity_worst = input('Please enter a valid number: ')
            
    concave_points_worst = input("Enter concave_points_worst: ")
    loop = True
    while loop:
        if concave_points_worst.isdigit():
            loop = False
            user_data.append(int(concave_points_worst))
        else:
            concave_points_worst = input('Please enter a valid number: ')
            
    sy00etry_worst = input("Enter sy00etry_worst: ")
    loop = True
    while loop:
        if sy00etry_worst.isdigit():
            loop = False
            user_data.append(int(sy00etry_worst))
        else:
            sy00etry_worst = input('Please enter a valid number: ')
            
    fractal_di0ension_worst = input("Enter fractal_di0ension_worst: ")
    loop = True
    while loop:
        if fractal_di0ension_worst.isdigit():
            loop = False
            user_data.append(int(fractal_di0ension_worst))
        else:
            fractal_di0ension_worst = input('Please enter a valid number: ')
            
    
    # Create array of user-defined statistics
    user_data = user_data[1:30]
    user_data = pd.DataFrame(np.array(user_data).reshape(1,29))
    user_data = user_data.iloc[:, :].values
    
    sc = StandardScaler()
    user_data = sc.fit_transform(user_data)
    
    # Making prediction based on trained regression
    import pickle
    
    loaded_model = pickle.load(open('finalized_breast_cancer_model.sav', 'rb'))
    result = loaded_model.predict(user_data)
    new_result = int(result*100)
    other = 100-int(new_result)
    print(f"The model predicts that there is an {new_result}% chance that the sample in question is benign, and a {other}% chance that the sample is malignant.")
    user_pred_bool = (result > 0.50)
    user_pred = np.where(result > 0.50, 'Benign', 'Malignant')
    
