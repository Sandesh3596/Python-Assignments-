import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler



def Marvellousclassifier(DataPath):
    border = "_"* 50

    # Step 1: Load the Dataset from csv file

    print(border)
    print("Step 1: Load the Dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from Dataset: ")
    print(df.head())
    print(border)

    # Step 2: Clean, Prepare & Manipulate the Data

    print(border)
    print("Step 2: Clean, Prepare & Manipulate the Data")
    print(border)

    df.dropna(inplace = True)

    print("Shape of Dataset: ",df.shape)
    print('Total records: ',df.shape[0])
    print("Total columns: ",df.shape[1])

    print(border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    print(border)

    print("Input Columns : ",X.columns.tolist())
    print("Output Columns: Class")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.5, random_state= 42, stratify= Y)

    print(border)
    print("Details of Training and Testing Data")

    print("Shape of X_train: ", X_train.shape)
    print("Shape of X_test: ", X_test.shape)
    print("Shape of Y_train: ", Y_train.shape)
    print("Shape of Y_train: ", Y_train.shape)
    print(border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature Scaling Done")
    print(border)

    model = KNeighborsClassifier(n_neighbors= 9)

    print("Classification model is created")

    #Step 3 : Train the model

    print(border)
    print("Step 3: Train the model")
    print(border)

    model = model.fit(X_train_scaled,Y_train)

    print("Model training Completed")

    print(border)

    #Step 4 : Test the model
    
    print(border)
    print("Step 4: Test the model")
    print(border)
    
    y_pred = model.predict(X_test_scaled)
    print("Model Testing Completed")

    #Step 5: Calculate Accuracy
        
    print(border)
    print("Step 5: Calculate Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test,y_pred)
    print("The accuracy is ",accuracy*100)
    print(border)

def main():
    Marvellousclassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()