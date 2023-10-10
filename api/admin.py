from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.


class BUPADataAdmin(ImportExportModelAdmin):
    list_display = ('mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks', 'predictions', 'prediction_message')
    list_filter = ('predictions',)
    search_fields = ('predictions',)
    list_per_page = 25

admin.site.register(BUPA_Data, BUPADataAdmin)



@admin.register(HeartDisease)
class HeartDiseaseAdmin(ImportExportModelAdmin):
    list_display = (
        'age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
        'gender_Male', 'gender_Other', 'work_type_Never_worked',
        'work_type_Private', 'work_type_Self_employed', 'work_type_children',
        'Residence_type_Urban', 'smoking_status_formerly_smoked',
        'smoking_status_never_smoked', 'smoking_status_smokes', 'stroke', 'prediction_message'
    )
    list_filter = (
        'hypertension', 'heart_disease', 'gender_Male', 'work_type_Private',
        'Residence_type_Urban', 'smoking_status_formerly_smoked',
        'smoking_status_never_smoked', 'smoking_status_smokes', 'stroke'
    )
    search_fields = ('age', 'avg_glucose_level', 'bmi', 'date')
    date_hierarchy = 'date'
    list_per_page = 25

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
                'gender_Male', 'gender_Other', 'stroke'
            ),
        }),
        ('Work and Residence', {
            'fields': (
                'work_type_Never_worked', 'work_type_Private',
                'work_type_Self_employed', 'work_type_children', 'Residence_type_Urban',
            ),
        }),
        ('Smoking Status', {
            'fields': (
                'smoking_status_formerly_smoked',
                'smoking_status_never_smoked', 'smoking_status_smokes',
            ),
        }),
        ('Date Information', {
            'fields': ('date',),
        }),
    )

    readonly_fields = ('date',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('age', 'avg_glucose_level', 'bmi', 'gender_Male', 'gender_Other', 'stroke')
        return self.readonly_fields

admin.site.site_header = 'Prediction Database Administration'





@admin.register(ChronicKidneyPrediction)
class ChronicKidneyPredictionAdmin(ImportExportModelAdmin):
    list_display = ['Bp', 'Sg', 'Al', 'Su', 'Rbc', 'Bu', 'Sc', 'Sod', 'Pot', 'Hemo', 'Wbcc', 'Rbcc', 'Htn','prediction', 'prediction_message']
    search_fields = ['Bp', 'Sc', 'Pot']
    list_filter = ['Htn', 'Rbc', 'Su']
    ordering = ['prediction']


class DiabeticsPredictionAdmin(ImportExportModelAdmin):
    list_display = (
        'quality_assessment',
        'pre_screening',
        'ma_confidence_level_0_5',
        'ma_confidence_level_0_6',
        'ma_confidence_level_0_7',
        'ma_confidence_level_0_8',
        'ma_confidence_level_0_9',
        'ma_confidence_level_1_0',
        'exudates_confidence_level_0_5',
        'exudates_confidence_level_0_6',
        'exudates_confidence_level_0_7',
        'exudates_confidence_level_0_8',
        'exudates_confidence_level_0_9',
        'exudates_confidence_level_1_0',
        'exudates_normalized_by_roi_1',
        'exudates_normalized_by_roi_2',
        'macula_optic_disc_distance',
        'optic_disc_diameter',
        'am_fm_based_classification',
        'prediction',
        'prediction_message'
    )

admin.site.register(DiabeticsPrediction, DiabeticsPredictionAdmin)