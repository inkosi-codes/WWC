$(document).ready(function () {
    $('#edit-button').click(function () {
        var disabled = $("Input").prop('disabled');
        if (disabled) {
            $("Input").prop('disabled', false);
        }
        else {
            $("Input").prop('disabled', true);
        }

    })
});

$(document).ready(function() {
    $("#edit-button").click(function() {
        $("#save-button").show();
    });

    $("#save-button").click(function() {
        $("#save-button").hide();
        $("Input").prop('disabled', true); 
    });
});