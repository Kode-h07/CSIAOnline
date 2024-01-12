apiURL = "http://127.0.0.1:8000";

function updateYaja() {
    // Object to store selected values
    let selectedValues = {
        period1: getSelectedValue("period1"),
        period2: getSelectedValue("period2"),
        period3: getSelectedValue("period3"),
    };

    console.log(selectedValues)

    // Make a PUT request to the backend API
    fetch(apiURL+"/yaja/", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(selectedValues),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            // Redirect to the API URL
            alert("Successfully changed!");
            window.location.href = apiURL+"";
        } else {
            console.error("Error in updateYaja: Unexpected response", data);
        }
    })
    .catch(error => {
        console.error("Error in updateYaja:", error);
    });
}

function getSelectedValue(period) {
    // Get the selected value for a specific period
    let dropdown = document.getElementById(period);
    let selectedValue = dropdown.value;

    // If 'others' is selected, get the value from the text input
    if (selectedValue === "others") {
        let othersDetailInput = document.getElementById(`${period}-others-detail`);
        if (othersDetailInput.value.trim() !== "") {
            return othersDetailInput.value;
        }
    }

    return selectedValue;
}

document.getElementById("yajaForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission behavior
    updateYaja();
});

// Show/hide 'others' detail input based on selected value in dropdown
document.querySelectorAll('select').forEach(dropdown => {
    dropdown.addEventListener('change', function () {
        let period = this.id;
        let othersDetailInput = document.getElementById(`${period}-others-detail`);

        if (this.value === "others") {
            othersDetailInput.style.display = "block";
        } else {
            othersDetailInput.style.display = "none";
        }
    });
});
