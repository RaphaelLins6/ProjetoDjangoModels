from django import forms
from .models import Pagamento
from .models import Produto

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
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }