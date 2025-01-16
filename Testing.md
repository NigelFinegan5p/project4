## Strategic & Defensive Programming

Strategic & Defensive programming conducted manual testing as per the site structure below:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Navbar links | | | | |
| | Click on Gift Box Direct - Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Blog link in navbar | Redirection to Blog page | Pass | |
| | Click on Book & Subscribe link in navbar | Log in to Book & Subscribe, registered user only,  Django Decorator | Pass | |
| | Click on Gifts link in navbar | Redirection to Gifts page ( view 6 GBD boxes )| Pass | |
| | Click on Register link in navbar | Redirection to Accounts/Sign up page | Pass | |
| GBD Blog Page | | | | |
| | Click on post title | Redirection to that post details page | Pass | |
| | Click on Pagination nav number | Redirection to that pagination page | Pass | |
| | Click on Pagination right arrow | Redirection to next pagination page | Pass | |
| | Click on Pagination double right arrow | Redirection to last pagination page | Pass | |
| | Click on Pagination left arrow | Redirection to previous pagination page | Pass | |
| | Click on Pagination double left arrow | Redirection to first pagination page | Pass | |
| Register/Sign up | | | | |
| | Enter valid Username | Field will accept max letters 20 | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Redirects user to landing/homapge page | Pass |
| Log In | | | | |
| | Enter valid Username | Field will accept max letters 20 | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Logs out user, Redirects user to logout page | Pass |
| User Book & Subscribe | | | | |
| | Must be Logged in|  Please log in. If you have not created an account yet, then sign up first. | Pass | |
| | Enter valid Username & Password | Field will accept max letters 20 | Pass | |
| | Click any one of the 6 options ( book 1 to 6 ) - click ( BOOKING ) button | Redirect to booking Form | Pass | |
| | Enter details for booking - Customer name & Customer Email | Redirect to booking confimation Form | Pass | |
| | Click on Book Giftbox | Redirects to that booking confirmation page with email confirmation details | Pass | |
| Confirmation Details | | | | |
| | After confirmation email sent to user | Redirect to giftbox booking confirmation page | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Redirect to login page, redirect back after login | Pass | |
| New Comment on GBD Blog Post - Registered User | | | | |
| | Enter Post Comment Title | Submit button is required | Pass | |
| | Enter Post Comment Update | Edit button is required | Pass | |


<br>
<br>

<br>
<br>


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.homepage.jpg) | Pass: No Errors |
| About |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.about.jpg) | Pass: No Errors |
| Blog |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.blog.jpg) | Pass: No Errors |
| Hello |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.hello.jpg) | Pass: No Errors |
| Gifts |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.gifts.jpg) | Pass: No Errors |
| Logout |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.logout.jpg) | Pass: No Errors |
| Book |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.book1.jpg) | Pass: No Errors |
| Confirmation |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/w3c_validator/w3c.confirmation.jpg) | Pass: No Errors |


<br>
<br>

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home |![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/css_validator/css.validator.jpg) | Pass: No Errors |


<br>
<br>

<br>
<br>

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation About App

| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/about/about_app.admin.py.jpg) | Pass: No Errors |
| apps.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/about/about_app.apps.py.jpg) | Pass: No Errors |
| forms.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/about/about_app.forms.py.jpg) | Pass: No Errors |
| models.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/about/about_app.models.py.jpg) | Pass: No Errors |
| urls.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/about/about_app.urls.py.jpg) | Pass: No Errors |
| views.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/about/about_app.views.py.jpg) | Pass: No Errors |


<br>
<br>

#### Validation Blog App

| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/blog/blog_app.admin.py.jpg) | Pass: No Errors |
| apps.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/blog/blog_app.apps.py.jpg) | Pass: No Errors |
| forms.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/blog/blog_app.forms.py.jpg) | Pass: No Errors |
| models.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/blog/blog_app.models.py.jpg) | Pass: No Errors |
| urls.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/blog/blog_app.urls.py.jpg) | Pass: No Errors |
| views.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/blog/blog_app.views.py.jpg) | Pass: No Errors |


<br>
<br>

#### Validation Codestar  ( Project Folder )

| File | Screenshot | Notes |
| --- | --- | --- |
| settings.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/codestar/codestar_app.settings.py.jpg) | Pass: No Errors |
| urls.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/codestar/codestar_app.urls.py.jpg) | Pass: No Errors |
| wsgi.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/codestar/codestar_app.wsgi.py.jpg) | Pass: No Errors |



<br>
<br>


#### Validation Firstapp

| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/firstapp/firstapp_app.apps.py.jpg) | Pass: No Errors |
| urls.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/firstapp/firstapp_app.urls.py.jpg) | Pass: No Errors |


<br>
<br>



#### Validation Gifts App

| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/gifts/gifts_app.apps.py.jpg) | Pass: No Errors |
| urls.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/gifts/gifts_app.urls.py.jpg) | Pass: No Errors |
| views.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/gifts/gifts_app.views.py.jpg) | Pass: No Errors |


<br>
<br>

#### Validation Hello_world App

| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/hello_world/hello_world.admin.py.jpg) | Pass: No Errors |
| apps.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/hello_world/hello_world.apps.py.jpg) | Pass: No Errors |
| forms.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/hello_world/hello_world.forms.py.jpg) | Pass: No Errors |
| models.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/hello_world/hello_world.models.py.jpg) | Pass: No Errors |
| urls.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/hello_world/hello_world.urls.py.jpg) | Pass: No Errors |
| views.py | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/python_linter/hello_world/hello_world.views.py.jpg) | Pass: No Errors |


<br>
<br>



## Lighthouse Audit, Chrome Developer Tools

Tested my deployed Heroku project using the Lighthouse Audit tool to check for any major issues.

### Website App Templates - Desktop Testing
| Page | Screenshot | Notes |
| --- | --- | --- |
| Home |  ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/homepage.lighthouse.jpg) | performance suggestions |
| About | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/aboutpage.lighthouse.jpg) | performance suggestions |
| Blog | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/blog.lighthouse.jpg) | performance suggestions |
| Hello Book & Subscribe | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/hello.lighthouse.jpg) | performance suggestions |
| Gifts | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/gifts.lighthouse.jpg) | performance suggestions |
| Logout | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/logout.lighthouse.jpg) | performance suggestions |
| Book  | ![screenshot]() | performance suggestions |
| Confirmation | ![screenshot](https://github.com/NigelFinegan5p/project4/blob/main/xtra_documents/lighthouse/confirmation.lighthouse.jpg) | performance suggestions |

