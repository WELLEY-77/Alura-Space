from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        max_length=100,
        label='Nome do login',
        required=True,
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: João Silva'
            }
        ),
    )

    senha = forms.CharField(
        max_length=70,
        label='Senha',
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha',
            }
        ),
    )

class CadastoForms(forms.Form):
    nome_cadastro = forms.CharField(
        max_length=100,
        required=True,
        label='Nome de Cadastro',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: João Silva'
            }
        )  
    )

    email = forms.EmailField(
        max_length=100,
        label='E-mail',
        required=True,
        widget= forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: joaosilva@xpto.com',
            }
        )
    )

    senha_1 = forms.CharField(
        max_length=70,
        label='Senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha',
            }
        )
    )

    senha_2 = forms.CharField(
        max_length=70,
        required=True,
        label='Confirme sua senha',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha novamente',
            }
        )
    )


def clean_nome_cadastro(self):
    nome = self.cleaned_data.get('nome_cadastro')

    if nome:
        nome = nome.strip()

        if ' ' in nome:
            raise forms.ValidationError('Espaços não são permitidos nesse campo')
        else:
            return nome
        

def clean_senha_2(self):
     senha_1 = self.cleaned_data.get('senha_1')
     senha_2 = self.cleaned_data.get('senha_2')

     if senha_1 and senha_1:
        if senha_1 != senha_2:
            raise forms.ValidationError('As senhas não são iguais')
        else:
            return senha_2
