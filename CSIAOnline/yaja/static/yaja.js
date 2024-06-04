// Function to update the entire schedule
// Function to get the selected value of a dropdown

apiURL = "http://127.0.0.1:8000";

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

function updateEntireSchedule() {
  // Retrieve selected values from the
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
  fetch(apiURL+"/yaja", {
    method: "POST", // Assuming it's always a POST request for updating the entire schedule
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(selectedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.student_id)
      if (data.status === "echo") {
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

function retreiveSchedule() {
  console.log('Sending GET request to:', apiURL+"/yaja");
  fetch(apiURL+"/yaja", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log('Received response:', data);
      if (data.action === "retrieve") {
        console.log("GET request responded");
        
        // Monday
        document.getElementById("period1-Monday").value = data.monday.period1;
        document.getElementById("period2-Monday").value = data.monday.period2;
        document.getElementById("period3-Monday").value = data.monday.period3;
    
        // Tuesday
        document.getElementById("period1-Tuesday").value = data.tuesday.period1;
        document.getElementById("period2-Tuesday").value = data.tuesday.period2;
        document.getElementById("period3-Tuesday").value = data.tuesday.period3;
    
        // Wednesday
        document.getElementById("period1-Wednesday").value = data.wednesday.period1;
        document.getElementById("period2-Wednesday").value = data.wednesday.period2;
        document.getElementById("period3-Wednesday").value = data.wednesday.period3;
    
        // Thursday
        document.getElementById("period1-Thursday").value = data.thursday.period1;
        document.getElementById("period2-Thursday").value = data.thursday.period2;
        document.getElementById("period3-Thursday").value = data.thursday.period3;
      }
    })
    .catch((error) => {
      console.error("Error in retrieveSchedule:", error);
    });
}

// Function to update today's schedule
function updateTodaySchedule() {
  // Retrieve selected values from the
  console.log("success in front");
  let selectedValues = {};

  // Loop through periods 1, 2, and 3 to get selected values
  for (let period_num = 1; period_num <= 3; period_num++) {
    let periodId = `period${period_num}`;
    selectedValues[periodId] = getSelectedValue(periodId);
  }

  console.log(selectedValues);

  // Make the request to the backend API to update today's schedule
  fetch(apiURL+"/yaja", {
    method: "PUT", // Assuming it's always a PUT request for updating today's schedule
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(selectedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      console.log("got response");
      if (data.status == "success") {
        alert("Successfully changed today's schedule!");
        window.location.reload(); // Reload the page after successful update
      } else {
        console.error(
          "Error in updateTodaySchedule: Unexpected response",
          data
        );
      }
    })
    .catch((error) => {
      console.error("Error in updateTodaySchedule:", error);
    });
}

// Attach event listeners to the s based on their IDs or other attributes

document.addEventListener("DOMContentLoaded", function () {
  console.log("loaded");
  // Attach change event listener to all select elements
  document.querySelectorAll("select").forEach((dropdown) => {
    dropdown.addEventListener("change", function () {
      let period = this.id;
      let othersDetailInput = document.getElementById(
        `${period}-others-detail`
      );

      if (this.value === "others") {
        othersDetailInput.style.display = "block";
      } else {
        othersDetailInput.style.display = "none";
      }
    });
  });
  document
    .getElementById("yaja_Form")
    .addEventListener("submit", function (event) {
      console.log("clickeeed the submit for today button");
      event.preventDefault();
      updateTodaySchedule();
    });

  document
    .getElementById("scheduleForm")
    .addEventListener("submit", function (event) {
      console.log("clickeeed the submit button");
      event.preventDefault();
      updateEntireSchedule();
    });

  document
    .getElementById("modalpop")
    .addEventListener("click", function (event) {
      console.log("clickeeed to enable retrieveschedule");
      event.preventDefault();
      retreiveSchedule();
    });
});
