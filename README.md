# Be a Dear - Volunteer
A Django project utilizing python, javascript, HTML, and CSS.

## Description
Be a Dear - Volunteer is a web-based application designed to allow high school students to plan and record their volunteer activities and to request credit for those toward their graduation requirement, which is typically 20 to 30 hours for high schools in California. 


Teachers are able to approve the hours on the back end, and students can see the status of their credit requests, as well as their total hours and to allow teachers to approve hours of service toward the graduation requirement,

The application Be a Dear as a whole contains three apps: the main app is Volunteer, which houses all of the front-end CRUD for the project. Beneficiaries and Slots are the main models, and it is with these that the user interacts to view volunteer opportunities (the various beneficiaries listed on the site), save those opportunities as "tasks" (called slots in the model and the code)

## Purpose
Traditionally, students must volunteer for public-facing organizations in order to have their volunteer time approved for credit. The Be a Dear site lists a number of potential beneficiaries and also includes the beneficiary categories of "Other" and "Individual" so that students can track volunteer time even for beneficiaries not explicitly listed on the site, and it encourages students to volunteer for individuals in their community in small time increments.

UX



##Wireframes

![Wireframes](https://miro.com/welcomeonboard/bmxvNXFhc3NBWW42QUNBM2dZNG5id2JUNmZpVjdTd2g4YlBXNXh3T21XTkhHaEFzYUpLeDB4Zkx4dmVPbEt4aXVOQ1NlYVUzWk5XcmFKdDdXdzZBbTY0N3VUb3RLSXRBVjJybllPbGlSZDc0aC9wcER1NFl5YThpTmdCNXRjUHQhZQ==?share_link_id=329771186676)

## User Stories
A site visitor can read about the project on the home page and on the about page, and they can send messages from either page through a contact form.

## Features







### User Profiles

Users can have profiles that consist of a profile picture, classroom to which they belong (relating to a separate classroom model), profile type (student, teacher, or school admin), and alias, which defaults to "Someone". The classroom attribute is the most important attribute of the model because it allows teachers to quickly identify on the back end which students they want to validate slots for. The superuser changes any teachers' profile type from the default student to "teacher" and then manually gives the teachers various permissions on the admin panel. When a teacher later accesses the admin panel, they can sort profiles by homeroom to view the students they are interested in.

At the moment, profiles are handled entirely on the back end. Thanks to being registered as inline with the user model in the users app admin.py file, profile creation is straightforward. When a new user is created in the admin panel, or when a previously added user is chosen to view, the fields for the Profile model appear as well, so the superuser can assign the correct profile attributes, such as homeroom, or a profile picture that differs from the default. See future enhancements for more about user profiles.



user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default='default-profile-pic.jpg')
    classroom = models.ForeignKey(Classroom, default="999", on_delete=models.SET_DEFAULT)
    profile_type = models.PositiveSmallIntegerField(choices=PROFILE_TYPE, default=0)
    alias = models.CharField(max_length=25, default="Someone")




### List of beneficiaries

Students can browse a list of beneficiaries with short descriptions and locations, with a link to read more about each and to add the beneficiary to their dashboard for planning their volunteer activities. The list includes the beneficiary categories "An Individual" and "Other Organization or Group" so that students can plan volunteer activities not included under an already listed beneficiary. Through the contact form on the About page, students can send suggestions for posting opportunities they know of so other students can become aware of them.

### Task creation

On the beneficiary details page, users can read more about volunteer opportunities involving a particular beneficiary, find contact information to investigate further, and can enter information concerning the task they plan to (or have already) performed for that beneficiary. Here, users fill in a short task description and task_location (as this might differ from beneficiary location), and optionally, the date.  

### Student dashboard

