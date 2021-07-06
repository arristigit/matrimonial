# from django import forms
# from django.db.models import fields
# from django.forms import widgets
# from .models import *

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields= '__all__'

#         widgets = {
#             'gender': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
#             'age': forms.TextInput(attrs={'class': 'form-control col-md-2'}),
#             'pic': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
#         }
#         # fields=('age', 'pic')
#         # fields=("id", "gender", "age", "pic", "phone", "date_of_birth", "city", "address", "father_name", "mother_name", "father_phone", "work_address", "occupation", "salary", "qualification", "hobby", "caste", "religion", "family_type")
#         # fields=("user", "gender", "age", "pic", "phone", "date_of_birth", "city", "address", "father_name", "mother_name", "father_phone", "work_address", "occupation", "salary", "qualification", "hobby", "caste", "religion", "family_type")

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('user','caption', 'image')

#         widgets = {
#             'user': forms.TextInput(attrs={'class': 'form-control'}),
#             'caption': forms.TextInput(attrs={'class': 'form-control, col-md-6', 'value': 'Enter image caption', 'disabled':"" }),
#             # 'image': forms.ImageField(widget=forms.ImageField(attrs={'class': 'col-md-6'})),
            
#             }