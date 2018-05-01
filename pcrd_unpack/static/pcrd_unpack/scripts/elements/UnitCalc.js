
function set_result(udm) {
    let m = udm;
    udm.result_ids.forEach(function (s) {
        $("#" + s).text(Math.round(m[s]));
    });
    return true;
}

function pcrd_calculate() {
    parameterChecker();
    udm.result_ids = data_tags;
    udm.calc(parseInt($("#level").val()),
             parseInt($("#rank").val()),
             parseInt($("#rarity").val()));
    set_result(udm);
}

function pcrd_unit_data_init() {
    unit_parameter = $.getJSON(data_url, success = function (data) {
        unit_parameter = data;
        udm.unit_parameter = unit_parameter;
        tags.forEach(function (tag) {
            udm["max_"+tag] = parseInt($("#" + tag).val());
        });

        $("#parameters input").on("change paste keyup",
            pcrd_calculate
        );
        pcrd_calculate_main();
    });
}

function parameterChecker() {
    tags.forEach(function (element) {
        let temp = document.getElementById(element);
        if (temp.value > udm["max_" + element]) {
            temp.value = udm["max_" + element];
        }
        else if (temp.value < 1) {
            temp.value = 1;
        }
    });
}

function pcrd_calculate_main() {

    pcrd_calculate();
}

let unit_parameter = {};
let udm = new UnitDataModel();

window.onload = function () {
    pcrd_unit_data_init();
};