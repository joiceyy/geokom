# Data Processing
import numpy as np
import pandas as pd

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn import svm
from sklearn.ensemble import *
from sklearn.linear_model import *
from sklearn.naive_bayes import *
from sklearn.neighbors import *
from sklearn.svm import *
from sklearn.tree import *
from catboost import CatBoostClassifier

# Prepare Train Tes Data
def prepare_train_test_data(dataset_ml, test_size):
    X = dataset_ml[[col for col in dataset_ml.columns if col not in ['num_lithology', 'lithology', ]]]
    Y = dataset_ml['num_lithology']
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
                                                        random_state=32,  
                                                        test_size=test_size, 
                                                        shuffle=True)
    par_input = [col for col in X]

    input_train = X_train[par_input].values
    input_test = X_test[par_input].values
    output_train = Y_train.values
    output_test = Y_test.values
    
    output_train = change_obj_to_int_arrays(output_train)
    output_test = change_obj_to_int_arrays(output_test)
    return input_train, input_test, output_train, output_test

# Change Objek to Integer Arrays
def change_obj_to_int_arrays(arrays:[]):
    return [int(obj) for obj in arrays]

#  MinMax Normalization
# (x - min(x)) / (max(x) - min(x))
def minMaxNormalization(dataset_ml_col):
    return (dataset_ml_col - dataset_ml_col.min())/(dataset_ml_col.max() - dataset_ml_col.min())

# Mean Normalization
# (x - mean(x)) / std(x)
def meanNormalization(dataset_ml_col):
    return (dataset_ml_col - dataset_ml_col.mean())/dataset_ml_col.std()
    
# Normalization
def normalization(dataset_ml, method):
    for col in dataset_ml.columns:
        if col not in ['longitude', 'latitude', 'lithology', 'num_lithology']:
            if method == 'Min-Max':
                dataset_ml[col] = minMaxNormalization(dataset_ml[col])
            elif method == 'Mean':
                dataset_ml[col] = meanNormalization(dataset_ml[col])

    return dataset_ml

# Model Fitting
def model_fitting(model, input_train, input_test, output_train, output_test):
    model.fit(input_train,output_train)
    predict_train = model.predict(input_train)
    predict_test = model.predict(input_test)
    print('### Model Accuracy - Train ### \n')
    print(classification_report(output_train, predict_train))
    print('Accuracy Score:', accuracy_score(output_train, predict_train))
    print('===========================================================')
    print('\n ### Model Accuracy - Test ###')
    print(classification_report(output_test, predict_test))
    print('Accuracy Score:', accuracy_score(output_test, predict_test))

# Read Dataset
dataset_raw = pd.read_excel('Dataset/data_train.xlsx')
dataset = dataset_raw.copy()

# Data Null
dataset.isnull().sum()
dataset.dropna(inplace=True)
dataset.reset_index(drop=True, inplace=True)


#kode untuk pencarian anomaly (boxplot)
boxplot_fields = ['band_1', 'band_2', 'band_3', 'band_4', 'band_5', 'band_6', 'band_7', 'band_8']
dataset.boxplot(column=boxplot_fields)
plt.show()
dataset = dataset[
   (dataset['band_1'] <= 40000) 
  & (dataset['band_2'] <= 40000)
  & (dataset['band_3'] <= 40000)
  & (dataset['band_4'] <= 40000)
  & (dataset['band_5'] <= 40000)
  & (dataset['band_6'] <= 40000)
  & (dataset['band_7'] <= 40000)
  & (dataset['band_8'] <= 40000)
]

dataset.reset_index(drop=True, inplace=True)
boxplot_fields = ['band_1', 'band_2', 'band_3', 'band_4', 'band_5', 'band_6', 'band_7', 'band_8']
dataset.boxplot(column=boxplot_fields)
plt.show()
dataset[(dataset['longitude'] <= 0) & (dataset['latitude'] <= 0)]

#Penentuan nilai EVI
dataset['evi'] = 2.5 * (dataset["band_8"] - dataset["band_4"])/(dataset["band_8"] + 6 * dataset["band_4"] - 7.5 * dataset["band_2"] + 1)

geo_fields = ['band_1', 'band_2', 'band_3', 'band_4', 'band_5', 'band_6', 'band_7', 'band_8', 'gcvi', 'ndbi', 'mndwi', 'ndmi', 'lswi']
dataset[geo_fields].describe()
dataset['lithology'].value_counts().plot(kind='bar')
plt.title('Lithology Frequency ')
plt.ylabel('Frequency')
plt.show()

sns.scatterplot(data=dataset, x='longitude',
                y='latitude', palette = ['yellow', '#8a3c0e', 'grey', 'green', 'red', '#00ccff'],
                hue='lithology', style='lithology')
plt.title('Lithology Map')
plt.show()

dataset[geo_fields].corr()

dataset_ml=dataset.copy()
dataset_ml.dtypes
dataset_ml['lithology'].unique()
pd.set_option('future.no_silent_downcasting', True)


#Kamus litologi
num_lith={'Sandstone':1, 'Conglomerate':2, 'Alluvial':3, 'Clay': 4, 'Granite': 5,
       'Limestone':6}
dataset_ml['num_lithology']=dataset_ml['lithology'].replace(num_lith)


dataset_ml_minmax = normalization(dataset_ml, 'Min-Max')
dataset_ml_mean = normalization(dataset_ml, 'Mean')



input_train, input_test, output_train, output_test = prepare_train_test_data(dataset_ml_mean, 0.3)

model_fittings = {
  # "RandomForestClassifier": RandomForestClassifier(),
  # "DecisionTreeClassifier": DecisionTreeClassifier(),
  # "RidgeClassifier": RidgeClassifier(),
  # "LogisticRegression": LogisticRegression(),
  # "GaussianNB": GaussianNB(),
  # "CatBoostClassifier": CatBoostClassifier(),
#   "GradientBoostingClassifier": GradientBoostingClassifier(),
#   "AdaBoostClassifier": AdaBoostClassifier(),
  "KNeighborsClassifier": KNeighborsClassifier(),
#   "SVC": SVC()
    }

for k, v in model_fittings.items():
    print("Algorithm: ", k)
    model_fitting(v, input_train, input_test, output_train, output_test)


# testing commit
