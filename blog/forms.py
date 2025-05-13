from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['metodo']
        widgets = {
            'metodo': forms.Select(attrs={'class': 'form-select'}),
        }