Here students can track, edit, update, or delete their planned activities ("slots"), which appear on their own pages under the rubriques Planning, Completed, Credit Requested (in terms of minutes), and Teacher Approved (in terms of minutes credited). They also see their total minutes credited.
Under the Teacher Approved rubrique are displayed both the minutes of credit requested by the student and the minutes of credit approved by the teacher, so that any discrepancies can be discussed by the teacher and student and then resolved, as teachers will not necessarily want to approve the same number of minutes requested by the student.

### Downloadable Signature Forms

Credit for volunteer work by high school students in the State of California, as a matter of fact and not merely by the design of this project, requires proof in the form of signatures and contact details of the beneficiary. (For this reason, students have traditionally been limited to volunteering for public-facing organizations or institutions.) Students will be able to download signature forms to provide a basis for teacher approval of their volunteer hours.

### Teacher approval in the admin panel

Teacher ability to approve their students' activities and hours and minutes for credit toward graduation on the backend. Teachers receive the is_staff attribute on the backend by the superuser and are given the ability to log in to the admin panel, where they can sort students by homeroom to make the approval process easy.

### Homeroom page counter
Showing total minutes of volunteer time completed and approved by the students in the class as a whole.




## Data Models

### Entity Relationship Diagram

![alt text](static/images/drawsql.png)

Please note that all fields descriptions were not available for use through the DrawSQL site (at least the free version). Image fields in the About, Profile, and Beneficiary models should indicate BLOB for type, rather than BigInt.

##Validation

Javascript files were run through JSHint and passed with no errors. No changes have been made to the js files after being passed through the linter, except to remove the coded out first line, visible in the images below, needed to run the linter for ES6.
![Results of JSHint for `slots.js` in the be_a_dear project directory](static/images/jshint-slotsjs.png)


![Results of JSHint for `dahsboard.js` in the volunteer app](static/images/jshint-dashboard.png)

## Bugs

The Slot Form (from the beneficiary detail page) was not posting to the database when a user tried to edit. I got it working by deleting some of the fields on the form to be shown on that page, just to see if I could pinpoint the problem more exactly. The form then worked fine, but reappeared when I included the other fields again. I considered leaving the offending fields off of the form for that page, as users are expected to manage their tasks mainly from their dashboards, but I knew it would be terrible UX to allow users to edit tasks for which they could not see all the details. After all, they might decide to edit or delete a task that, unbeknownst to them (from that page), had already received approved credit hours. I realized finally that the reason my javascript wasn't working was that I had not included all of the fields in the html for that page, so there was nothing in the rendered html for the javascript to get to prepopulate the form. It now seems so obvious to me, but at the time it was all pretty murky! When the time came to write my own javascript for the dashboard stats, rather than just modifying the script taught to us in the blog walkthrough (as was the case for the slots editing), I had a clear understanding of what i was doing.

It turns out that I had a number of typographical errors in my javascript (in `slots.js`).  


few fields in the model to make the app more user-friendly, and then the slot form on the beneficiary detail page was prepopulating the form with the fields of an object after clicking the edit button for that object, but saving the form created a new object instead of updating the object. I first tried rewriting the function `edit_slot` in the view. My reasoning was that, even though the form used to edit or create the slot, lacking the field for beneficiary, would not allow a user to change the beneficiary of the task (which is a related model, and set upon creation of the task), by leaving beneficiary out of the original code in `edit_slot`, I was somehow causing the edit form to create a new slot each time. I had left out the beneficiary in the function because my reasoning was that I was passing the slot id into the function already, so that the beneficiary was already defined (and inaccessible in the form as well). In any case, revising the 'edit_slot` function did not work, although I decided it was still important to have the code regarding the beneficiary in the function, as I had done for the function to create a slot. Next step is to have a look at the javascript, as I note that the "Save to Dashboard" button does not change to "Update", as it should with proper running of the js code, so that is a clue that the problem lies there. First, because I was getting a warning in my terminal about duplicate tables in my database potentially causing my program to not work properly, I took measures to clear the database of all data, remigrate and register the models, and create a new model to replace the one (which I hadn't implemented yet anyway) that was causing the warning. This did not solve the current bug. The javascript is throwing errors in the terminal, so I have been addressing them one by one. Earlier, the form couldn't populate because I wasn't displaying all the fields on the page that were included in the form. That has been fixed. The javascript also did not like if a field was empty, as it couldn't read a null value. I revised to models to include some default text for those fields, which had the added positive effect of letting users know what they could or should enter there (and that it was ok to fill those in with specific details later). After fixing some typos in the js file, I was able to get through the js function all the way to my console message of "The function has completed!" (not for the first time), but the behaviour of saving a new slot instead of updating the old one persisted. Then this same error showed in the console. The script seems to get hung up on similar lines in the function, but not always the same ones, with the following message:
`Uncaught TypeError: Cannot read properties of null (reading 'innerText')
    at HTMLButtonElement.<anonymous> (slots.js:24:109)`
