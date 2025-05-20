from django import forms
from .models import Pagamento
from .models import Produto
from .models import Cliente

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['metodo']
        widgets = {
            'metodo': forms.Select(attrs={'class': 'form-select'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto 
        fields = ['nome', 'descricao', 'preco', 'estoque', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }