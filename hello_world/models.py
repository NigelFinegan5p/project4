from django.db import models

class GiftBox(models.Model):
    # Define the six gift boxes
    BOX_CHOICES = [
        ('giftbox_1', 'Giftbox 1'),
        ('giftbox_2', 'Giftbox 2'),
        ('giftbox_3', 'Giftbox 3'),
        ('giftbox_4', 'Giftbox 4'),
        ('giftbox_5', 'Giftbox 5'),
        ('giftbox_6', 'Giftbox 6'),
    ]
    
    name = models.CharField(max_length=20, choices=BOX_CHOICES, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    giftbox = models.ForeignKey(GiftBox, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} booked {self.giftbox.name}"

