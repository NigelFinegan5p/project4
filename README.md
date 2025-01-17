## Our custom model code & the how and why ?

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

## Tools & Technologies Used

| Page | Link | Notes |
| --- | --- | --- |
| HTML | [LINK](https://en.wikipedia.org/wiki/HTML) | used for the main site content |
| CSS | [LINK](https://en.wikipedia.org/wiki/CSS) | used for the main site content styling |
| CSS flexbox | [LINK](https://www.w3schools.com/css/css3_flexbox.asp) | used for the main site content |
| CSS grid | [LINK](https://www.w3schools.com/css/css_grid.asp) | enhanced responsive layout. |
| Javascript | [LINK](https://www.javascript.com) | used for user interaction on the site |
| Python | [LINK](https://www.python.org) | OOP back-end programming language |
| GitHub | [LINK](https://github.com) | online code storage, PAAS. |
| Bootstrap | [LINK](https://getbootstrap.com) | off teh shelf responsiveness and pre-built solutions |
| Django | [LINK](https://www.djangoproject.com) | Python framework for the site. |
| Heroku | [LINK](https://www.heroku.com) | hosting the deployed site |
| Cloudinary | [LINK](https://cloudinary.com) | online static file storage |
| Gunicorn | [LINK](https://gunicorn.org/) | A WSGI server |
| psycopg2 | [LINK](https://pypi.org/project/psycopg2/) | PostgreSQL database adapter |


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

## Testing

For all testing, please refer to the [TESTING.md](https://github.com/NigelFinegan5p/project4/blob/main/Testing.md) file.


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


### Acknowledgements

I would like to thank my Code Institute mentor, Spencer Barriball for all the meeetings, insights & insightfullnes, viking stories and Game of thrones anecdotes.

P.s spence the book recommedation of Antonio Melé author of the Django by Example programming book, has been most helpful and of great assistance. 

Thank you............................................................



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

