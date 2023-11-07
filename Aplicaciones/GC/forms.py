from django import forms
from . models import Usuario, Curriculum

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellidos',
            'email',
            'contrasena',
            'rut',
            'fecha_nacimiento',
            'roles',
        ]

class LoginForm(forms.Form):
    nombre_usuario = forms.CharField(label='Nombre de Usuario')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = [
            'nombre',
            'correo_electronico',
            'area_trabajo',
            'telefono',
            'experiencia_laboral',
            'anios_experiencia',
            'educacion',
            'habilidades',
            'idiomas',
            'curriculum_adjunto',
        ]

#class CurriculumForm(forms.Form):
    #nombre = forms.CharField(label='Nombre', max_length=50, required=True)
    #correo_electronico = forms.EmailField(label='Correo Electrónico', required=True)
    #area_trabajo = forms.CharField(label='Área de Trabajo', max_length=50, required=True)
    #telefono = forms.CharField(label='Teléfono', max_length=15, required=True)
    #experiencia_laboral = forms.CharField(label='Experiencia Laboral', widget=forms.Textarea, required=True)
    #anos_experiencia = forms.IntegerField(label='Años de Experiencia', required=True)
    #educacion = forms.CharField(label='Educación', widget=forms.Textarea, required=True)
    #habilidades = forms.CharField(label='Habilidades', widget=forms.Textarea, required=True)
    #idiomas = forms.CharField(label='Idiomas', widget=forms.Textarea, required=True)
    #curriculum = forms.FileField(label='Adjuntar Currículum', required=True)

class CurriculumEditForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = [
            'nombre',
            'correo_electronico',
            'area_trabajo',
            'telefono',
            'experiencia_laboral',
            'anios_experiencia',
            'educacion',
            'habilidades',
            'idiomas',
            'curriculum_adjunto',
        ]