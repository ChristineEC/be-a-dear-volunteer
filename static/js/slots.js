const editButtons = document.getElementsByClassName("btn-edit");
const slotTask = document.getElementById("id_task")
const slotTaskLocation = document.getElementById("id_task_location")
const slotTaskDates = document.getElementById("id_dates")
const slotTaskTimes = document.getElementById("id_times")
const slotTaskCompleted = document.getElementById("id_completed")
const slotTaskCreditMinutesRequested = document.getElementById("id_credit_minutes_requested")
const slotForm = document.getElementById("slotForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
        button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        let slotTaskContent = document.getElementById(`task${slotId}`).innerText;
        slotTask.value = slotTaskContent;
        let slotTaskLocationContent = document.getElementById(`task_location${slotId}`).innerText;
        slotTaskLocation.value = slotTaskLocationContent;
        let slotTaskDatesContent = document.getElementById(`dates${slotId}`).innerText;
        slotTaskDates.value = slotTaskDatesContent;
        let slotTaskTimesContent = document.getElementById(`times${slotId}`).innerText;
        slotTaskTimes.value = slotTaskTimesContent;
        let slotTaskCompletedContent = document.getElementById(`completed${slotId}`).innerText;
        slotTaskCompleted.value = slotTaskCompletedContent;
        let slotTaskCreditMinutesRequestedContent = document.getElementById("credit_minutes_requested${slotId}");
        slotTaskCreditMinutesRequested =slotTaskCreditMinutesRequestedContent;
        submitButton.innerText = "Update";
        slotForm.setAttribute("action", `edit_slot/${slotId}`);

        console.log("This is from inside the event listener function");
    });
}

console.log("The function has completed!");
