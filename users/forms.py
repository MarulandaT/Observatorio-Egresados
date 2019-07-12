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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, prueba con otro")
        return email

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile.interests.add(*self.cleaned_data.get('interests'))
        profile = Profile(user=user)

        profile.save()
        




class ProfileForm(forms.ModelForm):
    """Profile form."""
    class Meta :
        model = Profile
        exclude =  ('username','password','email','last_name','first_name', 'age','gender','website','groups','city', 'authorized','type_user','user','confirmation_handling_sensitive_data')
    interests = forms.ModelMultipleChoiceField( label = 'Intereses',      
        widget=forms.CheckboxSelectMultiple(),
        queryset=Subject.objects.all()
    )
    biography = forms.CharField(label = 'Biografia', max_length=500, required=False,  widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label = 'Telefono',max_length=20, required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    picture = forms.ImageField(label = 'Foto De Perfil',required=True)
    dni_administrador = forms.CharField(label = 'Cédula',max_length=20, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
