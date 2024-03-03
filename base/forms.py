from .models import UserMessage
from django.forms import ModelForm, TextInput

class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = ['user_name', 'user_email', 'text']