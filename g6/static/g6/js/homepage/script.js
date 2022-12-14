
/* This function handle the profile navigation displaying the 
appropriate section depending on the button clicked */

function profileMenu() {
    let appointmentButton = document.getElementById('my-appointment-button')
    let reportButton = document.getElementById('my-report-button')
    let detailsButton = document.getElementById('my-details-button')
    let availabilityButton = document.getElementById('my-availabilities-button')
    
    let appointmentSection = document.getElementById('appointment-section')
    let reportSection = document.getElementById('report-section')
    let detailsSection = document.getElementById('details-section')
    let availabilitySection = document.getElementById('availabilities-section')


    appointmentButton.onclick = function() {
        appointmentSection.style.display = "block"
        reportSection.style.display = "none"
        detailsSection.style.display = "none"
        availabilitySection.style.display = "none"
    }; 

    reportButton.onclick = function() {
        appointmentSection.style.display = "none"
        reportSection.style.display = "block"
        detailsSection.style.display = "none"
        availabilitySection.style.display = "none"
    }; 

    detailsButton.onclick = function() {
        appointmentSection.style.display = "none"
        reportSection.style.display = "none"
        detailsSection.style.display = "block"
        availabilitySection.style.display = "none"
    }; 

    availabilityButton.onclick = function() {
        appointmentSection.style.display = "none"
        reportSection.style.display = "none"
        detailsSection.style.display = "none"
        availabilitySection.style.display = "block"
    }; 
}

// Populate the variables for the buttons and sections
profileMenu()