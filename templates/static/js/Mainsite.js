let dt = document.getElementById("enrolldate"); //get your date
let ebutton = document.getElementById("enroll-button")

let today = new Date(); //get date today
let enrolldate = new Date(dt.innerText);

today = today.getTime();
enrolldate = enrolldate.setFullYear(enrolldate.getFullYear() + 1);

function enroll() {
    if (today > enrolldate) {
        dt.style.color = "red";
        alert(
            "Your benefits enrollment has expired. Please use the enrollment button to apply for benefits"
        );
        ebutton.style.display = 'block'
    } else if (today < enrolldate) {
        dt.style.color = "black";
        ebutton.style.display = 'None'
    }
}
