// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function share_btn_bind () {
    $("#share_btn").click(function (e) {
        if (!(check_list_valid(left_team) && check_list_valid(left_team) && check_list_valid(left_team) && check_list_valid(left_team))){
            alert("units should be selected correctly")
        }
        $(this).attr('aria-disabled', true);
        $(this).attr('disabled', true);
        $(this).addClass('btn-secondary');
        $.ajax({
            url:add_solution_url,
            type: 'POST',
            data:
                JSON.stringify({
                    "left_team": left_team,
                    "right_team": right_team,
                    "left_rarity": left_rarity,
                    "right_rarity": right_rarity,
                }),
            contentType: 'application/json',
            success: function (data, status, jqxhr) {
                window.location.href = data;
            },

        });
    });
}


function check_list_valid(team_list) {
    return team_list.length ===5 && !team_list.includes(undefined)
}