Looking more closely at the html in the browser using dev tools, I can see that the values that javascript is supposed to be setting are not being done. That is, they show in the form on the screen, but the values shown in the html under "value" are not changing as they did before. When I had a simpler form with just the task and task location, this worked. Now no values in the form change when the edit button is clicked, even though the form displays the slot and any edits that are made. So I'm beginning to think there's a problem binding the data to the form, and I'll be taking another look at the view tomorrow.

## Bugs Fixed

Errors occurred in the terminal after writing new javascript, but the errors pointed to the older javascript that had been working fine up until that point. On the student dashboard page, for which the new javascript was written, the code would not run through to complete the function relevant for that page. Those errors indicated a problem with the bootstrap delete Modal, which is used on a different page for editing slots. And on that other page, where the javascript was being used to prepopulate the form to edit a slot, an error was being thrown which referenced the javascript for the dashboard. I did not notice that second fact at first, so I was thinking that perhaps there had been some update with bootstrap that I would need to take into consideration, as the error pointed not only to my js file, but to the bootstrap script as well. But as I discussed the issue with Holly at Code Institute Tutor Support, I discovered the fact about the other webpage displaying a related (but reverse) error, and at Holly's suggestion, I split the javascript into separate files, each targeting only the relevant page or pages. Problem solved! Thank you, Holly!





## Credits

A million thanks to Kay at Code Institute for her encouragement and guidance during our weekly standups! It made the whole experience of developing this app a whole lot less daunting--and more fun! And just because this thanks is short, I really mean it when I say that her smiling face each week and her sharing of knowledge have really made this course for me.

Many, many thanks as well to my mentor, Juliia, who quickly pointed out, during our mid-project session, that a feature I was bent on including in my project would simply have to be put on the back burner until after the project submission and that I'd better focus on the must-haves to make the deadline. I was reluctant to take that advice at first, but she was absolutely right. There were a lot of details to take care of, and I would not have made the deadline if I'd not taken her advice. (She also gets credit for my contact form not allowing an empty name or message field. A small detail that I'd overlooked when creating the model, and which she said I could skip and mention here as a future improvement, but it was an easy fix, so it's done.) 

And of course, many thanks to Code Institute's Tutor Support. I wish I'd made more use of you, especially in the early to middle stages, because whenever I did you saved me a lot of time! After staring at my javascript for what seems like forever, it took one of you just a minute to see where I'd accidentally left out a "let" before a variable. I swear I read over that code a million times and just couldn't for the life of me find that one error. I've learned there's a fine line between using descriptive variables and making variables so long that it's hard to see mistakes in the code. What a difference a second pair of eyes makes.

For the view code for the beneficiary details page, I borrowed heavily from the Codestar walkthrough project, although it has been adapted to my purposes.

The pagination code on index.html is also heavily based on the Codestar project.

Favicon: The favicon was obtained from flaticon.com at <a href="https://www.flaticon.com/free-icons/volunteerism" title="volunteerism icons">Volunteerism icons created by gravisio - Flaticon</a>

