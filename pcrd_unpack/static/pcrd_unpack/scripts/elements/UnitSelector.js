window.onload = function () {
    // img1 = new Image();
    // img1.src = "/static/pcrd_unpack/Texture2D/assets/_elementsresources/resources/unit/icon/icon_unit_{0}{1}1.jpg";
    // img1.id = "unit_img_left_1";

    // const img_src_base = "/static/pcrd_unpack/Texture2D/assets/_elementsresources/resources/unit/icon/icon_unit_{0}.jpg";
    // $(".unit_selector").change(function () {
    //     var pos =  this.id.split("_").slice(-1)[0];
    //     var unit_id = parseInt($(this).val());
    //     var rarity = 3;
    //
    //     if (rarity >=3) {
    //         unit_id += 30;
    //     } else {
    //         unit_id += 10;
    //     }
    //
    //     $("#unit_img_left_"+pos).attr("src", img_src_base.replace("{0}", unit_id));
    // });

    // select unit
    set_unit();

    // change rarity
    set_rarity();


    if (check_list_valid(left_team) && check_list_valid(right_team)){


        var imgs = $(".card-img-top.img-thumbnail");
        var selectors = $(".form-control.unit_rarity_selector");

        var team = left_team.concat(right_team);
        var ratity = left_rarity.concat(right_rarity);
        imgs.each(function (i, e) {
            // set unit
            // e.src = (unit_icon_path + "/icon_unit_" + (parseInt(team[i]) + 30) + ".jpg");
            // $(e).disable();
            // set rarity
            // selectors[i].value = (ratity[i]);
            $(selectors[i]).change();

        });
    } else {
    }
    share_btn_bind();

    up_vote();
    down_vote();

};

function set_unit() {
    $(".dropdown-menu a").click(function () {
        var img_src = $(this).find("img").attr("src");
        var pos = $(this).parent().attr("id").split("_").slice(-1)[0];
        $(this).closest("div.card").find("img.card-img-top").attr("src", img_src);
        if ($(this).parent().attr("id").includes("right")) {
            right_team[pos-1] = $(this).find("span").text();
        }
        else{
            left_team[pos-1] = $(this).find("span").text();
        }
        $(this).closest("div.card").find(".unit_rarity_selector").change();
    });
}

function set_rarity() {
    $(".unit_rarity_selector").change(function () {
        var rarity = parseInt($(this).val());
        var current_img = $(this).closest("div.card").find("img.card-img-top");
        var img_src = current_img.attr("src");
        if (img_src.includes("unknown")){
            return;
        }
        var img_head = img_src.slice(0,img_src.length - 6);
        if (rarity >=3) {
            img_src = img_head + "3";
        } else {
            img_src = img_head + "1";
        }
        img_src += "1.jpg";
        current_img.attr("src", img_src);

        var pos = $(this).attr("id").split("_").slice(-1)[0];
        if ($(this).attr("id").includes("right")) {
            right_rarity[pos-1] = $(this).val();
        }
        else{
            right_rarity[pos-1] = $(this).val();
        }
    });
}