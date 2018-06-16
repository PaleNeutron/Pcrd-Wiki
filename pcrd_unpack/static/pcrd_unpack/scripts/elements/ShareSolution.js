"use strict";

function share_btn_bind() {
    $("#share_btn").click(function (e) {
        if (!(check_list_valid(left_team) && check_list_valid(left_team) && check_list_valid(left_team) && check_list_valid(left_team))) {
            alert("units should be selected correctly");
        }
        $(this).attr('aria-disabled', true);
        $(this).attr('disabled', true);
        $(this).addClass('btn-secondary');
        $.ajax({
            url: add_solution_url,
            type: 'POST',
            data: JSON.stringify({
                "left_team": left_team,
                "right_team": right_team,
                "left_rarity": left_rarity,
                "right_rarity": right_rarity
            }),
            contentType: 'application/json',
            success: function success(data, status, jqxhr) {
                window.location.href = data;
            }

        });
    });
}

var btn_up = $("#up_vote_btn");
function up_vote() {
    btn_up.click(function () {

        $(this).attr('aria-disabled', true);
        $(this).attr('disabled', true);
        $(this).addClass('btn-secondary');
        $.ajax({
            url: vote_url,
            type: 'GET',
            data: { "method": "up_vote" },
            success: function success() {
                var l = btn_up.text().split(" ");
                var pre_fix = l[0];
                var i = parseInt(l[1]);
                btn_up.text(pre_fix + " " + (i + 1));
            }
        });
    });
}

var btn_down = $("#down_vote_btn");
function down_vote() {
    btn_down.click(function () {

        $(this).attr('aria-disabled', true);
        $(this).attr('disabled', true);
        $(this).addClass('btn-secondary');
        $.ajax({
            url: vote_url,
            type: 'GET',
            data: { "method": "down_vote" },
            success: function success() {
                var l = btn_down.text().split(" ");
                var pre_fix = l[0];
                var i = parseInt(l[1]);
                btn_down.text(pre_fix + " " + (i + 1));
            }
        });
    });
}

$(document).ready(function () {
    share_btn_bind();
    up_vote();
    down_vote();
});