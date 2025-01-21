![enter image description here](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/readme/homepage..jpg)
![enter image description here](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/readme/homepage2..jpg)



<br>
<br>

<br>
<br>

<br>
<br>

## Our Story & The Vision

**_The Customer UX & serving the market_**

We strongly believe in supporting local producers. Not all small producers get listed in large multnational retailers. Some of these brand and products operate in parrrell to the traditional retail model and offer some very premium experiences. Our aim is to bring some of these unknown and unrecognised names directly to the customer household.


**_The Inspiration_**

We strongly believed in supporting local producers. When I was young, I would work every Saturday in a local retail store and I always saw the same faces there, week in, week out. That store was more than the shop that sold customers their newspapers, eggs, and bread; it was their friend and confidant.

**_The Beginning_**  
The company started out in 2025, with some poetic licence required.

What was an idea for a gift service delivering local shopping needs evolved into an online gift delivery company, specializing in Irish gourmet hampers and alternative gifts, as well as a wide range of personalized and experience gifts. The real Price/Value propositon is bringing the new and upcoming premium brands to market via a DTC business model and allowing the unseen and heard brands to become household names. 

At Gift Box Direct, we're passionate about supporting the best premium suppliers. We have begun to nurture relationships with over 30 local businesses to ensure our hampers are brimming with only the finest gourmet foods and iconic premium brands & Irish treats.  
#shoplocal

**_When It Has To Be the GBD box_**

Our mission is to make gift-giving as convenient as possible, and this is at the heart of everything we intend to do, no matter what the occasion. The potential for success can be seen by delivering the best of premium suppliers, beautifully presented, coupled with superior customer service. Our streamlined gift boxes, User experience, Customer service, bears this out from the moment you hit the landing page on mobile or desktop.

Our dedicated team is ready and waiting to help you choose the perfect gift for loved ones and valued clients alike, so give us a call or drop us a line and we'll take care of the rest.


<br>
<br>

<br>
<br>

<br>
<br>



## UX User experience &  the customer

The vison for this project  was to create a simple, sleek, website with 6 gift box options which would be in stark contrast to the many cluttered websites with a multitude of options that the user will have undoubtedly come across. Relevant information on the product offering is presented in a concise, clean manner, allowing the user to navigate through the site functions in a linear, frictionless manner. 


<br>

## User Goals / Project Goals

***E-commerce 4p's***
<p>

The 4Ps of Ecommerce Marketing – Product, Price, Place, and Promotion – these first order principles of E-Marketing,  have been critical and insightful for providing guiding principles to unlocking unprecedented value added ideas for this project. By carefully strategizing these elements, we enhanced and elevated the original project idea to a brand, and stand out Price/Value position in the competitive world of online retail, gift boxing.  

<br>


***User Goals***

-   Discover the Gift Box Brand
-   Leave the site with a great brand experience
-   View the 6 strategic product options available
-   Access Anywhere
-  Engage with the brand on blog posts and allow the user to drop there ideas and feedback on blog posts or use the contact us form . 


<br>

***Project Goals***

-   Build a Functional Platform
- Meet CRUD Functionality 
- Align project with guidance material for grading
-   Implement User Authentication
-   Optimize Performance
-   Test and Debug
-   Deploy a Live Application
-   Ensure Accessibility 

I used Agile frameworks & hand drawn tools to organize and manage my project efficiently. GitHub was the main tool I used to implement this system.

<br>
<br>

<br>
<br>

<br>
<br>




### Colour Scheme, Colors & Color Palette Generator


The color scheme uses the following at project inception, due to the adaptive nature of the project this changed when needed and adapted accordingly:


![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/readme/homepage3%2C_enhanced.jpg)

<br>
<br>

<br>
<br>

<br>
<br>



## Our custom model code & the how and why ?

<br>
<br>

## Admin.py File

This admin.py file configures the Django Admin interface for two models: GiftBox and Booking. Let's break it down the lines into steps:

**1. First step, Importing Required Modules**

    from django.contrib import admin
    from .models import GiftBox, Booking

-   admin is imported from django.contrib to access Django's built-in admin interface.
-   GiftBox and Booking are imported from the models module, so you can define custom user purchase of 6 gift boxes for these models in the Django Admin interface.

**2. Clearly Defining Custom Admin Class for** **GiftBox**

    class GiftBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)

