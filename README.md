# Be a Dear - Volunteer
A Django project utilizing Python, JavaScript, HTML, CSS, and PostgreSQL.

Links to the deployed app and the GitHub repository:

[Be a Dear app deployed on Heroku](https://be-a-dear-volunteer-10d02942fbed.herokuapp.com/)

[Be a Dear GitHub repository](https://github.com/ChristineEC/be-a-dear-volunteer)

## Table of Contents
- [Description](#description)
- [Purpose](#purpose)
- [Agile Methods](#agile-methods)
- [UX/IX](#uxix)
- [Wireframes](#wireframes)
- [Features](#features)
    - [General Overview](#general-overview)
    - [Home Page](#home-page)
    - [Header and Navigation Bar](#header-and-navigation-bar)
    - [Logged In Status](#logged-in-status)
    - [Viewing opportunties on the Volunteer page](#viewing-volunteer-opportunities-on-the-volunteer-page)
    - [See what others are doing](#see-what-others-are-doing)
    - [Student privacy](#student-privacy)
    - [Saving tasks to register and plan volunteer activities](#saving-tasks-to-register-and-plan-volunteer-activities)
    - [Full CRUD: Creating, reading, updating and deleting tasks](#full-crud-creating-reading-updating-and-deleting-tasks)
    - [Site admin control of what is displayed](#site-admin-control-of-what-is-displayed)
    - [Managing tasks from the dashboard (RUD)](#managing-tasks-from-the-dashboard-rud)
    - [Students can keep track of their progress](#students-can-keep-track-of-their-progress)
    - [Profiles and classrooms](#profiles-and-classrooms)
    - [Read about the project](#read-about-the-project)
    - [Sending messages](#sending-messages)
    - [User messages](#user-messages)
    - [Teachers' approval of credit for students](#teachers-approval-of-credit-for-students)
    - [Footer](#footer)
    - [Favicon](#favicon)
- [User Stories Summarized](#user-stories-summarized)
- [Data Models](#data-models)
- [Future enhancements](#future-enhancements)
- [Deployment](#deployment)


## Description
Be a Dear - Volunteer is a web-based application designed to allow high school students to plan and record their volunteer activities and to request credit toward their graduation requirement, which is typically 20 to 30 hours for high schools in California.

The application is designed to be managed by a student, administrator or teacher of a school, with teachers able to approve credit on the backend. Students are usually required to volunteer at public-facing organizations. The idea behind the project is to allow students to volunteer in non-traditional ways, such as by assisting a private individual in their community, such as an elderly, disabled, or injured neighbor. In addition to being able to volunteer for private citizens, students are allowed to volunteer for as little as five minutes at a time as part of the fictional project.
## Purpose
The purpose of the project is to allow high school students, who must volunteer 20 to 30 hours to meet graduation requirements in California, to volunteer in 
- non-traditional,
- more fun, 
- convenient, and
- personally meaningful ways;
- more locally and 
- for smaller increments of time.

Traditionally, students must volunteer for public-facing organizations, such as at a soup kitchen, food bank, animal shelter, or environmental group, in order to have their volunteer time approved for credit. In reality, many students never complete their hours but instead have their parents sign off on work never done. A quick Google search of the issue reveals that many, if not most, students consider the requirement just an additional hoop to jump through in order to graduate; many resent the requirement and gain little from their experiences, much less any motivation for future volunteerism. 

Secondly, the COVID-19 pandemic caused increased mental health issues among teenagers, so another purpose of the project is to 
- improve the mental health of students. 

It is well-known that when people help others, even in tiny doses, it increases their own happiness and self esteem.

Finally, college acceptance is extremely competitive in California, especially for the cheapest schools, the public universities, which are also the highest ranked in California. Colleges do look at the extracurricular activities of applicants, including their volunteer experiences, and they read college application essays as an important part of the screening process. 

It is hypothesized that students who volunteer by helping an elderly neighbor on a regular basis, for example, will have more to say about their experiences on a college application, potentially helping their chances of acceptance. One of the (actually) stated rationales behind having students volunteer is that they will gain experiences in the public sphere that can help them in future employment. While this may be the case (for a very small number of cases, I'd venture to guess, as many students work part time jobs anyway), it is my belief that experiences of real people and real problems in their communities would be of more benefit, especially when it comes to an awareness of society as a whole. While traditional volunteer experiences have much to offer, I think that the gulf between teenage volunteers and those helped is often too wide for the experience to give real personal meaning, especially to someone carrying out the work begrudgingly. Teenagers may simply have difficulty identifying with their beneficiaries when they are so far removed from them socially, and when they receive little personal feedback. It is thought that more regular experiences with people closer to them in the community, on a regular basis, could yield more meaningful experiences due to the immediacy and social intimacy of the personal relationships formed. The hope is that students, who can be quick to reject externally imposed notions of morality, will come to enjoy their encounters and will learn an important fact about being human: that a great reason for helping others is that it makes us feel good, too.
## Agile Methods
The project was developed using agile methods. User stories were used to define the requirements, and these were tracked as issues on a Kanban board as a project in GitHub connected to the Be a Dear project repository. Labels were used to distinguish the different user stories as, for example, "must have", "should have", and "won't do". In addition to columns for To Do, In Progress, Done, and Won't Do, I used a column for Styling in Progress, which I found extremely helpful, at the suggestion of my mentor.

The link to my Kanban board: ![Kanban](https://github.com/users/ChristineEC/projects/5/views/1)
## UX/IX
User experience and user interaction:

The design of the website is simple and straightforward. Future functionality, such as the ability of students to post about their experiences, share photos, etc., would likely merit enhanced design, but for the scope of this project, simplicity is key.

- Colors: The color scheme is simple and clean: black and white, with some light pink background in places which helps break up the page into easily recognizable sections while maintaining good contrast with the font color (universally black, except when white on a black background). The pink coordinates with the valentine candy heart image on the home page, all in line with the intentional corniness of the title. (One mustn't be too earnest with teenagers!)

- Fonts: The main font used is open-sans for easy readability and clean presentation. The exception is the use of Graduate in the navbar as a nod to the high school milieu, and the limited use of Cabin Sketch on the dashboard page, as it looks like a student's doodle on a notebook or like block letters written with chalk on a chalkboard. I also used Bootstrap's "display-1" through "display-6" classes, as I found them, with their narrow line width and increased size, to be a more effective means of communicating messages quickly and at a glance--that is, succinctly and without shouting, as with bold font.

- The website is fully responsive.
Large images are included throughout the file. Here are some images from ![Am I Responsive's responsiveness checker](https://ui.dev/amiresponsive):

![Responsive image 1](documentation/responsive1.png)

![Responsive image 2](documentation/responsive2.png)


- Quick, intuitive navigation: Students will want to quickly find what they are looking for and be able to navigate freely and intuitively from the different pages, being redirected to where they started out after completing a task in the app. For this reason, the site was developed so that students are able to read, edit and delete their tasks from two different places on the site. 
    - From the beneficiary detail page they can quickly add tasks to their dashboards without worrying about including all of the details. They can create, read, update and delete from there, without ever having to leave the page. 
    - This means they can quickly add a number of tasks related to the different beneficiaries to their dashboards for later updating as they wish. 
    - Later, from their dashboards, they can read, update and delete their tasks, filling in the details and requesting credit as they go. Editing or deleting from the dashboard returns the student to the dashboard, and editing or deleting from the beneficiary detail page keeps users on the beneficiary detail page.

- Easily visible, convenient links: Other links are also made convenient. Any visitor to the site can send a message by clicking on "Contact Us" in the navbar, by clicking on an inline link on the homepage, or by filling in the form on the About page. All users have access to the Home, About, and beneficiary details pages (accessed by clicking on a beneficiary). (Only logged in users can save tasks to a dashboard.)

- The navbar includes only those links that are relevant to the user. Non-logged-in users see Home, About, Contact Us, Register, and Log In. Logged in users see Home, About, Contact Us, Log Out, and My Dashboard. All visitors to the site see a message under the navigation items either telling them that they are logged in as ( their username) or that they are not logged in, as the case may be. The message is shown on all pages.

- Clear messages are displayed to users indicating the results of any action taken by them, such as successful creation, updating or deleting of slots, or alternatively, if they try to visit a page to which they don't have access by typing in the url. 404 messages are in place as well. Delete modals are used to warn users before they delete anything.

- Pagination is not used, as most students are expected to be accessing the site on their mobile phones, where infinite scroll is more convenient. If any enhancement were to be made in the future, it might be the ability to search for an organization by name or by first letter by clicking on letters of the alphabet, but this would only be useful if there were to be very many organizations, and this would not be expected to be the case. In any case, the current scope of the project does not merit this.

- Privacy: Privacy is maintained, as usernames and information about planned tasks, etc., are never shown (at least not by name) on the pages that are not strictly personal to the logged in user. (In a future version of the app, aliases could be displayed on public pages, based on the aliases users choose for their profile.)

- Crispy forms were used to style all forms, including the login, register, logout, contact, and CRUD operations.

- **An important change:** One important change that I made at a late stage in development, one that I think resulted in vast improvement in UX/UI, was that I moved the list of beneficiaries from the homepage to its own page, called Volunteer. Before that change, visitors to the home page had no clear idea of what the website was for, and the navbar, lacking the now prominent "Volunteer" didn't provide a lot of clues. Too much explanation on the home page would have been a turn off. Splitting the two pages up allowed me to introduce the project more gradually and more effectively, most broadly on the home page, and then more specifically on the Volunteer page. This avoided overwhelming the site visitor when they landed on the home page for the first time, while allowing them to quickly grasp the general idea. At the urging of my mentor, just days before submission of this project, I made the change and am so glad I did.

I recognize that there is vast room for improvement in the visual design of the site. I hope the ease of navigation and clear messaging make up for some of it!

## Wireframes

My earliest wireframe was created using ![Balsamiq](https://balsamiq.com/), but my free trial period ended before I was ready to use it here, so I am including a downloaded image of it here:

![Mobile wireframe](documentation/mobile-wireframe.png)

More extensive wireframes were done in Miro (below). The home page differs from the design, and a new page, Volunteer, was added to improve UX. See the section on [UX/IX](#uxix) for a discussion of the reasons behind that decision.

![Wireframe done in Miro](documentation/wireframe.jpg)


## Features
### General overview
The Be a Dear project as a whole contains three apps:
1. The Volunteer app: houses all front-end CRUD. 
    - Models: Beneficiary, Slot, Classroom 
        - Beneficiary and Slot, together with Django's allauth User model, provide full front-end CRUD
        - Classroom enables teachers to sort user profiles (see below) by Classroom in the admin panel.
    - Templates:
        - index.html "Home"
        - volunteer_opportunties.html "Volunteer"
        - beneficiary_detail.html **(full CRUD)** - slug
        - student_dashboard.html **(RUD)** "My Dashboard"
        - update_task.html (RUD) - Edit buttons on dashboard
    - Forms:
        - SlotForm (full CRUD in one template, RU in another)
2. The About app
    - Model: About
    - Form: CollaborateForm (embedded in about.html and freestanding in contact_form.html)
    - Templates:
        - about.html
        - contact_form.html
3. The Users app
    - Model: Profile
        - Linked to Django allauth Users model (OneToOne) and to Classroom model in the volunteer app.
    - Function: Teachers can sort by classroom in the admin panel; students can read what Classroom they are assigned to.
        - Although the Profile model provides only limited (back-end) functionality at the current stage of this project, it does allow for rapid development of future enhancements.

### Home page
The home page acts as a landing page, providing a brief but clear and comprehensive introduction to the purpose and general functionality of the website.


![Homepage - index.html](documentation/homepage.png)


### Header and Navigation Bar
The header consists of a simple logo and the name of the project, clickable to return the user to the homepage from any page.

![Header](header-and-nav.png)


The nav bar is fully responsive, appearing as text on wider screens and as a navbar "hamburger" icon on smaller screens


![navbar-medium](documentation/navbar-medium.png)


![navbar-mobile](documentation/navbar-mobile.png)


The content of the navbar changes depending on whether a user is logged in or out.


![nav-logged-in](documentation/nav-logged-in.png)


![nav-logged out](documentation/nav-logged-out.png)


Current page shows as bolded in the navbar


![nav-bolded](documentation/nav-bolded.png)


### Logged In Status
A user is told that they are logged in as `<username>` or that they are not logged in at the top of every page, just under the navbar.


![You are logged in as message](documentation/logged-in-as.png)


![You are not logged in message](documentation/not-logged-in-msg.png)


### Viewing volunteer opportunities on the Volunteer page
The Volunteer page consists of three sections
- A header that shows what the page is about and simultaneously promotes (or at least encourages!) student engagement with the project.


![Volunteer header](<documentation/volunteer header.png>)


- How it Works section
Explains what students can do and how they can do it, displaying prominent links to giving further visual overview of the site.


![How it works](documentation/how-it-works.png)


- List of beneficiaries
With obvious links begging to be clicked.


![Beneficiaries](documentation/beneficiaries.png)


### Saving tasks to register and plan volunteer activities
When the user clicks on a beneficiary on the volunteer page, they are directed to that beneficiary's detail page, which also contains a prominent form for saving a task related to that beneficiary to their dashboard.


![Animal shelter detail](documentation/animal-shelter.png)




![More animal shelter detail](documentation/animal-shelter-2.png)


### See what others are doing
On each beneficiary's detail page, students can see how many students have saved or completed tasks for that beneficiary, and what those tasks look like (if they are published!).


![What and how many](documentation/what-and-how-many.png)


### Student privacy
In the image above, note that users names are not displayed. A future feature would allow aliases to be displayed. The Profile model is already set up to do this. Students would be made aware that if they wished their activities to remain private, they could leave their alias as the default "Someone". Otherwise, their chosen alias would be displayed, and it would be up to them who they revealed their alias to. Teachers would be able to see on the back end, of course, as they would have access to all users and profiles.


### Full CRUD: Creating, reading, updating and deleting tasks
The form on each beneficiary's page allows users to create and update "tasks", known as slots on the back end.


![alt text](documentation/create-and-update.png)


On the same page, users see their own slots, with edit and delete buttons.


![edit and delete](documentation/edit-and-delete.png)


Clicking on edit prepopulates the form, and when the user clicks on Update, the object is saved in the database and immediately appears as edited on the same page (and in the dashboard, of course).


![prepopulate to update](documentation/prepopulate-and-update.png)


Clicking the update button results in the slot being updated and a success message showing.


![update success message](documentation/task-updated.png)


![update displayed](documentation/update-displayed.png)


Clicking on delete brings up a delete modal.


![Delete modal](documentation/delete-modal.png)


Successful deletion displays a message.


![Delete success](documentation/delete-success.png)


### Site admin control of what is displayed
When a user updates a task that has been published, the task reverts to unpublished.


![Before edit](documentation/before.png)


![After edit](documentation/after-edit.png)


### Managing tasks from the dashboard (RUD)
Part of the student dashboard is shown here. Students can read, update and delete tasks and be returned to the dashboard.
The tasks are color coded by status (planned, completed, credit requested, or credit granted). In case a student doesn't mark an assignment as complete but still asks for credit, that task will appear in a red row. (It doesn't have any material bearing on the time calculation anyway, so it's not something they actually need to fix. This was created as a catch all in case a task is not caught by the if/else statements used to create the differentiation by color. This could be the only logical case.) Future enhancements should eliminate this possibility.


![Tasks on the dashboard](documentation/dashboard-tasks.png)


Clicking on edit for a task brings the user to the update_task.html page. It was important that users be able to update tasks here and be redirected right back to the dashboard, rather than being directed to the page where they created the task. The user receives a success message (as shown above) after clicking the update button.


![Update task page](update-task-page.png)


Clicking on delete brings up the same modal as above and the user is provided with the same success message as for deleting from the beneficiary page.


### Students can keep track of their progress
Total minutes and hours volunteered, total required, and total remaining appear at the bottom of the students' dashboards.


![Total hours](documentation/stats.png)


### Profiles and Classrooms
User profiles are created on the back end, in a OneToOne relation to Django's allauth Users model. On the front end, anyone with a profile can see what classroom they've been assigned to. If they don't have a profile, they are informed that a profile has not been created yet but that they still enjoy full functionality on the site and they can message (with a link) to ask for one to be created. This was a good example of agile development. I made sure to make the crucial functionality independent of the profile model. Users enjoy full functionality regardless of whether they have a profile or not, and teachers can still update their credit approvals on the back end.


![profile front end](documentation/class-assignment.png)


On the back end, teachers can sort profiles by classroom to quickly get an overview of their students who have registered and have profiles. Classroom numbers were made the primary key of the classroom model for this purpose. Even if the project were expanded to multiple schools, the 10 character limit (Char field) on the attribute is sufficient to allow for distinguishing between schools and adding many, in case a district decided to implement, for example.


![profile back end](documentation/back-end-profile.png)


Profiles are incredibly easy to create for users because they appear inline with the User model on the back end, whether creating, viewing, or updating a user profile.


![User top half screen](documentation/user-first-half.png)


![User bottom half screen](documentation/user-second-half.png)


- **Future functionality:** Together, these two models could provide some interesting functionality, such as competitions between classes and between class years, and even between schools in a district.Teacher pages with the ability to grant credit on the front end would be possible, as well as the ability of users to upload profile pictures. In future development, profiles should be created automatically through signals when users register. As soon as a user creates an account, they would be directed to a form or a pop up asking for their profile information. At the very least, profiles should be created in the database through signals with the available default fields saved, and then users could edit their profiles quite easily via a form.


### Read about the project

On the home page and the about page, all site visitors can become acquainted with the project. Through the About model, the site admin can update the About page at will, saving drafts in the admin panel and publishing when desired. The most recently "published" About object is the one shown on the page.


![About](documentation/about.png)


### Sending messages
There is a form on the About page for sending messages to the site admin(s). Filling it in sends a message, which the site owner can mark as read to keep track of things, and the user is returned to the About page.
Links throughout the site bring users to contact_form.html page, where they can also send messages from. Filling out this form sends users to the homepage afterward, which is not ideal. Future enhancement would send them back to the page they came from.

### User Messages
Prominent messages are displayed to the user when they interact with the website:

Sign in success


![Sign in success](documentation/sign-in-success.png)


Sign out Are You Sure?


![Are you sure you want to sign out?](documentation/sure-sign-out.png)


Sign out success:


![Sign out success](documentation/sign-out-success.png)


Sent message (from all relevant links and pages):


![Thanks for your message!](documentation/message-thanks.png)


Wrong username and password or 
Not registered yet but trying to sign in


![Wrong or no credentials to sign in](documentation/wrong-creds.png)


Creation of a task from the Volunteer page


![Task created](documentation/slot-created.png)


![But not yet published](documentation/slot-not-published.png)


- and after publication:


![After publication](documentation/after-publication.png)


Task Updated!


![Update success](documentation/task-updated.png)


Deleting a task

- first the delete modal


![Delete modal](documentation/delete-modal.png)


- then delete success message


![Task deleted](documentation/task-deleted.png)


### Teachers' approval of credit for students
Teachers are identified as such on the back end by the superuser--both by labeling them as "staff" with Django's built-in User model and by changing their default profile type to "teacher". After being given the relevant privileges there, teachers are able to view their students' requested hours and approve them, either for the full amount requested or some other amount, as they deem creditable. (After all, high school students are known to exaggerate!)

### Footer
The footer is designed to be changed out by the particular school using the app. I have included two external links for good form, but schools will want to keep everything in-house, and would probably include links to the school's home page and such.


![Footer](documentation/footer.png)


### Favicon
The favicon, a simple heart, was obtained from ![Flaticon](https://www.flaticon.com/free-icons/free). A future improvement would be to use one with better contrast for people using dark mode.

## User Stories Summarized
A site visitor can 
- read about the project on the home page and on the about page
- can send messages from either page through a contact form.

A site visitor can log in and create an account to:
- read about volunteer opportunities
- read about what other students have signed up for
- see a count of how many students have saved and how many have completed tasks related to a specific beneficiary
- save opportunities (i.e., create "tasks" related to a beneficiary) to their dashboard
- create, read, update and delete tasks from the beneficiary detail page
- manage their tasks (read, update and delete) from their student dashboard
- request credit by updating the fields "completed" and "credit minutes requested" on the update form (or from the Volunteer page wherefrom they saved the tasks)
- quickly see (via color coding on the dashboard) which tasks are planned, or completed, or have credit minutes/hours requested, or have already received credit
- compare the amount of credit received with the amount they requested (in case they want to argue their case for more minutes of credit!)
- see how many hours and minutes of credit they have received in total
- see how many more minutes or hours they must complete toward graduate
- see whether they have been assigned to a classroom, and if not know what to do if they haven't
- send messages to the site owners to suggest the posting of new volunteer opportunties, or for help with a forgotten password
- log out

The superuser can:
- designate certain registered users as "staff" (from the is_staff attribute from Django's allauth), to allow them to access the admin panel
- designate those users as either teachers or school admins and give them restricted privileges in the admin panel
- assign classrooms to the teachers (or a default "unassigned" classroom 999 in the case of school admins)
- create a user profile for any user, inline in the admin panel, assigning classrooms to students and teachers, and uploading profile pictures for display on student dashboards
- Create, read, update and delete beneficiaries and tasks, as well as users and profiles
- create, read, update and delete text for the About page, including uploading images
- mark received messages as read in order to keep track of what has been done (or answered)
- add classrooms for the project (create, read, update and delete functionality for this)

A teacher can:
- log in as a regular user and enjoy full functionality as if they were a student
- get access to the admin panel, once approved by the superuser
- be given the ability to approve students' requests for credit (i.e., can update slots)
- approve either the amount requested or a different amount, as the fields for credit requested and credit approved are distinct
- read information about all beneficiaries, slots, homerooms, users, and profiles on the back end
- sort profiles by classroom to see a list of all students in a classroom that are registered
- check if a student has been assigned a homeroom
- send a message through the admin panel
- read messages in the admin panel

All users stories were tested extensively during manual testing. Please see [Manual Testing](#manual-testing) in the TESTING.md file.

## Data Models
The data models were described briefly above. Here is the ERD, created in DrawSQL. Please note that all fields descriptions were not available for use through the DrawSQL site (at least the free version). Image fields in the About, Profile, and Beneficiary models should indicate BLOB for type, rather than BigInt.

**Entity Relationship Diagram**


![Entity relationship diagram made in DrawSQL](https://drawsql.app/teams/self-729/diagrams/be-a-dear)



## Future enhancements

- Profiles auto created through signals and able to be updated on the front end

- Homeroom page counter showing total minutes of volunteer time completed and approved by the students in the class as a whole.

- Teachers' pages, where they can approve credit on the front end

- Downloadable signature Forms: Credit for volunteer work by high school students in the State of California, as a matter of fact and not merely by the design of this project, requires proof in the form of signatures and contact details of the beneficiary. (For this reason, students have traditionally been limited to volunteering for public-facing organizations or institutions.) Students will be able to download signature forms to provide a basis for teacher approval of their volunteer hours.

- Better handling (or preparation for handling) of images.


For validation results, please see [VALIDATION](#validation) in TESTING.md.

## Deployment

To deploy the project, one has to first ensure that all dependences are in requirements.txt. A Procfile needs to be created to tell Heroku that the project is to be deployed to the web. ecord the version of python in a separate .python-version file in the root directory so Heroku knows which version of python has been used. The final code is pushed to the project's GitHub repository, ensuring that Debug is first set to False and secret key and database url are hidden in an env.py file which is saved in gitignore so that it is not uploaded to GitHub. Log in to Heroku and create an app. Click on Config Vars from the Settings menu and include variables for Cloudinary (if used), the database url, in my case the postgresql url to my database, and a secret key (does not have to be the same on as used in the app; indeed, it is recommended that it be different). Click on Deploy in the menu, then click on Deploy Branch. Set Enable Automatic Deploys. 

## Credits
### Thanks
A million thanks to Kay at Code Institute for her encouragement and guidance during our weekly standups! It made the whole experience of developing this app a whole lot less daunting--and more fun! And just because this thanks is short, I really mean it when I say that her smiling face each week and her sharing of knowledge have really made this a positive experience, and I've learned a lot from her. Thanks, Kay!

And a million more thanks to my mentor, Juliia, who quickly pointed out, during our mid-project session, that a feature I was bent on including in my project would simply have to be put on the back burner until after the project submission and that I'd better focus on the must-haves to make the deadline. I was reluctant to take that advice at first, but she was absolutely right. There were a lot of details to take care of, and I would not have been able to finish in time if I'd not taken her advice. (She also gets credit for my contact form not allowing an empty name or message field. A small detail that I'd overlooked when creating the model, and which she said I could skip and mention here as a future improvement, but it was an easy fix, so it's done.) Finally, thanks for pushing me to improve the UX of the project. I am so glad I decided to add the extra page. Thank you!

And of course, many thanks to Code Institute's Tutor Support. I wish I'd made more use of them, especially in the early to middle stages, because whenever I did they saved me a lot of time! After staring at my javascript for what seems like forever, it took someone from tutor support just a minute to see where I'd accidentally left out a "let" before a variable. I swear I read over that code a million times and just couldn't for the life of me find that one error. I've learned there's a fine line between using descriptive variables and making variables so long that it's hard to see mistakes in the code. What a difference a second pair of eyes makes.

### Credit due
For the view code for the beneficiary details page, I borrowed heavily from the Codestar walkthrough project, although it has been adapted to my purposes. I also took the code for formatting django generated messages directly from a Code Institute video when I decided at the last minute that my own styling, while it made my messages stand out, left a lot to desire. (It was plain ugly.)

For images and icons:

The heart favicon from ![Flaticon](https://www.flaticon.com/free-icons/free)

![Photo by Lisa Fotios: person-digging-on-soil-using-garden-shovel](https://www.pexels.com/photo/person-digging-on-soil-using-garden-shovel-1301856/)

![Photo by Inge Wallumrød:cat](https://www.pexels.com/photo/silver-tabby-cat-lying-on-brown-wooden-surface-126407/)

![LinkedIn icon from FontAwesome](https://fontawesome.com)

![GitHub icon from FontAwesome](https://fontawesome.com)

![Balsamiq](https://balsamiq.com/) for my mobile wireframe.

![Miro](https://miro.com/) for the more extensive wireframes.

![Pixabay](https://pixabay.com/) for the hearts image in the homepage header.

![MadelineEmery through Pexels](https://www.pexels.com/) for the soup kitchen image.

![Matheus Bertelli through Pexels](https://www.pexels.com/) for the adopt-me(dog) image.