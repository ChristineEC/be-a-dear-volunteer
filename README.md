# Love your Neighbor = Love Yourself

## Description

## Purpose

## User Stories

## Features

### User Profiles

User profiles are created upon the creation of a user account using signals, and users can then update their profiles to add their homeroom number and upload a profile picture (which only shows on their own page).


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

![ERD]](drawSQL-image-export-2024-12-24-1.png)



## Bugs

The Slot Form is not posting to the database. For the time being, I am removing the date and time fields in slot sign-up, as these are not needed at this stage. The student is expected to add and edit these fields as the planned activities near or take place. One form will be used for adding the slot to a student's dashboard, where the student will then have access to a more complete form for filling in the details of the slot as their plans become more concrete or even after they have completed the activities.

The signal was not working to create a profile. Thanks to tutor support for helping me pinpoint the problem(s): I had unnecessarily imported the User model at the start of the apps.py file in the users app where I was importing users.signals in the AppConfig function below, and I kept getting an error in the terminal that my apps weren't loading, so although I strongly suspected the issue was with the apps.py file (after reading the django documentation), I wasn't able to see what was _causing_ the error being raised. I wasn't aware that unnecessarily importing a model somewhere could cause such havoc! Also, I had created my Profile model (OneToOne with User) with a field for "alias" set to unique, and I had overlooked the fact that upon _creation_, the field would need to be populated with _something_, rather than only upon update by the user as I had planned. The reason that the unique field in the model was a problem seems obvious to me now: the Create.object code called by the signal would need to populate the field with something, and Django would only populate a field with the same Null value if there were no default, but since the field was supposed to be unique, both criteria could not be met. I was essentially learning how to deal with a OneToOne model while coding, so my understanding evolved through the learning process. In any case, the field was actually unnecessary for my purposes in the end. Again, many thanks to Code Institute's tutor support for helping me understand the issue. My misunderstanding arose from the fact that I didn't have clear in my mind how the create_profile function (now renamed edit_profile!) was related to the Create.object.profile command being called by the signal sent by the user upon creation of the user account. Removing the field from the model had no drawbacks, as the purpose for which it was intended (student privacy together with student identification to teachers) could be maintained by what I chose to display on the front end.

The slot form on the beneficiary detail page does prepopulate the form with the fields of an object after clicking edit for that object, however, saving the form creates a new object instead of updating the object one is trying to edit. I first tried rewriting the function `edit_slot` in the view. My reasoning was that, even though the form used to edit or create the slot, lacking the field for beneficiary, would not allow a user to change the beneficiary of the task (which is a related model, and set upon creation of the task), by leaving beneficiary out of the original code in `edit_slot`, I was somehow causing the edit form to create a new slot each time. I had left out the beneficiary in the function because my reasoning was that I was passing the slot id into the function already, so that the beneficiary was already defined (and inaccessible in the form as well). In any case, revising the 'edit_slot` function did not work, although I decided it was still important to have the code regarding the beneficiary in the function, as I had done for the function to create a slot. Next step is to have a look at the javascript, as I note that the "Save to Dashboard" button does not change to "Update", as it should with proper running of the js code, so that is my clue that the problem lies there.

## Bugs Fixed





## Credits

For the view code for the beneficiary details page, which includes a form for signing up for slots, I have borrowed heavily from the Codestar walkthrough project, although it has been adapted to my purposes.
The pagination code on index.html is also heavily based on the Codestar project.