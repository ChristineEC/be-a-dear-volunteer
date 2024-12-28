const editButtons = document.getElementsByClassName("btn-edit");
const slotTask = document.getElementById("id_task");
const slotLocation = document.getElementById("id_task_location");
const slotDate = document.getElementById("id_date");
const slotStartTime = document.getElementById("id_start_time");
const slotEndTime = document.getElementById("id_end_time");
const slotCompleted = document.getElementById("id_completed");
const slotCreditMinutesRequested = document.getElementById("id_credit_minutes_requested");
const slotCreditMinutesApproved = document.getElementById("id_credit_minutes_approved");
const slotForm = document.getElementById("slotForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        let slotTask = document.getElementById(`${id_task}`).innerText;
        slotTask.value = slotTask;
        let slotTaskLocation = document.getElementById(`${id_task_location}`).innerText;
        slotTaskLocation.value = slotTaskLocation;
        let slotDate = document.getElementById(`${id_date}`).innerText;
        slotDate.value = slotDate;
        let slotStartTime = document.getElementById(`${id_start_time}`).innerText;
        slotStartTime.value = slotStartTime;
        let slotEndTime = document.getElementById(`${id_end_time}`).innerText;
        slotEndTime.value = slotEndTime;
        let slotCompleted = document.getElementById(`${id_completed}`).innerText;
        slotCompleted.value = slotCompleted;
        let slotCreditMinutesRequested = document.getElementById(`${id_credit_minutes_requested}`).innerText;
        slotCreditMinutesRequested.value = slotCreditMinutesRequested;
        submitButton.innerText = "Update";
        slotForm.setAttribute("action", `edit_slot/${slotId}`);
    });
}
