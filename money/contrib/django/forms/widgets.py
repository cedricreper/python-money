from django import forms


class CurrencySelectWidget(forms.MultiWidget):
    """
    Custom widget for entering a value and choosing a currency
    """

    def __init__(self, choices=None, attrs=None, exclude_currency_select=False):
        widgets = (
            forms.TextInput(attrs=attrs),
        )

        if not exclude_currency_select:
            widgets += (forms.Select(attrs=attrs, choices=choices),)

        super(CurrencySelectWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        try:
            return [value.amount, value.currency]
        except:
            return [None, None]
