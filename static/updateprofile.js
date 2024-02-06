document.getElementById("profileForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let formData = new FormData(this);

    fetch("/updateprofile", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        console.log("Profile updated successfully:", data);
        // Optionally, update UI to indicate success
    })
    .catch(error => {
        console.error("Error updating profile:", error);
        // Optionally, update UI to indicate error
    });
});
