from rest_framework_json_api import serializers
from .models import DoctorData, ExcelUpload,FrontDeskModel

class ExcelUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelUpload
        fields = ('__all__')

class FrontDeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontDeskModel
        fields = ('__all__')

class FrontDeskActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontDeskModel
        fields = ['id','active'] 

# class FrontDeskUpdatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FrontDeskModel
#         fields = ['id','active'] 

class DoctorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorData
        fields = ('__all__')

class CalenderSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(method_name='calenderview')
    date = serializers.SerializerMethodField(method_name='dates')
    def dates(self, dat:FrontDeskModel):
        date = dat.DOS
        return date
    class Meta:
        model =  FrontDeskModel
        fields = [
            'id','title','date','Doctor_name'
        ]
        
    def calenderview(self,model: FrontDeskModel):
        location = model.Location
        doctor = model.Doctor_name
        total_patient = FrontDeskModel.objects.count()
        patient_not_present = FrontDeskModel.objects.filter(active =False).count()
        patient_present = total_patient - patient_not_present
        return f'{location}-{doctor}-{patient_present}/{total_patient}'

class CalenderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontDeskModel
        fields = ("__all__")