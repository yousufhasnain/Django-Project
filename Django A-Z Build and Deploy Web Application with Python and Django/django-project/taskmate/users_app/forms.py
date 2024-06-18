from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
""" UserCreationForms --> CustomRegisterForm+E-mail Fields ---> CustomRegisterForms """

class CustomRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=250)
    last_name=forms.CharField(max_length=250)
    email=forms.EmailField(max_length=250)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
       
       
       

""" 
1.Create default forms that is UserCreationForm in views .
2.modify it using forms.py 
3.then import it from views.py and use it.



"""

""" 
use Crispy_forms
1.pip install django-crispy-forms
2.pip install crispy-boostrap5
3.add 'crispy_forms' in project setting installed app
4.load crispy_forms_tags in the templates html files
5.{{data|crispy}}

"""