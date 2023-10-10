from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from .models import BUPA_Data , HeartDisease
from .serializers import BUPA_DataSerializer , HeartDiseaseSerializer , ChronicKidneyPredictionSerializer ,DiabeticsPredictionSerializer
import joblib

def home(request):
  return render(request , 'home.html')



# Load the machine learning model

bupa_model = joblib.load('ml_models/ml_bupa_model.joblib')
heardiseases_model = joblib.load('ml_models/heart_diseases_model.joblib')

@api_view(['POST'])
def predict_bupa_data(request):
    if request.method == 'POST':
        serializer = BUPA_DataSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data from the serializer
            mcv = serializer.validated_data.get('mcv')
            alkphos = serializer.validated_data.get('alkphos')
            sgpt = serializer.validated_data.get('sgpt')
            sgot = serializer.validated_data.get('sgot')
            gammagt = serializer.validated_data.get('gammagt')
            drinks = serializer.validated_data.get('drinks')
            prediction = bupa_model.predict([[mcv, alkphos, sgpt, sgot, gammagt, drinks]])
            prediction = prediction[0]
            if prediction == 1:
                prediction_message = "The patient is likely to have liver disease."
            else:
                prediction_message = "The patient is not likely to have liver disease."
            # Update the 'predictions' field in the serializer
            serializer.validated_data['predictions'] = prediction
            serializer.validated_data['prediction_message'] = prediction_message
            # Save the serializer instance to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








@api_view(['POST'])
def predict_heart_disease(request):
    if request.method == 'POST':
        serializer = HeartDiseaseSerializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from the serializer
            age = serializer.validated_data['age']
            hypertension = serializer.validated_data['hypertension']
            heart_disease = serializer.validated_data['heart_disease']
            avg_glucose_level = serializer.validated_data['avg_glucose_level']
            bmi = serializer.validated_data['bmi']
            gender_Male = serializer.validated_data['gender_Male']
            gender_Other = serializer.validated_data['gender_Other']
            work_type_Never_worked = serializer.validated_data['work_type_Never_worked']
            work_type_Private = serializer.validated_data['work_type_Private']
            work_type_Self_employed = serializer.validated_data['work_type_Self_employed']
            work_type_children = serializer.validated_data['work_type_children']
            Residence_type_Urban = serializer.validated_data['Residence_type_Urban']
            smoking_status_formerly_smoked = serializer.validated_data['smoking_status_formerly_smoked']
            smoking_status_never_smoked = serializer.validated_data['smoking_status_never_smoked']
            smoking_status_smokes = serializer.validated_data['smoking_status_smokes']

            # Make predictions using the machine learning model
            prediction = heardiseases_model.predict([
                [age, hypertension, heart_disease, avg_glucose_level, bmi,
                 gender_Male, gender_Other, work_type_Never_worked,
                 work_type_Private, work_type_Self_employed, work_type_children,
                 Residence_type_Urban, smoking_status_formerly_smoked,
                 smoking_status_never_smoked, smoking_status_smokes]
            ])[0]

            # Update the prediction field in the serializer
            serializer.validated_data['stroke'] = prediction

            if prediction == 1:
                serializer.validated_data['prediction_message'] = "The patient is likely to have a stroke."
            else:
                serializer.validated_data['prediction_message'] = "The patient is not likely to have a stroke."

            # Save the data to the database
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def predict_chronic_kidney_data(request):
    if request.method == 'POST':
        serializer = ChronicKidneyPredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data from the serializer
            data = serializer.validated_data

            # Create a dictionary with keys matching the model fields
            data_dict = {
                'Bp': data.get('Bp'),
                'Sg': data.get('Sg'),
                'Al': data.get('Al'),
                'Su': data.get('Su'),
                'Rbc': data.get('Rbc'),
                'Bu': data.get('Bu'),
                'Sc': data.get('Sc'),
                'Sod': data.get('Sod'),
                'Pot': data.get('Pot'),
                'Hemo': data.get('Hemo'),
                'Wbcc': data.get('Wbcc'),
                'Rbcc': data.get('Rbcc'),
                'Htn': data.get('Htn'),
            }

            # Load the machine learning model
            ml_model = joblib.load('ml_models/chronic_kidney_model.joblib')

            # Make a prediction using the model
            prediction = ml_model.predict([list(data_dict.values())])
            prediction = prediction[0]

            # Set the prediction and prediction_message in the serializer
            serializer.validated_data['prediction'] = prediction
            serializer.validated_data['prediction_message'] = 'The patient has a high risk of chronic kidney disease.' if prediction == 1 else 'The patient is not likely to have chronic kidney disease.'

            # Save the data to the database
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def predict_diabetics_data(request):
    if request.method == 'POST':
        serializer = DiabeticsPredictionSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract data from the serializer
            data = serializer.validated_data

            # Prepare the input data as a dictionary
            data_dict = {
                "quality_assessment": data.get('quality_assessment'),
                "pre_screening": data.get('pre_screening'),
                "ma_confidence_level_0_5": data.get('ma_confidence_level_0_5'),
                "ma_confidence_level_0_6": data.get('ma_confidence_level_0_6'),
                "ma_confidence_level_0_7": data.get('ma_confidence_level_0_7'),
                "ma_confidence_level_0_8": data.get('ma_confidence_level_0_8'),
                "ma_confidence_level_0_9": data.get('ma_confidence_level_0_9'),
                "ma_confidence_level_1_0": data.get('ma_confidence_level_1_0'),
                "exudates_confidence_level_0_5": data.get('exudates_confidence_level_0_5'),
                "exudates_confidence_level_0_6": data.get('exudates_confidence_level_0_6'),
                "exudates_confidence_level_0_7": data.get('exudates_confidence_level_0_7'),
                "exudates_confidence_level_0_8": data.get('exudates_confidence_level_0_8'),
                "exudates_confidence_level_0_9": data.get('exudates_confidence_level_0_9'),
                "exudates_confidence_level_1_0": data.get('exudates_confidence_level_1_0'),
                "exudates_normalized_by_roi_1": data.get('exudates_normalized_by_roi_1'),
                "exudates_normalized_by_roi_2": data.get('exudates_normalized_by_roi_2'),
                "macula_optic_disc_distance": data.get('macula_optic_disc_distance'),
                "optic_disc_diameter": data.get('optic_disc_diameter'),
                "am_fm_based_classification": data.get('am_fm_based_classification')
            }

            # Load the machine learning model
            ml_model = joblib.load('ml_models/diabetics_prediction_model.joblib')
            
            # Make the prediction using values from data_dict
            prediction = ml_model.predict([list(data_dict.values())])
            
            # Determine prediction message based on the prediction
            if prediction[0] == 0:
                prediction_message = "No diabetes detected."
            else:
                prediction_message = "Diabetes detected."

            # Save the prediction to the database
            serializer.save(prediction=prediction[0], prediction_message=prediction_message)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)