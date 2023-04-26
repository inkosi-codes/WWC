// Get the modal
const modal = document.getElementById("myModal");

// Get the link that opens the modal
const link = document.getElementById("myLink");

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close");

// When the user clicks on the link, open the modal
link.onclick = function(event) {
  event.preventDefault(); // Prevent the link from navigating to a new page
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}