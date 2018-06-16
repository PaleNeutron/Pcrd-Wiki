"use strict";

function set_result(udm) {
    var m = udm;
    udm.result_ids.forEach(function (s) {
        $("#" + s).text(m[s]);
    });
    return true;
}

function pcrd_calculate() {
    parameterChecker();
    udm.result_ids = data_tags;
    udm.calc(parseInt($("#level").val()), parseInt($("#rank").val()), parseInt($("#rarity").val()), parseInt($("#love").val()));
    set_result(udm);
}

var tags = [];
function pcrd_unit_data_init() {
    unit_parameter = $.getJSON(data_url, success = function success(data) {
        unit_parameter = data;
        udm.unit_parameter = unit_parameter;
        tags = $("#input_tags input").map(function () {
            return this.id;
        }).get();
        tags.forEach(function (tag) {
            udm["max_" + tag] = parseInt($("#" + tag).val());
        });

        $("#parameters input").on("change paste keyup", pcrd_calculate);
        pcrd_calculate_main();
    });
}

function parameterChecker() {
    tags.forEach(function (element) {
        var temp = document.getElementById(element);
        if (temp.value > udm["max_" + element]) {
            temp.value = udm["max_" + element];
        } else if (temp.value < 1) {
            temp.value = 1;
        }
    });
}

function pcrd_calculate_main() {

    pcrd_calculate();
}

var unit_parameter = {};
var udm = new UnitDataModel();

window.onload = function () {
    pcrd_unit_data_init();
};