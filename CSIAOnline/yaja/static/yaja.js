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

function updateDefaultSchedule() {
  // Retrieve selected values from the
  let selectedValues = {};

  // Loop through each day and period to get selected values
  ["Monday", "Tuesday", "Wednesday", "Thursday"].forEach((day) => {
    selectedValues[day] = {};
    for (let period_num = 1; period_num <= 3; period_num++) {
      let periodId = `default-period${period_num}-${day}`;
      selectedValues[day][`period${period_num}`] = getSelectedValue(periodId);
    }
  });

  console.log(selectedValues);

  // Make the request to the backend API to update the entire schedule
  fetch(apiURL + "/yaja/", {
    method: "POST", // Assuming it's always a POST request for updating the entire schedule
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(selectedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.student_id);
      if (data.status === "echo") {
        alert("Successfully changed Default schedule!");
        window.location.reload(); // Reload the page after successful update
      } else {
        console.error(
          "Error in updateDefaultSchedule: Unexpected response",
          data
        );
      }
    })
    .catch((error) => {
      console.error("Error in updateDefaultSchedule:", error);
    });
}

function retrieveDefaultSchedule() {
  console.log("Sending GET request to:", apiURL + "/yaja");
  fetch(apiURL + "/yaja/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "X-Schedule-Type": "default",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Received response:", data);
      if (data.action === "retrieve") {
        console.log("GET request responded");

        // Monday
        document.getElementById("default-period1-Monday").value =
          data.monday.period1;
        document.getElementById("default-period2-Monday").value =
          data.monday.period2;
        document.getElementById("default-period3-Monday").value =
          data.monday.period3;

        // Tuesday
        document.getElementById("default-period1-Tuesday").value =
          data.tuesday.period1;
        document.getElementById("default-period2-Tuesday").value =
          data.tuesday.period2;
        document.getElementById("default-period3-Tuesday").value =
          data.tuesday.period3;

        // Wednesday
        document.getElementById("default-period1-Wednesday").value =
          data.wednesday.period1;
        document.getElementById("default-period2-Wednesday").value =
          data.wednesday.period2;
        document.getElementById("default-period3-Wednesday").value =
          data.wednesday.period3;

        // Thursday
        document.getElementById("default-period1-Thursday").value =
          data.thursday.period1;
        document.getElementById("default-period2-Thursday").value =
          data.thursday.period2;
        document.getElementById("default-period3-Thursday").value =
          data.thursday.period3;
      }
    })
    .catch((error) => {
      console.error("Error in retrieveSchedule:", error);
    });
}

// Function to update today's schedule
function updateWeekSchedule() {
  // Retrieve selected values from the inputs for Monday to Thursday
  let updatedValues = {
    Monday: {},
    Tuesday: {},
    Wednesday: {},
    Thursday: {},
  };

  // Loop through days and periods to get selected values
  let days = ["Monday", "Tuesday", "Wednesday", "Thursday"];
  for (let day of days) {
    for (let period_num = 1; period_num <= 3; period_num++) {
      let periodId = `period${period_num}-${day}`;
      updatedValues[day][`period${period_num}`] =
        document.getElementById(periodId).value;
    }
  }

  console.log(updatedValues);

  // Make the request to the backend API to update this week's schedule
  fetch(apiURL + "/yaja/", {
    method: "PUT", // PUT request to update the entire week's schedule
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updatedValues),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      console.log("got response");
      if (data.status == "success") {
        alert("Successfully changed this week's schedule!");
        window.location.reload(); // Reload the page after successful update
      } else {
        console.error("Error in updateWeekSchedule: Unexpected response", data);
      }
    })
    .catch((error) => {
      console.error("Error in updateWeekSchedule:", error);
    });
}

function retrieveCurrentSchedule() {
  console.log("Sending GET request to:", apiURL + "/yaja");
  fetch(apiURL + "/yaja/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "X-Schedule-Type": "current",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Received response:", data);
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
        document.getElementById("period1-Wednesday").value =
          data.wednesday.period1;
        document.getElementById("period2-Wednesday").value =
          data.wednesday.period2;
        document.getElementById("period3-Wednesday").value =
          data.wednesday.period3;

        // Thursday
        document.getElementById("period1-Thursday").value =
          data.thursday.period1;
        document.getElementById("period2-Thursday").value =
          data.thursday.period2;
        document.getElementById("period3-Thursday").value =
          data.thursday.period3;
      }
    })
    .catch((error) => {
      console.error("Error in retrieveSchedule:", error);
    });
}

// Attach event listeners to the s based on their IDs or other attributes

document.addEventListener("DOMContentLoaded", function () {
  console.log("loaded");
  retrieveCurrentSchedule();
  // Attach change event listener to all select elements
  document
    .getElementById("weekForm")
    .addEventListener("submit", function (event) {
      console.log("clickeeed the submit for today button");
      event.preventDefault();
      updateWeekSchedule();
    });

  document
    .getElementById("defaultForm")
    .addEventListener("submit", function (event) {
      console.log("clickeeed the submit button");
      event.preventDefault();
      updateDefaultSchedule();
    });

  document
    .getElementById("modalpop")
    .addEventListener("click", function (event) {
      console.log("clickeeed to enable retrieveschedule");
      event.preventDefault();
      retrieveDefaultSchedule();
    });
});
