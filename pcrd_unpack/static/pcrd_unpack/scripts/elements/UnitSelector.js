"use strict";

$(document).ready(function () {

    // select unit
    set_unit();

    // change rarity
    set_rarity();

    if (check_list_valid(left_team) && check_list_valid(right_team)) {

        var imgs = $(".card-img-top.img-thumbnail");
        var selectors = $(".form-control.unit_rarity_selector");

        imgs.each(function (i, e) {

            $(selectors[i]).change();
        });
    } else {}
});

function set_unit() {
    $(".dropdown-menu a").click(function () {
        var img_src = $(this).find("img").attr("src");
        var pos = $(this).parent().attr("id").split("_").slice(-1)[0];
        $(this).closest("div.card").find("img.card-img-top").attr("src", img_src);
        if ($(this).parent().attr("id").includes("right")) {
            right_team[pos - 1] = $(this).find("span").text();
        } else {
            left_team[pos - 1] = $(this).find("span").text();
        }
        $(this).closest("div.card").find(".unit_rarity_selector").change();
    });
}

function set_rarity() {
    $(".unit_rarity_selector").change(function () {
        var rarity = parseInt($(this).val());
        var current_img = $(this).closest("div.card").find("img.card-img-top");
        var img_src = current_img.attr("src");
        if (img_src.includes("unknown")) {
            return;
        }
        var img_head = img_src.slice(0, img_src.length - 6);
        if (rarity >= 3) {
            img_src = img_head + "3";
        } else {
            img_src = img_head + "1";
        }
        img_src += "1.jpg";
        current_img.attr("src", img_src);

        var pos = $(this).attr("id").split("_").slice(-1)[0];
        if ($(this).attr("id").includes("right")) {
            right_rarity[pos - 1] = parseInt($(this).val());
        } else {
            left_rarity[pos - 1] = parseInt($(this).val());
        }
    });
}

function check_list_valid(team_list) {
    return team_list.length === 5 && !team_list.includes(undefined) && !team_list.includes("");
}