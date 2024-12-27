const editButtons = document.getElementsByClassName("btn-edit");
const slotText = document.getElementById("id_task");
// const slotText2 = document.getElementById("id_task_location")
// const slotLocation = document.getElementById("id_task_location");
// const slotDate = document.getElementById("id_date");
// const slotStartTime = document.getElementById("id_start_time");
// const slotEndTime = document.getElementById("id_end_time");
// const slotCompleted = document.getElementById("id_completed");
// const slotCreditMinutesRequested = document.getElementById("id_credit_minutes_requested");
// const slotCreditMinutesApproved = document.getElementById("id_credit_minutes_approved");
const slotForm = document.getElementById("slotForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        // let slotContent = document.getElementById(`slot${slotId}`).innerText;
        // slotText.value = slotContent;
        let slotTask = document.getElementById(`${id_task}`).innerText;
        slotTask.value = slotTask;
        let slotTaskLocation = document.getElementById(`${id_task_location}`).innerText;
        slotTaskLocation.value = slotTaskLocation;
        let slotDate = document.getElementById(`${id_date}`).value;
        slotDate.value = slotDate;
        let slotStartTime = document.getElementById(`${id_start_time}`).value;
        slotStartTime.value = slotStartTime;
        let slotEndTime = document.getElementById(`${id_end_time}`).value;
        slotEndTime.value = slotEndTime;
        let slotCompleted = document.getElementById(`${id_completed}`).value;
        slotCompleted.value = slotCompleted;
        let slotCreditMinutesRequested = document.getElementById(`${id_credit_minutes_requested}`).value;
        slotCreditMinutesRequested.value = slotCreditMinutesRequested;
        submitButton.innerText = "Update";
        slotForm.setAttribute("action", `slot_edit/${slotId}`);
    });
}
