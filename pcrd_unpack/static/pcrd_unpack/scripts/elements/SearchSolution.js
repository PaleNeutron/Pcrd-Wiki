"use strict";

$(window).ready(function () {
    $("#btn_search").click(function () {
        $.ajax({
            url: search_url,
            type: 'POST',
            data: JSON.stringify({
                "team": left_team,
                "rarity": left_rarity
            }),
            contentType: 'application/json',
            success: function success(response) {
                // $("html").html(response);
                var result_div = "#solution_search_result";
                var result = $(response).find(result_div).html();
                if (result.length > 10) {
                    $(result_div).html(result);
                } else {
                    $(result_div).html("<div class='row justify-content-center'><h2>No Result</h2></div>");
                }
            }
        });
    });
});