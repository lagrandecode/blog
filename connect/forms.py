from django.forms import ModelForm
from connect.models import Question


class FormConnect(ModelForm):
    class Meta:
        model = Question
        fields = ['title','grade','cadre','address','age']

#Creating a form to add into the database         



