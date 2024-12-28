const editButtons = document.getElementsByClassName("btn-edit");
const slotTask = document.getElementById("id_task");
const slotTaskLocation = document.getElementById("id_task_location")
const slotForm = document.getElementById("slotForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        let slotTaskContent = document.getElementById(`slot${slotId}`).innerText;
        slotTask.value = slotTaskContent;
        submitButton.innerText = "Update";
        slotForm.setAttribute("action", `edit_slot/${slotId}`);
    });
}
