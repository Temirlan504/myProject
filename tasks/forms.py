from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)