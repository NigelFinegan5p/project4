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




### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home |![screenshot]() | Pass: No Errors |
| About |![screenshot]() | Pass: No Errors |
| Blog |![screenshot]() | Pass: No Errors |
| Hello |![screenshot]() | Pass: No Errors |
| Gifts |![screenshot]() | Pass: No Errors |
| Logout |![screenshot]() | Pass: No Errors |
| Book |![screenshot]() | Pass: No Errors |
| Confirmation |![screenshot]() | Pass: No Errors |