-   **GiftBoxAdmin** is a custom admin class that defines how the GiftBox model will be displayed in the Django Admin interface.
-   **list_display** specifies the fields to display in the list view of the model on the admin page. In this case, it will show the name, description, and price of the gift box, in this case €19.99
-   **search_fields** defines the fields that can be searched. Here, it allows the admin to search for name and description.
-   **list_filter** adds a filter option on the right sidebar. It allows the admin to filter the list by the name of the gift box.
-   **ordering** specifies the default ordering of the objects in the admin interface. In this case, the list will be ordered alphabetically by name.

**3. Defining Custom Admin Class for** **Booking**

    class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'giftbox', 'customer_email', 'date_booked')  # noqa: E501
    search_fields = ('customer_name', 'customer_email')
    list_filter = ('giftbox', 'date_booked')
    ordering = ('-date_booked',)

-   **BookingAdmin** is another custom admin class, this time for the Booking model.
-   **list_display** lists the fields to be shown in the admin list view. Here, it displays the customer_name, the associated giftbox, customer_email, and the date_booked.
-   **search_fields** specifies the fields that are searchable in the admin interface. Admin users can search by customer_name or customer_email.
-   **list_filter** adds filters in the sidebar. In this case, it enables filtering by giftbox and date_booked. (i.e most recent to oldest.)
-   **ordering** determines how the objects are ordered in the list view. The -date_booked means that bookings will be displayed in descending order based on when they were booked (newest first).

**4. Registering the Models**

    admin.site.register(GiftBox, GiftBoxAdmin)
    admin.site.register(Booking, BookingAdmin)

-   These lines register the GiftBox and Booking models with the custom admin classes defined earlier (GiftBoxAdmin and BookingAdmin). This allows the Django Admin to use these custom configurations when displaying the models.

**Conclusion**

This admin.py file is configuring the Django Admin interface for two models, GiftBox and Booking, with custom admin views to display certain fields, allow searching, filtering, and ordering. It enhances the usability of the Django Admin for managing these 2 custom models.

<br>
<br>

<br>
<br>

<br>
<br>


## Forms.py File

The forms.py file defines a Django form that is used for handling the creation or update of Booking objects. Here's a breakdown of the code in the forms.py file:

**Imports:**

    from django import forms
    from .models import Booking, GiftBox

-   **from django import forms**: This imports Django's forms module, which contains various classes and methods for creating forms. It’s essential for handling user input and validation in Django applications.
-   **from .models import Booking, GiftBox**: This imports the Booking and GiftBox models from the current module ( in this case from the models.py file), which are the custom models this form will be interacting with.

**The** **BookingForm** **class:**

    class BookingForm(forms.ModelForm):
	    class Meta:
	    model = Booking
	    fields = ['giftbox', 'customer_name', 'customer_email']
	    
	    giftbox = forms.ModelChoiceField(queryset=GiftBox.objects.all(), empty_label="Select a Giftbox")
	    customer_name = forms.CharField(max_length=100)
	    customer_email = forms.EmailField()


This form is a **ModelForm**, which means it's directly tied to a Django model. The form will automatically generate fields based on the model's attributes and handle the validation and saving of data for the Booking model.

**class BookingForm(forms.ModelForm):**

-   This creates a subclass of forms.ModelForm, allowing the form to work with the Booking model.

**class Meta:**

-   The **Meta class** is used to configure the form's settings, particularly which model it is tied to and which fields should be included in the form.

**model = Booking**

-   This specifies that the form is tied to the Booking model. So, the form will be used to create or edit instances of this model, in this case the below fields.

**fields = ['giftbox', 'customer_name', 'customer_email']**

-   This indicates that the form will include the following fields for user input:

-   giftbox: A reference to a GiftBox object. ( giftboxes 1 to 6 for the user to choose from )
-   customer_name: A text field to capture the customer's name.
-   customer_email: A text field to capture the customer's email address.


**Conclusion:**

The BookingForm is a Django form that allows users to create or update Booking objects. It has the following three fields:

-   A dropdown to select a GiftBox, numbered 1 to 6
-   A text field for the customer's name, and
-   A field for the customer's email address.

The form uses a ModelForm to handle the conversion of user input into model instances for saving to the database. One the user inputs the 3 fields the data is sent to the Django database and retrieved form there by /admin and logging in as a Super User. 

<br>
<br>

<br>
<br>

<br>
<br>


## Urls.py File

The urls.py file. So what really happens in urls.py?
Like reading a map before exploring a terrain A URL pattern is defined as a regular expression that matches a URL. When a user requests a URL, Django goes through the list of URL patterns defined in the urls.py file and finds the first pattern that matches the URL. If no pattern matches, Django returns a 404 error.

