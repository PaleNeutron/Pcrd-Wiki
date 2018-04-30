
function set_result(udm) {
    let m = udm;
    udm.result_ids.forEach(function (s) {
        $("#" + s).text(Math.round(m[s]));
    });
    return true;
}

function pcrd_calculate() {
    udm.result_ids = data_tags;
    udm.calc(parseInt($("#level").val()),
             parseInt($("#rank").val()),
             parseInt($("#rarity").val()));
    set_result(udm);
}

function pcrd_unit_data_init() {
    $("#level").val(88);
    $("#rarity").val(5);
    $("#rank").val(8);
    unit_parameter = $.getJSON(data_url, success = function (data) {
        // enable edit after get data
        tags.forEach(function (element) {
            let e = document.getElementById(element);
            e.contentEditable = true;
            e.onclick = function () {
                window.getSelection().selectAllChildren(this)
            };
        });
        // console.log(data);
        unit_parameter = data;
        udm.unit_parameter = unit_parameter;
        $("#parameters input").on("change paste keyup",
            pcrd_calculate
        );
        pcrd_calculate_main();
    });
}

function parameterChecker() {
    tags.forEach(function (element) {
        let temp = document.getElementById(element);
        if (temp.innerHTML.match(/[^\d]/)) {
            temp.innerHTML = temp.innerHTML.replace(/[^\d]/g, '');
        }
    });
}

function pcrd_calculate_main() {
    parameterChecker();
    pcrd_calculate();
}

let unit_parameter = {};
let udm = new UnitDataModel();

window.onload = function () {
    pcrd_unit_data_init();
};