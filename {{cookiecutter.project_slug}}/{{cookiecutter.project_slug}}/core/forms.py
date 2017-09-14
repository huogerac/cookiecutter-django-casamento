# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm

import floppyforms.__future__ as forms
from floppyforms.widgets import PasswordInput, TextInput


class LoginForm(AuthenticationForm, forms.Form):
    """
    Override the default authentication
    """
    message_incorrect_password = "email/username or password invalid."
    message_inactive = "This account is inactive."

    username = forms.CharField(max_length=76, 
                    widget=TextInput(attrs={'placeholder': 'Email or Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if '@' in username:
            UserModel = get_user_model()
            user_email = UserModel._default_manager.filter(email__iexact=username)
            if user_email:
                username = user_email[0].username

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if (self.user_cache is None):
                raise forms.ValidationError(self.message_incorrect_password)
            if not self.user_cache.is_active:
                raise forms.ValidationError(self.message_inactive)
        self.check_for_test_cookie()
        return self.cleaned_data
