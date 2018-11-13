from django import forms
from django.core import validators
from first_app.models import User,UserProfileInfo
from django.contrib.auth.models import User


#custom validator. Can be defined in a field as a validators=[check_for_z]
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should start with a z!")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data= super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match!")

#creating a form from a model including all fields. exclude certain or include some is also possible
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# customer botcatcher
#    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

#    manuel bot kontrolu
#    def clean_botcatcher(self):
#        botcatcher = self.cleaned_data['botcatcher']
#        if len(botcatcher) > 0:
#            raise forms.ValidationError("GOTCHA BOT!")
#        return botcatcher
