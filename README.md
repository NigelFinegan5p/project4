
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

