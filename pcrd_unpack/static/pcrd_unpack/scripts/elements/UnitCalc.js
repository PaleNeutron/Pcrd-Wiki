class UnitDataModel {
    constructor() {
        this.level = 0;
        this.rank = 1;
        this.rarity = 1;

        this.hp = 0;
        this.atk = 0;
        this.magic_str = 0;
        this.def_field = 0;
        this.magic_def = 0;
        this.physical_critical = 0;
        this.dodge = 0;

        this.unit_parameter = {};

        this.MAX_LEVEL = 88;
        this.MAX_RANK = 8;
        this.MAX_RARITY = 5;
        this.result_ids = data_tags;
    }

    get_input() {
        this.level = parseInt($("#level").val());
        this.rank = parseInt($("#rank").val());
        this.rarity = parseInt($("#rarity").val());

        if (isNaN(this.level) || isNaN(this.rank) || isNaN(this.rarity)) {
            return false;
        }
        if (this.level > this.MAX_LEVEL) {
            return false;
        }

        if (this.rank > this.MAX_RANK) {
            return false;
        }

        if (this.rarity > this.MAX_RARITY) {
            return false;
        }

        return true;
    }

    calc() {
        if (!(Object.keys(this.unit_parameter).length === 0 && this.unit_parameter.constructor === Object)) {
            if (!this.get_input()) {
                return false;
            }
            let m = this;

            // prepare parameters
            let current_param = this.unit_parameter["unit_data"][this.rarity - 1];
            let l = this.level;

            // apply level growth
            this.result_ids.forEach(function (tag) {
                if (tag in current_param){
                    let base = current_param[tag];
                    // since def is escaped to def_field but def_growth not escaped to def_field_growth
                    let growth_tag = (tag + "_growth").replace("_field", "");
                    let growth = 0;
                    if (growth_tag in current_param){
                        growth = current_param[growth_tag];
                    }
                    m[tag] = base + growth * l;
                }
            });
            // let atk = current_param["atk"];
            // let atk_growth = current_param["atk_growth"];
            // let def_field = current_param["def_field"];
            // let def_growth = current_param["def_growth"];
            // let dodge = current_param["dodge"];
            // let hp_growth = current_param["hp_growth"];
            // let hp = current_param["hp"];
            // let magic_def = current_param["magic_def"];
            // let magic_def_growth = current_param["magic_def_growth"];
            // let unit_material_id = current_param["unit_material_id"];
            // let magic_str = current_param["magic_str"];
            // let magic_str_growth = current_param["magic_str_growth"];
            // let physical_critical = current_param["physical_critical"];
            //
            // this.atk = atk_growth * l + atk;
            // this.hp = hp_growth * l + hp;
            // this.magic_str = magic_str_growth * l + magic_str;
            // this.def_field = def_field + def_growth * l;
            // this.magic_def = magic_def + magic_def_growth * l;
            // this.physical_critical = physical_critical;
            // this.dodge = dodge;


            // get rank data
            if (m.rank > 1) {
                let current_rank_data = m.unit_parameter["unit_rank_data"][m.rank - 2];
                m.result_ids.forEach(function (s) {
                    m[s] += current_rank_data[s];
                });
            }

            // get equipment data
            if (m.rank > 1) {
                let current_equipments_data = m.unit_parameter["unit_promotion_data"][m.rank - 2];
                current_equipments_data.forEach(function (eq) {
                    m.result_ids.forEach(function (s) {
                        m[s] += m.unit_parameter["equipment_data"][eq][s];
                        m[s] += m.unit_parameter["equipment_enhance"][eq][s] *(1 + m.unit_parameter["equipment_enhance"][eq]["promotion_level"]);
                    });
                });
            }
            this.set_result();
            return true;
        }
    }

    set_result() {
        let m = this;
        this.result_ids.forEach(function (s) {
            $("#" + s).text(Math.round(m[s]));
        });
        return true;
    }
}

function pcrd_calculate() {
    udm.calc();
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
    observer.disconnect();
    parameterChecker();
    startObserve();
    pcrd_calculate();
    // tags.forEach(function (element) {
    //     let r = parseInt(document.getElementById(element).innerHTML);
    //     console.log(element.toString()+":"+ r);
    // });
}

let unit_parameter = {};
let udm = new UnitDataModel();
let observer = new MutationObserver(pcrd_calculate_main);
let observer_config = {characterData: true, subtree: true, childList: true};

function startObserve() {
    let targetNode = document.getElementById('parameters');
    observer.observe(targetNode, observer_config);
}

window.onload = function () {
    pcrd_unit_data_init();
};