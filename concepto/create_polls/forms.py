from django import forms
from create_polls.models import Poll, Answer


# class CreatePollForm(forms.ModelForm):
#     question = forms.CharField(max_length=500, help_text="Question")
#     option1 = forms.CharField(max_length=500, help_text="Option 1"))
#     option2=forms.CharField(max_length = 500, help_text = "Option 2"))
#     option3=forms.CharField(max_length=500, help_text="Option 3"))
#     option4=forms.CharField(max_length=500, help_text="Option 4"))

#     class Meta:
# Provide an association between the ModelForm and a model
#         model=Category
#         fields=('name',)
