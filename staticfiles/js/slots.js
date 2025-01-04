const editButtons = document.getElementsByClassName("btn-edit");
const slotTask = document.getElementById("id_task")
const slotTaskLocation = document.getElementById("id_task_location")
const slotTaskDate = document.getElementById("id_date")
const slotTaskStartTime = document.getElementById("id_start_time")
const slotTaskEndTime = document.getElementById("id_end_time")
const slotTaskCompleted = document.getElementById("id_completed")
const slotTaskCreditMinutesRequested = document.getElementById("id_credit_minutes_requested")
const slotUpdateForm = document.getElementById("slotUpdateForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
        button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        let slotTaskContent = document.getElementById(`task${slotId}`).innerText;
        slotTask.value = slotTaskContent;
        let slotTaskLocationContent = document.getElementById(`task_location${slotId}`).innerText;
        slotTaskLocation.value = slotTaskLocationContent;
        let slotTaskDateContent = document.getElementById(`date${slotId}`).innerText;
        slotTaskDate.value = slotTaskDateContent;
        let slotTaskStartTimeContent = document.getElementById(`start_time${slotId}`).innerText;
        slotTaskStartTime.value = slotTaskStartTimeContent;
        let slotTaskEndTimeContent = document.getElementById(`end_time${slotId}`).innerText;
        slotTaskEndTime.value = slotTaskEndTimeContent;
        let slotTaskCompletedContent = document.getElementById(`completed${slotId}`).innerText;
        slotTaskCompleted.value = slotTaskCompletedContent;
        let slotTaskCreditMinutesRequestedContent = document.getElementById("credit_minutes_requested${slotId}");
        slotTaskCreditMinutesRequested =slotTaskCreditMinutesRequestedContent;
        submitButton.innerText = "Update";
        slotUpdateForm.setAttribute("action", `edit_slot/${slotId}`);

        console.log("This is from inside the event listener function");
    });
}

console.log("The function has completed!");
