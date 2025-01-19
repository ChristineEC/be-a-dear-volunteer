/* For calculation of student dashboard stats */
const minutesApproved = document.getElementsByClassName("credit_minutes_approved");
const totalMinutesApproved = document.getElementById("calculated-minutes");
const totalHoursApproved = document.getElementById("calculated-hours");
const remainingHours = document.getElementById("remaining-hours");
const plusRemainingMinutes = document.getElementById("plus-remaining-minutes");
/* delete modal has been adapted from Dode Institute's Blog walkthrough */
const deleteModalDashboard = new bootstrap.Modal(document.getElementById("deleteModalDashboard"));
const deleteBtns =  document.getElementsByClassName("btn-delete-task");
const deleteConfirmDashboard = document.getElementById("deleteConfirmDashboard");
/* end cred */


let minutes = [];
for (let i=0; i < minutesApproved.length; i++) {
        let innernum = (parseInt(minutesApproved[i].textContent));
        minutes.push(innernum);
}
let totalminutes = minutes.reduce((acc, curr) => (acc + curr), 0);
totalMinutesApproved.innerHTML = totalminutes;
let calculatedhours = (totalminutes/60).toFixed(2);
totalHoursApproved.innerHTML = calculatedhours;
let calculatedremaininghours = 30 - Math.floor(totalminutes/60);
remainingHours.innerHTML = calculatedremaininghours;
let calculatedremainingminutes = totalminutes % 60;
plusRemainingMinutes.innerHTML = calculatedremainingminutes;


/*-- Partial credit for this code goes to Code Institute --*/
/*-- It has been adapted for my purposes --*/
for (let button of deleteBtns) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("data-slot_id");
        deleteConfirmDashboard.href = `delete_task/${slotId}/`;
        deleteModalDashboard.show();
    });
}
