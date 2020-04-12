from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from solver_app.models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 200, widget = forms.PasswordInput())

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        # Confirms that the two password fields match
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username/password")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name  = forms.CharField(max_length=20)
    email      = forms.CharField(max_length=50,
                                 widget = forms.EmailInput())
    username   = forms.CharField(max_length = 20)
    password   = forms.CharField(max_length = 200,
                                 label='Password',
                                 widget = forms.PasswordInput())
    confirm_password  = forms.CharField(max_length = 200,
                                 label='Confirm password',
                                 widget = forms.PasswordInput())


    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        # Confirms that the two password fields match
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username

# Note: no need to overide the clean method. The only thing being input is
#       text, which is adequately cleaned by the superclass's clean method
class CreatePostForm(forms.ModelForm):
    creation_time   = forms.DateTimeField(required=False)
    post_input_text = forms.CharField()
    class Meta:
        model = Post
        exclude = (
            'created_by',
            'creation_time',
        )

# Note: no need to overide the clean method. The only thing being input is
#       text, which is adequately cleaned by the superclass's clean method
class CreateCommentForm(forms.ModelForm):
    creation_time   = forms.DateTimeField(required=False)
    text            = forms.CharField()
    class Meta:
        model = Comment
        exclude = (
            'created_by',
            'creation_time',
            'response_to',
        )

MAX_UPLOAD_SIZE = 2500000

# TODO: Should probably validate some stuff here; also should maybe resize
#       image?
class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    bio_input_text  = forms.CharField(required=False, widget=forms.Textarea)
    class Meta:
        model = Profile
        exclude = (
            'user',
            'username',
            'following',
        )

    def clean_picture(self):
        picture = self.cleaned_data['profile_picture']
        if not picture:
            return None
        if not picture.content_type or not picture.content_type.startswith('image'):
            raise forms.ValidationError('File type is not image')
        if picture.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError('File too big (max size is {0} bytes)'.format(MAX_UPLOAD_SIZE))
        return picture