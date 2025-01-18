# TESTING
## Table of Contents
1. Validation
2. Manual Testing
- [Global](#global-1)
    - [Navigation](#navigation)
        - [Navigation bar](#navigation-bar)
        - [Other links](#other-links)
        - 
- [Authentication](#authentication)




## Global 

### Navigation

#### Navigation Bar

| Feature | Action | Expected Result | Pass or Fail |
|---------|--------|-----------------|--------------------|
| Logo (with text) | click on logo | routes user to homepage (if not already there) | Pass |
| Home | click on "home" on navbar | routes user to homepage | Pass |
| About | click on "about" in navbar | routes user to About page | Pass |
| Contact Us | click on Contact Us navbar link | user is directed to about/contact_us url, which contains a form for sending a message | Pass |
| Login | user clicks on "login" on navbar | user brought to login page containing login form *(see also Authentication) | Pass |
| Register | user clicks on "register" | user is directed to accounts/signup url and presented with signup form | Pass |
| Logout | a logged in user clicks on Logout | user is brought to the logout page and the modal "are you sure" appears for confirmation | Pass |
| signout confirmation | user clicks Sign Out on confirmation modal | user is logged out | Pass |


#### Other links

| Feature | Action | Expected Result | Pass or Fail (P/F) |
|---------|--------|-----------------|--------------------|
| Homepage: Inline link to About page | click on link |sends the user to the About page | Pass |
| Homepage: Inline link to "message" | click on link | sends user to the Contact Us form | Pass |
| Homepage: Inline link to Volunteer page | click on link | sends user to the Volunteer page | Pass |
| Homepage: Back button from the above links | click on back button | redirected to Home page | Pass |
### Authentication

| Feature | Action | Expected Result | Pass or Fail |
|---------|--------|-----------------|--------------|
| User login | site visitor clicks on login on navbar | user is redirected to sign-in form at accounts/login url and is able to log in | Pass |
| User logout | logged in user clicks navlink to log out | user brought to logout page and asked if they are sure, then logged out if they click sign out button | Pass |
| User account | visitor clicks on Registration in the navbar | user is directed to the sign up page and can sign up | Pass |
| No log in by unregistered user | A user without an account clicks on login | Sign in fails and user is directed to Register first | Pass |
| Registration - part 2 | user clicks on the inline Register link at login page | user brought to accounts/signup url and presented with form where they can register | Pass |
| Prevent non logged in user from accessing the form where they can reserve a slot | user clicks on a beneficiary from the volunteer page | user is directed as usual to the beneficiary detail page but receives the message that they must be logged in to save a task to their dashboard and a link to do so | Pass |
| Student Dashboard access prevention for non-logged-in user | user types in the student_dashboard url | user is directed to the sign-in page | Pass |
| Privacy | -- | There is no way to access another person's dashboard, as all user-specific content is coded in templates and javascript, not via separate urls | Pass |
| Wrong password or username | A user types in the wrong password and username combination | A message appears stating that the username and/or password specified are incorrect | Pass |
| Forgotten password | User clicks on the forgotten password link | user directed to message form to send message for help, then redirected to home page | Pass |





## CRUD