$.get("./templates/nav-template.html", function(data){
    $("#nav-placeholder").replaceWith(data);
});

$.get("./templates/footer-template.html", function(data){
    $("#footer-placeholder").replaceWith(data);
});