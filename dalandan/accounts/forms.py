from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserForm(forms.ModelForm):

    password2 = forms.CharField(widget=forms.PasswordInput,
                                label='Re-type Password')

    class Meta:
        model = User
        fields = (
            'username', 'password',
        )

    def clean_password2(self):
        """
        Make sure that the two password fields match.
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('The passwords did not match.')

        return password2

    def save(self, commit=True):
        """
        Make sure the raw password is hashed.
        """
        user = super().save(commit=False)

        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user
