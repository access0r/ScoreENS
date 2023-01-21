// JavaScript code for the frontend
const buttons = document.querySelectorAll('.btn-up, .btn-down');
for (let button of buttons) {
    button.addEventListener('click', (event) => {
        let dataId = event.target.dataset.id;
        let rating = event.target.classList.contains('btn-up') ? 1 : -1;
        updateRating(dataId, rating);
    });
}

function updateRating(dataId, rating) {
    const formData = new FormData();
    formData.append("data_id", dataId);
    formData.append("rating", rating);
    fetch("/rate", {
            method: "POST",
            body: formData
        })
        .then(response => {
            // Do something with the response
        });
}

<