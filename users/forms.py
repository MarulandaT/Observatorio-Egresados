"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile
from users.models.profile import Subject

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder":"Nombre de Usuario"})
    )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={"placeholder":"Contraseña"})
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={"placeholder":"Confirmar Contraseña"})
    )

    first_name = forms.CharField(min_length=2, 
                                max_length=50, 
                                widget=forms.TextInput(attrs={"placeholder":"Nombre"})
                                )
    last_name = forms.CharField(min_length=2, 
                                max_length=50,
                                widget=forms.TextInput(attrs={"placeholder":"Apellido"})
                                )

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={"placeholder":"Correo"})
    )
    
    
   
    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()



class ProfileForm(forms.ModelForm):
    """Profile form."""
    class Meta :
        model = Profile
        exclude =  ('username','password','email','last_name','first_name', 'age','gender','dni_administrador','groups','city', 'authorized','type_user','user','confirmation_handling_sensitive_data')
    interests = forms.ModelMultipleChoiceField( label = 'intereses',      
        widget=forms.CheckboxSelectMultiple(),
        queryset=Subject.objects.all()
    )
    website = forms.URLField(label = 'Sitio Web',max_length=200, required=True)
    biography = forms.CharField(label = 'Biografia', max_length=500, required=False)
    phone_number = forms.CharField(label = 'Telefono',max_length=20, required=False)
    picture = forms.ImageField(label = 'Foto De Perfil',required=False)
