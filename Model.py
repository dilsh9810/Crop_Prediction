import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import r2_score

#Load the dataset to the environment
df = pd.read_csv("Gardening Crops.csv")

df = df.iloc[:,:].values
df1 = pd.DataFrame(df)


#Get First Five Rows Of The Dataset
df1.head()


df1.dtypes


#Check Whether The Dataset Is Not Null
df1.isnull().any()


from sklearn.preprocessing import LabelEncoder, OneHotEncoder

Label = LabelEncoder()

df[:,6] = Label.fit_transform(df[:,6])

df1 = pd.DataFrame(df)

#Split The Dataset Values As Independent variables (X) And Dependent Variables (Y)

x = df1.iloc[:,0:6]
y = df1.iloc[:,-1]

y=y.astype('int')

x

#Split the x and y variables to train and test data
X_train, X_test, Y_train, Y_test =  train_test_split(x,y,test_size=0.25,random_state=0)


#Train the model
classifier = DecisionTreeClassifier(random_state=0)

classifier.fit(X_train,Y_train)

CropPredict = classifier.predict(X_test)

#CropPredict_train = classifier.predict(X_train)

Accuracy_score = r2_score(Y_test,CropPredict)
#Accuracy_scorenew = r2_score(X_test,CropPredict_train)

#Print the Crop Outputs and AccuracyScore

print(CropPredict)
print(CropPredict_train)
#print(Accuracy_scorenew)
print(Accuracy_score * 100)









