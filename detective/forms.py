from django import forms
from .models import Case


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ['title', 'description', 'location', 'difficulty']

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) < 5:
            raise forms.ValidationError(
                "Case title must be at least 5 characters long."
            )

        return title