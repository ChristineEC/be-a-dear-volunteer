const editButtons = document.getElementsByClassName("btn-edit");
const slotTask = document.getElementById("id_task");
const slotForm = document.getElementById("slotForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let slotId = e.target.getAttribute("slot_id");
        let slotTaskContent = document.getElementById(`slot${slotId}`).innerText;
        slotTask.value = slotTaskContent;
        submitButton.innerText = "Update";
        slotForm.setAttribute("action", `edit_slot/${slotId}`);
        console.log("This is from inside the event listener function")
    });
}

console.log("The function has completed!")