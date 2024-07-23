from django import forms

class MetodoPagoForm(forms.Form):
    METODOS_DE_PAGO = (
        ('efectivo', 'Efectivo'),
        ('mercadopago', 'MercadoPago'),
    )

    METODO_ENTEGRA = (
        ('takeaway', 'Take Away'),
        ('delivery', 'Delivery'),
    )

    metodo_pago = forms.ChoiceField(choices=METODOS_DE_PAGO, label='Método de Pago')
    direccion_entrega = forms.CharField(max_length=200, label='Dirección de Entrega', required=False)
    comentarios = forms.CharField(widget=forms.Textarea, label='Comentarios', required=False)
    metodo_entrega = forms.ChoiceField(choices=METODO_ENTEGRA, label='Método de entrega')