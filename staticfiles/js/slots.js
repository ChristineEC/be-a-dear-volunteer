/* --------  Most credit for this code goes to Code Institute --*/
/* ----It has been adapted for my purposes --*/

const editButtons = document.getElementsByClassName("btn-edit");
const slotTask = document.getElementById("id_task");
const slotLocation = document.getElementById("id_task_location");
const slotDates = document.getElementById("id_dates");
const slotTimes = document.getElementById("id_times");
const slotCompleted = document.getElementById("id_completed");
const slotCreditMinutesRequested = document.getElementById
    ("id_credit_minutes_requested");
const slotForm = document.getElementById("slotForm");
const submitButton = document.getElementById("submitButton");

/* --------  Credit for this code goes to Code Institute --*/
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons =  document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        deleteConfirm.href = `delete_slot/${slotId}/`;
        deleteModal.show();
    });
}

/* --------  Most credit for this code goes to Code Institute --*/
/* ----It has been adapted for my purposes --*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        let slotTaskContent = document.getElementById
            (`task${slotId}`).innerText;
        slotTask.value = slotTaskContent;
        let slotLocationContent = document.getElementById
            (`task_location${slotId}`).innerText;
        slotLocation.value = slotLocationContent;
        let slotDatesContent = document.getElementById
            (`dates${slotId}`).innerText;
        slotDates.value = slotDatesContent;
        let slotTimesContent = document.getElementById
            (`times${slotId}`).innerText;
        slotTimes.value = slotTimesContent;
        let slotCompletedContent = document.getElementById
            (`completed${slotId}`).innerText;
        slotCompleted.value = slotCompletedContent;
        let slotCreditMinutesRequestedContent = document.getElementById
            (`credit_minutes_requested${slotId}`).innerText;
        slotCreditMinutesRequested.value = slotCreditMinutesRequestedContent;
        submitButton.innerText = "Update";
        slotForm.setAttribute("action", `edit_slot/${slotId}/`);
    });
}
