// Function to update the entire schedule
// Function to get the selected value of a dropdown
function getSelectedValue(dropdownId) {
  let dropdown = document.getElementById(dropdownId);
  let selectedValue = dropdown.options[dropdown.selectedIndex].value;

  // Check if the selected value is "others"
  if (selectedValue === "others") {
    // If "others" is selected, get the value from the input field
    let inputField = document.getElementById(`${dropdownId}-others-detail`);
    return inputField.value;
  } else {
    // If not, return the selected option value
    return selectedValue;
  }
}

function updateEntireSchedule(form) {
  // Retrieve selected values from the form
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

  // Make the request to the backend API to update the entire schedule
  fetch(form.getAttribute("action"), {
    method: "POST", // Assuming it's always a POST request for updating the entire schedule
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(selectedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.action === "setdefault") {
        ["Monday", "Tuesday", "Wednesday", "Thursday"].forEach((day) => {
          selectedValues[day] = {};
          for (let period_num = 1; period_num <= 3; period_num++) {
            let periodId = `period${period_num}-${day}`;
            document.getElementById(periodId).value = data.day.period_num;
          }
        });
      }
      if (data.action === "echo" && data.status === "success") {
        alert("Successfully changed entire schedule!");
        window.location.reload(); // Reload the page after successful update
      } else {
        console.error(
          "Error in updateEntireSchedule: Unexpected response",
          data
        );
      }
    })
    .catch((error) => {
      console.error("Error in updateEntireSchedule:", error);
    });
}

// Function to update today's schedule
function updateTodaysSchedule(form) {
  // Retrieve selected values from the form
  let selectedValues = {};

  // Loop through periods 1, 2, and 3 to get selected values
  for (let period_num = 1; period_num <= 3; period_num++) {
    let periodId = `period${period_num}`;
    selectedValues[periodId] = getSelectedValue(periodId);
  }

  console.log(selectedValues);

  // Make the request to the backend API to update today's schedule
  fetch(form.getAttribute("action"), {
    method: "PUT", // Assuming it's always a PUT request for updating today's schedule
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(selectedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        alert("Successfully changed today's schedule!");
        window.location.reload(); // Reload the page after successful update
      } else {
        console.error(
          "Error in updateTodaysSchedule: Unexpected response",
          data
        );
      }
    })
    .catch((error) => {
      console.error("Error in updateTodaysSchedule:", error);
    });
}

// Attach event listeners to the forms based on their IDs or other attributes
document.querySelectorAll("form").forEach((form) => {
  if (form.id === "scheduleForm") {
    // If it's the form for updating the entire schedule
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission behavior
      updateEntireSchedule(form);
    });
  } else if (form.id === "todaysScheduleForm") {
    // If it's the form for updating today's schedule
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission behavior
      updateTodaysSchedule(form);
    });
  }
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
