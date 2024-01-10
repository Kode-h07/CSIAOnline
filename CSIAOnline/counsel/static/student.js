let studentData = {};
apiURL = "http://127.0.0.1:8000";

// Function to delete a reservation and update the availability row
async function deleteReservation(apiURL, timeSlot) {
  // Check if student data is available
  if (Object.keys(studentData).length === 0) {
    alert("Please log in first.");
    return;
  }

  // Prepare the data to send to the server (assuming you want to mark it as available)
  const reservationData = {
    ...studentData, // Include the student data
    timeSlot: timeSlot, // Include the time slot
  };

  // Make a DELETE request to the server (replace with your server URL)
  try {
    const response = await fetch(apiURL, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(reservationData),
    });

    if (!response.ok) {
      throw new Error("Error updating reservation");
    }

    const data = await response.json();
    console.log(data);

    // Update the availability cell in the HTML based on the response from the server
    const availabilityCell = document.querySelector(
      `td[data-time-slot="${data.timeSlot}"][class="Availability"]`
    );
    if (availabilityCell) {
      // Update availability status
      availabilityCell.textContent = "Available";

      // Hide the "Make Reservation" button and show the "Delete Reservation" button
      const makeButton = document.querySelector(
        `button[data-time-slot="${data.timeSlot}"][data-action="Make"]`
      );
      const deleteButton = document.querySelector(
        `button[data-time-slot="${data.timeSlot}"][data-action="Delete"]`
      );

      if (data.availability) {
        makeButton.style.display = "block";
        deleteButton.style.display = "none";
      } else {
        makeButton.style.display = "none";
        deleteButton.style.display = "block";
      }
    }
  } catch (error) {
    console.error("Error:", error);
    // You can add more user-friendly error handling here, like displaying an error message to the user.
  }
}

// Function to send data to the server and update the availability row
// Add a click event listener to all "Make Reservation" buttons with data-action="Make"
// Define the makeReservation function
async function makeReservation(apiURL, timeSlot) {
  // Check if student data is available
  if (Object.keys(studentData).length === 0) {
    alert("Please log in first.");
    return;
  }

  // Prepare the data to send to the server
  const reservationData = {
    ...studentData, // Include the student data
    timeSlot: timeSlot, // Include the time slot
  };

  try {
    const response = await fetch(apiURL, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(reservationData),
    });

    if (!response.ok) {
      throw new Error("Error updating reservation");
    }

    const data = await response.json();
    console.log(data);

    // Update the availability cell in the HTML based on the response from the server
    const availabilityCell = document.querySelector(
      `td[data-time-slot="${data.timeSlot}"][class="Availability"]`
    );
    if (availabilityCell) {
      // Update availability status
      availabilityCell.textContent = "Reserved";

      // Hide the "Make Reservation" button and show the "Delete Reservation" button
      const makeButton = document.querySelector(
        `button[data-time-slot="${data.timeSlot}"][data-action="Make"]`
      );
      const deleteButton = document.querySelector(
        `button[data-time-slot="${data.timeSlot}"][data-action="Delete"]`
      );

      if (data.availability) {
        makeButton.style.display = "block";
        deleteButton.style.display = "none";
      } else {
        makeButton.style.display = "none";
        deleteButton.style.display = "block";
      }
    }
  } catch (error) {
    console.error("Error:", error);
    // You can add more user-friendly error handling here, like displaying an error message to the user.
  }
}

// Add a click event listener to all "Make Reservation" buttons with data-action="Make"
document
  .querySelectorAll('button[data-action="Make"]')
  .forEach((makeButton) => {
    makeButton.addEventListener("click", (event) => {
      // Get the time slot from the button's data-time-slot attribute
      const timeSlot = event.target.getAttribute("data-time-slot");
      if (!studentData.name || !studentData.gradeLevel || !studentData.gender) {
        alert(
          "Please complete your student login information before making a reservation."
        );
        return;
      }
      console.log(timeSlot);

      // Call the makeReservation function
      makeReservation(apiURL, timeSlot);
    });
  });

document
  .querySelectorAll('button[data-action="Delete"]')
  .forEach((deleteButton) => {
    deleteButton.addEventListener("click", (event) => {
      // Get the time slot from the button's data-time-slot attribute
      const timeSlot = event.target.getAttribute("data-time-slot");
      if (!studentData.name || !studentData.gradeLevel || !studentData.gender) {
        alert(
          "Please complete your student login information before making a reservation."
        );
        return;
      }
      console.log(timeSlot);

      // Call the makeReservation function
      deleteReservation(apiURL, timeSlot);
    });
  });

// Function to handle teacher login
function teacherLogin() {
  const teacherNameInput = document.getElementById("teacherName").value;
  const teacherPasswordInput = document.getElementById("teacherPassword").value;

  // Check if name and password are correct (replace with your authentication logic)
  if (teacherNameInput === "이수희" && teacherPasswordInput === "csiacounsel") {
    alert("Teacher logged in successfully.");
    window.location.href = apiURL + "/teacher";
    // You can add further logic for teacher actions here.
  } else {
    alert("Teacher login failed. Please check your name and password.");
  }
}

// Add event listener for the teacher login button
document
  .getElementById("teacherLoginButton")
  .addEventListener("click", teacherLogin);

// ...

// Add event listeners for login, delete reservation, and update reservation buttons
document.getElementById("loginButton").addEventListener("click", () => {
  window.location.href = apiURL;
});
