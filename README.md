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

:worried: The default images were not being loaded for the About, Profile or Beneficiary objects.
**Fix:** Change default to "placeholder", rather than "default.jpg" or "placeholderimage.jpg", then load the relevant placeholder images conditionally in the templates. :star2:

:worried: The Slot Form (from the beneficiary detail page) was not posting correctly to the database when a user tried to edit. Although it would populate with the two first fields, it would then create a new Slot object. The reason for the bug is that I wasn't (originally) displaying all of the attributes in the rendered html template, so the javascript could not pick up all of the relevant attributes to edit. This threw errors and did not allow the javascript to run to the end of the function (where it should then change the button from "Save to Dashboard" to "Update").
**Fix:** I decided to render all of the objects attributes in the template so that they could be picked up by the javascript for editing, allowing the js function to complete, and thus allowing successful editing of the object. I considered making some of the attributes "hidden" using CSS classes, but further research revealed that javascript would not pick up any such hidden attributes. On further consideration, I thought that showing all of the attributes actually improved user experience and furthered one purpose of the project, which was to have students be able to read about what others were doing. That is, there was no harm, but to the contrary, some benefit, in rendering all of the objects attributes in the templates. As an afterthought, if I had truly wanted to hide the objects' attributes in the rendered templates, I could have simply made them display in the same font color as the background. However, I seem to recall learning that that is not good practice. So my solution in that case would be to use a different method of enabling the editing of objects, such as by using an update form, as is done from the student dashboard page. In any case, at first my solution did not work, and I discovered that I had a number of typographical errors in my javascript (in `slots.js`). Many thanks to Code Institute Tutor support for helping me identify that typo! :star2:


:worried: Errors occurred in the terminal after writing new javascript, but the errors pointed to the older javascript that had been working fine up until that point. On the student dashboard page, for which the new javascript was written, the code would not run through to complete the function relevant for that page. Those errors indicated a problem with the bootstrap delete Modal, which is used on a different page for editing slots. And on that other page, where the javascript was being used to prepopulate the form to edit a slot, an error was being thrown which referenced the javascript for the dashboard. I did not notice that second fact at first, so I was thinking that perhaps there had been some update with bootstrap that I would need to take into consideration, as the error pointed not only to my js file, but to the bootstrap script as well. But as I discussed the issue with Holly at Code Institute Tutor Support, I discovered the fact about the other webpage displaying a related (but reverse) error, and at Holly's suggestion, 
**Fix:** I split the javascript into separate files, each targeting only the relevant page or pages. Problem solved! Thank you, Holly! :star2:

Default images are not loading.



## Credits

A million thanks to Kay at Code Institute for her encouragement and guidance during our weekly standups! It made the whole experience of developing this app a whole lot less daunting--and more fun! And just because this thanks is short, I really mean it when I say that her smiling face each week and her sharing of knowledge have really made this course for me.

Many, many thanks as well to my mentor, Juliia, who quickly pointed out, during our mid-project session, that a feature I was bent on including in my project would simply have to be put on the back burner until after the project submission and that I'd better focus on the must-haves to make the deadline. I was reluctant to take that advice at first, but she was absolutely right. There were a lot of details to take care of, and I would not have made the deadline if I'd not taken her advice. (She also gets credit for my contact form not allowing an empty name or message field. A small detail that I'd overlooked when creating the model, and which she said I could skip and mention here as a future improvement, but it was an easy fix, so it's done.) 

And of course, many thanks to Code Institute's Tutor Support. I wish I'd made more use of you, especially in the early to middle stages, because whenever I did you saved me a lot of time! After staring at my javascript for what seems like forever, it took one of you just a minute to see where I'd accidentally left out a "let" before a variable. I swear I read over that code a million times and just couldn't for the life of me find that one error. I've learned there's a fine line between using descriptive variables and making variables so long that it's hard to see mistakes in the code. What a difference a second pair of eyes makes.

For the view code for the beneficiary details page, I borrowed heavily from the Codestar walkthrough project, although it has been adapted to my purposes.

The pagination code on index.html is also heavily based on the Codestar project.


<a href="https://www.flaticon.com/free-icons/volunteerism" title="volunteerism icons">Volunteerism icons created by gravisio - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/user" title="user icons">User icons created by Freepik - Flaticon</a>

![Photo by Lisa Fotios: person-digging-on-soil-using-garden-shovel](https://www.pexels.com/photo/person-digging-on-soil-using-garden-shovel-1301856/)

![Photo by Inge Wallumrød:cat](https://www.pexels.com/photo/silver-tabby-cat-lying-on-brown-wooden-surface-126407/)
