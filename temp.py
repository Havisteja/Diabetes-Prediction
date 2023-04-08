import numpy as np
import pickle
import streamlit as st
import mysql.connector



# loading the saved model
loaded_model = pickle.load(open('C:/Users/havis/Downloads/trained.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        diagnosis = 'The person is not diabetic , Updated Database'
        diagnosis1 = 0
    else:
        diagnosis = 'The person is diabetic ,Updated Database'
        diagnosis1 = 1
    
    insert_data(input_data,diagnosis1)
    
    return diagnosis
  
def insert_data(input_data, output_data):
    mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="snowworld",
     database="diabetesdb"
     )

    mycursor = mydb.cursor()
    sql = "INSERT INTO diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (input_data[0], input_data[1], input_data[2], input_data[3], input_data[4], input_data[5], input_data[6], input_data[7], output_data)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("Row inserted successfully")
  
def main():
   
    
    # giving a title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()