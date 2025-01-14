from django.db import models

class GiftBox(models.Model):
    """
    A simple model with gift boxs available for booking.

    Attributes:
        name (str): The name of the gift box. It is chosen from 6 options.
        description (str): A description of the gift box.
        price (decimal): The price of the gift box, stored @ €19.99 in the database or /admin
        
    BOX_CHOICES (list of tuples): A predefined set of 6 gift box options ( 1 to 6 )
    
    Methods:
        __str__(): Returns the name of the gift box when the object is represented as a string.
    """

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
    """
    A simple booking model representing 6 options ( gift boxes 1 to 6).

    Attributes:
        giftbox (GiftBox): A foreign key linking to a GiftBox that is being booked.
        customer_name (str): The name of the customer making the booking.
        customer_email (str): The email address of the customer.
        date_booked (datetime): The date and time when the booking was created, recored and sent via email. 
        
    Methods:
        __str__(): Returns a string describing the booking, including the customer's name and the booked gift box.
    """

    giftbox = models.ForeignKey(GiftBox, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} booked {self.giftbox.name}"




