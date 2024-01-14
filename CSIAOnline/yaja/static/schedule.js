const apiURL = "http://127.0.0.1:8000";

function updateSchedule() {
  // Object to store selected values
  let selectedValues = {};

  // Loop through each day and period to get selected values
  ["Monday", "Tuesday", "Wednesday", "Thursday"].forEach((day) => {
    selectedValues[day] = {};
    for (let period_num = 1; period_num <= 3; period_num++) {
      let periodId = `period${period_num}-${day}`;
      selectedValues[day][`period${period_num}`] = getSelectedValue(periodId);
    }
  });

  console.log(selectedValues);

  // Make a PUT request to the backend API
  fetch(apiURL + "/yaja/schedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(selectedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        // Redirect to the API URL
        alert("Successfully changed!");
        window.location.href = apiURL + "";
      } else {
        console.error("Error in updateSchedule: Unexpected response", data);
      }
    })
    .catch((error) => {
      console.error("Error in updateSchedule:", error);
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

// Attach the updateSchedule function to the form submission
document
  .getElementById("scheduleForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission behavior
    updateSchedule();
  });

// Show/hide 'others' detail input based on selected value in dropdown
document.querySelectorAll("select").forEach((dropdown) => {
  dropdown.addEventListener("change", function () {
    let period = this.id;
    let othersDetailInput = document.getElementById(`${period}-others-detail`);

    if (this.value === "others") {
      othersDetailInput.style.display = "block";
    } else {
      othersDetailInput.style.display = "none";
    }
  });
});
