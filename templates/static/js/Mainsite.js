var dt = document.getElementById("enrolldate"); //get your date
var today = new Date(); //get date today

today = today.setFullYear(today.getFullYear() - 1)

enrolldate = new Date(dt.innerText);
enrolldate = enrolldate.getTime();

if (enrolldate < today) {
  dt.style.color = "red";
}

function benefitsalert(){
if (dt.style.color = "red"){
    onload=alert("Your benefits enrollment has expired. Please use the enrollment button to apply for benefits")
}
}
// console.log(enrolldate)

window.onload = function () {
    benefitsalert();
    getCoords();
  };