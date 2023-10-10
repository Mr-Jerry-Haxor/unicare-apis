from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



class BUPA_Data(models.Model):
    mcv = models.PositiveIntegerField(validators=[MinValueValidator(65), MaxValueValidator(103)], null=True)
    alkphos = models.PositiveIntegerField( validators=[MinValueValidator(23), MaxValueValidator(138)], null=True)
    sgpt = models.PositiveIntegerField(validators=[MinValueValidator(4), MaxValueValidator(155)], null=True)
    sgot = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(82)], null=True)
    gammagt = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(297)], null=True)
    drinks = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)],null=True)
    predictions = models.CharField(max_length=200, blank=True)
    prediction_message = models.CharField(max_length=200, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date']



class HeartDisease(models.Model):
    age = models.FloatField(validators=[MinValueValidator(0.08), MaxValueValidator(82.0)])
    hypertension = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    heart_disease = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    avg_glucose_level = models.FloatField(validators=[MinValueValidator(55.12), MaxValueValidator(271.74)])
    bmi = models.FloatField(validators=[MinValueValidator(10.3), MaxValueValidator(97.6)])
    gender_Male = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    gender_Other = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    work_type_Never_worked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    work_type_Private = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    work_type_Self_employed = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    work_type_children = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    Residence_type_Urban = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    smoking_status_formerly_smoked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    smoking_status_never_smoked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    smoking_status_smokes = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    stroke = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)],blank=True)
    prediction_message = models.CharField(max_length=200, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']


class ChronicKidneyPrediction(models.Model):
    Bp = models.PositiveIntegerField(validators=[MinValueValidator(50), MaxValueValidator(180)])
    Sg = models.FloatField(validators=[MinValueValidator(1.005), MaxValueValidator(1.025)])
    Al = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    Su = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    Rbc = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    Bu = models.FloatField(validators=[MinValueValidator(1.5), MaxValueValidator(391.0)])
    Sc = models.FloatField(validators=[MinValueValidator(0.4), MaxValueValidator(76.0)])
    Sod = models.FloatField(validators=[MinValueValidator(4.5), MaxValueValidator(163.0)])
    Pot = models.FloatField(validators=[MinValueValidator(2.5), MaxValueValidator(47.0)])
    Hemo = models.FloatField(validators=[MinValueValidator(3.1), MaxValueValidator(17.8)])
    Wbcc = models.PositiveIntegerField(validators=[MinValueValidator(2200), MaxValueValidator(26400)])
    Rbcc = models.FloatField(validators=[MinValueValidator(2.1), MaxValueValidator(8.0)])
    Htn = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    prediction = models.PositiveIntegerField(null=True, blank=True)
    prediction_message = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']


class DiabeticsPrediction(models.Model):
    quality_assessment = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    pre_screening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    ma_confidence_level_0_5 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(151)])
    ma_confidence_level_0_6 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(132)])
    ma_confidence_level_0_7 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    ma_confidence_level_0_8 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(105)])
    ma_confidence_level_0_9 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(97)])
    ma_confidence_level_1_0 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(89)])
    exudates_confidence_level_0_5 = models.FloatField(validators=[MinValueValidator(0.349274), MaxValueValidator(403.939108)])
    exudates_confidence_level_0_6 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(167.131427)])
    exudates_confidence_level_0_7 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(106.070092)])
    exudates_confidence_level_0_8 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(59.766121)])
    exudates_confidence_level_0_9 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(51.423208)])
    exudates_confidence_level_1_0 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.098605)])
    exudates_normalized_by_roi_1 =models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.937799)])
    exudates_normalized_by_roi_2 =models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.937799)])
    macula_optic_disc_distance = models.FloatField(validators=[MinValueValidator(0.367762), MaxValueValidator(0.592217)])
    optic_disc_diameter = models.FloatField(validators=[MinValueValidator(0.057906), MaxValueValidator(0.219199)])
    am_fm_based_classification = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    prediction = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], blank=True)
    prediction_message = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

