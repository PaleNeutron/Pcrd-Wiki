class UnitDataModel {
    constructor(){
        this.level = 0;
        this.rank = 1;
        this.rarity = 1;

        this.hp = 0;
        this.atk = 0;
        this.magic_str = 0;
        this.def_field = 0;
        this.magic_def =0;
        this.physical_critical = 0;
        this.dodge = 0;

        this.unit_parameter = {};

        this.MAX_LEVEL = 88;
        this.MAX_RANK = 8;
        this.MAX_RARITY = 5;
        this.result_ids = ["hp", 'atk', 'magic_str', 'def_field', 'magic_def', 'physical_critical', 'dodge'];


    }

    get_input() {
        this.level = parseInt($("#level").text());
        if (this.level > this.MAX_LEVEL || isNaN(this.level)) {
            return false;
        }
        
        this.rank = parseInt($("#rank").text());
        if (this.rank > this.MAX_RANK || isNaN(this.rank)) {
            return false;
        }

        this.rarity = parseInt($("#rarity").text());
        if (this.rarity > this.MAX_RARITY || isNaN(this.rarity)) {
            return false;
        }

        return true;
    }

    calc() {
        if (!(Object.keys(this.unit_parameter).length === 0 && this.unit_parameter.constructor === Object)){
            if (! this.get_input()) {
                return false;
            }
            // prepare parameters
            let current_param = this.unit_parameter["unit_data"][this.rarity - 1];
            let atk = current_param["atk"];
            let atk_growth = current_param["atk_growth"];
            let def_field = current_param["def_field"];
            let def_growth = current_param["def_growth"];
            let dodge = current_param["dodge"];
            let hp_growth = current_param["hp_growth"];
            let hp = current_param["hp"];
            let magic_def = current_param["magic_def"];
            let magic_def_growth = current_param["magic_def_growth"];
            let unit_material_id = current_param["unit_material_id"];
            let magic_str = current_param["magic_str"];
            let magic_str_growth = current_param["magic_str_growth"];
            let physical_critical = current_param["physical_critical"];

            // apply level growth
            this.atk = atk_growth * this.level + atk;
            this.hp = hp_growth * this.level + hp;
            this.magic_str = magic_str_growth * this.level + magic_str;
            this.def_field = def_field + def_growth * this.level;
            this.magic_def = magic_def + magic_def_growth * this.level;
            this.physical_critical = physical_critical;
            this.dodge = dodge;


            // get rank data
            let m = this;
            let current_rank_data = m.unit_parameter["unit_rank_data"][m.rank - 2];
            console.log(current_rank_data);
            m.result_ids.forEach(function (s) {
                m[s] += current_rank_data[s];
            });

            this.set_result();
            return true;
        }
    }

    set_result(){
        let m = this;
        this.result_ids.forEach(function (s) {
            $("#"+s).text(Math.round(m[s]));
        });
        return true;
    }
}

function pcrd_calculate() {
    udm.calc();
}

function pcrd_unit_data_init() {
    $("#level").text(88);
    $("#rarity").text(5);
    $("#rank").text(8);
    unit_parameter = $.getJSON(data_url, success=function (data) {
        // enable edit after get data
        tags.forEach(function(element){
            let e = document.getElementById(element);
            e.contentEditable = true;
            e.onclick = function () {
                window.getSelection().selectAllChildren(this)
            };
        });
        // console.log(data);
        unit_parameter = data;
        udm.unit_parameter = unit_parameter;
        pcrd_calculate_main();
    });
}

function parameterChecker() {
    tags.forEach(function(element){
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
    pcrd_calculate_main();
    startObserve();
};