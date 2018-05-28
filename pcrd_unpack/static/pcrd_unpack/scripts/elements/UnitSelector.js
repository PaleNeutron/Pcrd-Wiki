let team = [];
let right_team = [];

window.onload = function () {
    // img1 = new Image();
    // img1.src = "/static/pcrd_unpack/Texture2D/assets/_elementsresources/resources/unit/icon/icon_unit_{0}{1}1.jpg";
    // img1.id = "unit_img_left_1";

    // const img_src_base = "/static/pcrd_unpack/Texture2D/assets/_elementsresources/resources/unit/icon/icon_unit_{0}.jpg";
    // $(".unit_selector").change(function () {
    //     let pos =  this.id.split("_").slice(-1)[0];
    //     let unit_id = parseInt($(this).val());
    //     let rarity = 3;
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
    $(".dropdown-menu a").click(function () {
        let img_src = $(this).find("img").attr("src");
        let pos = $(this).parent().attr("id").split("_").slice(-1)[0];
        $(this).closest("div.card").find("img.card-img-top").attr("src", img_src);
        if ($(this).parent().attr("id").includes("right")) {
            right_team = $(this).find("span").text();
        }
        else{
            team[pos-1] = $(this).find("span").text();
        }
        $(this).closest("div.card").find(".unit_rarity_selector").change();
    });
    // change rarity

    $(".unit_rarity_selector").change(function () {
        let rarity = parseInt($(this).val());
        let current_img = $(this).closest("div.card").find("img.card-img-top");
        let img_src = current_img.attr("src");
        if (img_src.includes("unknown")){
            return;
        }
        let img_head = img_src.slice(0,img_src.length - 6);
        if (rarity >=3) {
            img_src = img_head + "3";
        } else {
            img_src = img_head + "1";
        }
        img_src += "1.jpg";

        current_img.attr("src", img_src);
    });
};