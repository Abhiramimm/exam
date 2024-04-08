from django import forms

class StudentForm(forms.Form):

    StudentName=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    CourseName=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    Fees=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

