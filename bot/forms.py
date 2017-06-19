from django import forms
from .models import IA


class IAForm(forms.ModelForm):
	
	class Meta:
		model = IA
		fields = ('question','answer',)

	def __init__(self, *args, **kwargs):
		super(IAForm, self).__init__(*args, **kwargs)
		self.fields['question'].widget.attrs['class'] = 'form-control'
		self.fields['answer'].widget.attrs['class'] = 'form-control'
		self.fields['question'].widget.attrs['placeholder'] = 'Question'
		self.fields['answer'].widget.attrs['placeholder'] = 'Answer'
		self.fields['answer'].widget.attrs['required'] = 'required'
		self.fields['question'].widget.attrs['required'] = 'required'

		