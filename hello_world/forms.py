from django import forms
from .models import Booking, GiftBox

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['giftbox', 'customer_name', 'customer_email']

    giftbox = forms.ModelChoiceField(queryset=GiftBox.objects.all(), empty_label="Select a Giftbox")
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()



