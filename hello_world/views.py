from django.shortcuts import render, redirect
from .models import GiftBox, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required



@login_required(login_url="/accounts/login/")
def giftbox_list(request):
    giftboxes = GiftBox.objects.all()
    return render(request, 'hello_world/giftbox_list.html', {'giftboxes': giftboxes})

def book_giftbox(request, giftbox_id):
    giftbox = GiftBox.objects.get(id=giftbox_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking and redirect to the booking confirmation page
            booking = form.save(commit=False)
            booking.giftbox = giftbox
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(initial={'giftbox': giftbox})

    return render(request, 'hello_world/book_giftbox.html', {'form': form, 'giftbox': giftbox})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'hello_world/booking_confirmation.html', {'booking': booking})