The urls.py file contains the follwing code:

    from django.urls import path
    from . import views
        
          
     urlpatterns = [
        path('', views.giftbox_list, name='giftbox_list'),
        path('book/<int:giftbox_id>/', views.book_giftbox, name='book_giftbox'),
        path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'), 
        ]


1.  **Imports**:

`from django.urls import path` <p></p>
`from . import view`

-   path is imported from django.urls to define URL patterns.
-   views is imported to reference the view functions that handle HTTP requests and return responses.

2.  **URL Patterns**:

-   urlpatterns: This is a list that defines the URL patterns for the application.

Each path() function call represents a specific URL pattern and maps it to a view function.

`path('', views.giftbox_list, name='giftbox_list'):`

-   The empty string '' matches the root URL of this section of the site.
-   When this URL is accessed, it calls the giftbox_list function in views.py to handle the request.
-   The URL is named hello from the app set up with the HTML file named 'giftbox_list', 


`path('book/<int:giftbox_id>/', views.book_giftbox, name='book_giftbox'):`

-   This pattern will match URLs of the form book/<giftbox_id>, where <giftbox_id> is an integer passed as a parameter.
-   The value of <giftbox_id> will be passed to the book_giftbox view function.
-   The booking from the end user occurs when they are presented with a drop down box of 6 options.


<br>
<br>

<br>
<br>

<br>
<br>

## Views.py File

<br>

***Introduction***

In the model view controller (MVC) architecture, the view component deals with how data is presented to users for consumption and viewing. In the Django framework,  [views](https://docs.djangoproject.com/en/3.1/topics/http/views/)  are Python functions or classes that receive a web request and return a web response. Additionally we are noting the clear distinction and delineation between function, class and template based views. 

The response can be a simple HTTP response, an HTML template response, or an HTTP redirect response that redirects a user to another page. Views hold the logic that is required to return information as a response in whatever form to the user. As a matter of best practice, the logic that deals with views is held in the  **views.py**  file in a Django app.


### 1. **Imports**:

    from django.shortcuts import render, redirect
    from .models import GiftBox, Booking
    from .forms import BookingForm
    from django.contrib.auth.decorators import login_required



-   `render` and `redirect`: These are Django shortcuts for rendering templates and redirecting users to different views respectively.
-   `GiftBox` and `Booking`: These are models from your Django application/ database that represent the database tables.
-   `BookingForm`: This is a form of class that handles the user input for booking a giftbox, and its realationship with and to forms.py
-   `login_required`: A decorator that ensures a user must be logged in to access certain views.

<br>
<br>


### 2. **Giftbox List View** (`giftbox_list`):


```
@login_required(login_url="/accounts/login/")
def giftbox_list(request):
    giftboxes = GiftBox.objects.all()
    return render(request, 'hello_world/giftbox_list.html', {'giftboxes': giftboxes})
```


  **Decorator**: 
- `@login_required` ensures that only logged-in users can view this page. If a user is not logged in, they will be redirected to `/accounts/login/`. Instruction provided by [Django decorators](https://docs.djangoproject.com/en/5.1/topics/http/decorators/).

**Logic**:

  -   This view retrieves all `GiftBox` objects from the database using `GiftBox.objects.all()`.
  -   The `render()` function returns an HTML page (`giftbox_list.html`), passing the `giftboxes` data as context to the
   template. The data is giftbox 1 to giftbox 6. 


<br>


### 3. **Book Giftbox View** (`book_giftbox`):


```
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
```

-   **Fetch Giftbox**: The giftbox being booked is fetched using `giftbox_id` passed from the URL (e.g., `/book/<giftbox_id>/`).
-   **POST Request**: If the form is submitted (`POST` method), a `BookingForm` is instantiated with the request data (`request.POST`). If the form is valid:
    -   A new booking instance is created using `form.save(commit=False)`, which means the form data is processed but not saved to the database yet.
    -   The `giftbox` is associated with the booking (this step links the booking to the specific giftbox).
    -   The booking is saved to the database with `booking.save()`.
    -   After successful booking, the user is redirected to the booking confirmation page using `redirect('booking_confirmation', booking_id=booking.id)`, passing the `booking_id` to the confirmation view.
    - To access the saved booking data i manually tested this 5 times and the order is saved to the database with a corresponding order number


<br>

### 4. **Booking Confirmation View** (`booking_confirmation`):

-   **Fetch Booking**: The booking is retrieved by its `id` from the URL (e.g., `/confirmation/<booking_id>/`).
-   **Render Confirmation**: The `booking` object is passed as context to the `booking_confirmation.html` template to show the details of the booking.

```
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'hello_world/booking_confirmation.html', {'booking': booking})
```

<br>


### 5. **Django decorator** 

In order to ensure that logged in users only can order from the Book & Subscribe page on GBD we added in the following from the Django Library.

Using this approach requires that the [`login_required()`](https://docs.djangoproject.com/en/5.1/topics/auth/default/#django.contrib.auth.decorators.login_required "django.contrib.auth.decorators.login_required") also takes an optional `login_url` parameter. 

Example:

```
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def my_view(request): ...
```


<br>
<br>

<br>
<br>

<br>
<br>

## Models.py File

This `models.py` file defines two Django models: `GiftBox` and `Booking`. Here's an an overview of the Models.py file for the custom booking system.

```
from django.db import models


class GiftBox(models.Model):
 
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

```



<br>
<br>

### **GiftBox Model**

#### **Gift Boxes 1 to 6 :**

-   **`BOX_CHOICES`**: This is a predefined list of tuples used in the `name` field of the `GiftBox` model. Each tuple contains a value and a display name. The `choices` attribute ensures that only one of the options from this list can be selected when creating or updating a `GiftBox`.




This model represents a "gift box" that can be booked with 6 options. 

#### **Attributes:**

-   **`name`**: A `CharField` with a maximum length of 20 characters. The `choices` attribute ensures that the value can only be one of the six predefined options (Giftbox 1 to Giftbox 6). The `unique=True` constraint ensures that no two `GiftBox` records can have the same name.
    
-   **`description`**: A `TextField` that stores a longer description of the gift box. This is typically used to provide more information about the box's contents or its intended use.
    
-   **`price`**: A `DecimalField` that stores the price of the gift box, with a maximum of 6 digits, of which 2 digits can be after the decimal point (e.g., 19.99).
    

#### **Methods:**

-   **`__str__()`**: This method is overridden to return the `name` of the gift box when the object is represented as a string. This is particularly useful for displaying the name in Django admin or when querying the database.



<br>
<br>

### **Booking Model**

This model represents a booking of a `GiftBox` made by a customer.

#### **Attributes:**

-   **`giftbox`**: A `ForeignKey` field that links this `Booking` to a specific `GiftBox` from the `GiftBox` model. The `on_delete=models.CASCADE` argument means that if a `GiftBox` is deleted, all related `Booking` instances will also be deleted automatically.
    
-   **`customer_name`**: A `CharField` that stores the name of the customer who made the booking.
    
-   **`customer_email`**: An `EmailField` that stores the email address of the customer.
    
-   **`date_booked`**: A `DateTimeField` that automatically stores the date and time when the booking was created. The `auto_now_add=True` argument ensures that this field is set to the current date and time when a new `Booking` instance is created.
    
<br>


#### **Methods:**

-   **`__str__()`**: This method returns a string that describes the booking, including the customer’s name and the name of the booked gift box. This is used when displaying the booking in Django admin or in query results.


<br>
<br>


## Troubleshooting & Looping through

When i build the booking & subscrition model and refreshed the browser it did not work.
So to clearly define and articulate what i mean by this the HTML file giftbox_list.html file was only showing the `<h1>` heading on the page. 

As a way to test whether or not what i had written needed adaption a approached it this way.

 1. in the URL use /admin
 2. login into the admin panel
 3. check of the migrations from the CLI that were displaying ok had been back end administered
 4. the admin panel showed they had and therefore the next step was that the database & display was to be tested
 5. i wrote a qurey set in line 5 of the giftbox_list.html file
 6. Using the following code i wrote {{ hello world }}
 7. I then refreshed the browser and the page displayed `<QUERYSET>`
 8. Able to ascertain that the database was looping through by the `<QUERYSET>` the next step was add data to the empty database.
 9. I added the giftbox options and price when logged into /admin
 10. After a refresh of the browser  the display otions appeared after the back end inputs.

Thats how i troubled shooted and tested the LOOP that i built. 
All that was left to do was input the the final HTML for page structure with appropriate bootstrap for responsive design.



<br>
<br>

<br>
<br>

<br>
<br>



## Bug fixing & Unfixed Bugs

There are no remaining bugs that I am aware of after extensive manual testing.

The home page / landing page had an overflow which was affecting all the sizing on the page in various mobile sizes. 

Having spoke to tutor suport on this and the approah to take was to install the following chrome extension, Unicorn Revealer by dehlin.dev 5.0 withe the following (20 ratings) from other users.

**Unicorn revealer**

The extension excerpts below:
Overview
Do you have overflow on your website and want to try find it. Sparkle some 🦄 on your website and find where it is.

As a web developer it can be hard to inspect and find out where overlow is located. You can sprinke some 🦄 on the website and it will turn all black and pink, this will show the borders and make it easier to debug. It is as simple as right click a website Sparkle it on once done right click and remove the sparkle.

**The fix**

Using this chrome extension I were able to locate the issue in a hr tag, the Horizontal Rule tag and the solution was to add width 300px to the hr tag, therefore solving the issue and allowing full mobile responsiveness without the border overruns which were occuring. 

Before implementing a final solution to this I tested 200px. 250px, 300px, 350px and 400px. 

Thanks to Thomas Wharton - Learning Success Tutor - Code Institute... 

<br>
<br>

<br>
<br>

<br>
<br>

## Tools & Technologies Used

| Page | Link | Notes |
| --- | --- | --- |
| HTML | [LINK](https://en.wikipedia.org/wiki/HTML) | Used for the main site content |
| CSS | [LINK](https://en.wikipedia.org/wiki/CSS) | Used for the main site content styling |
| CSS flexbox | [LINK](https://www.w3schools.com/css/css3_flexbox.asp) | Used for the main site content |
| CSS grid | [LINK](https://www.w3schools.com/css/css_grid.asp) | Enhanced responsive layout. |
| Javascript | [LINK](https://www.javascript.com) | Used for user interaction on the site |
| Python | [LINK](https://www.python.org) | OOP back-end programming language |
| GitHub | [LINK](https://github.com) | Online code storage, PAAS. |
| Bootstrap | [LINK](https://getbootstrap.com) | Off teh shelf responsiveness and pre-built solutions |
| Django | [LINK](https://www.djangoproject.com) | Python framework for the site. |
| Heroku | [LINK](https://www.heroku.com) | Hosting the deployed site |
| Cloudinary | [LINK](https://cloudinary.com) | Online static file storage |
| Gunicorn | [LINK](https://gunicorn.org/) | A WSGI server |
| Psycopg2 | [LINK](https://pypi.org/project/psycopg2/) | PostgreSQL database adapter |


<br>
<br>

<br>
<br>

<br>
<br>

### MoSCoW Prioritization

I applied the MoSCow prioritization and labels to my user stories within GitHub platform.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

<br>
<br>

<br>
<br>

<br>
<br>

## Testing

For all testing, please refer to the [TESTING.md](https://github.com/NigelFinegan5p/project4/blob/main/Testing.md) file.


<br>
<br>

<br>
<br>

<br>
<br>

### Images & Media Sources 


| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pixabay](https://pixabay.com/) | Landing pape | image | Main image |
| [Pixabay](https://pixabay.com/) | Blog posts | image | Wrapped present
| [Pixabay](https://pixabay.com/) | About page| image | Present


<br>
<br>

<br>
<br>

<br>
<br>


### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after the initial account setup & creation:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

<br>
<br>

<br>
<br>

<br>
<br>


### Acknowledgements

I would like to thank my Code Institute mentor, Spencer Barriball for all the meeetings, insights & insightfullnes, viking stories and Game of thrones anecdotes.

P.s spence the book recommedation of Antonio Melé author of the Django by Example programming book, has been most helpful and of great assistance. 

Thank you............................................................



<br>
<br>

<br>
<br>

<br>
<br>

## Bibliography & Sources

Django 5 By Example book, Antonio Melé (5th & 6th Edition), available for free download.

https://djangobyexample.com/


IMPRACTICAL PYTHON PROJECTS, Author Lee Vaughan

[https://www.kea.nu/files/textbooks/humblelearn2code/impracticalpythonprojects.pdf](https://www.kea.nu/files/textbooks/humblelearn2code/impracticalpythonprojects.pdf)


Python Distilled (Developers Library) (1st Edition) (David Beazley)

[https://www.scribd.com/document/764971811/Python-Distilled-Developers-Library-1st-Edition-David-Beazley](https://www.scribd.com/document/764971811/Python-Distilled-Developers-Library-1st-Edition-David-Beazley)

Python for Dummies by Aahz Maruch and Stef Maruch

[https://www.vailtech.net/sites/default/files/Python_Essentials_for_Dummies.pdf](https://www.vailtech.net/sites/default/files/Python_Essentials_for_Dummies.pdf)

