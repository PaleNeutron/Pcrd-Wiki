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

        this.result_ids = [];
    }

    get_input(level, rank, rarity) {
        this.level = level;
        this.rank = rank;
        this.rarity = rarity;

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

    calc(level, rank, rarity) {
        if (!(Object.keys(this.unit_parameter).length === 0 && this.unit_parameter.constructor === Object)) {
            if (!this.get_input(level, rank, rarity)) {
                return false;
            }
            let m = this;

            // prepare parameters
            let current_param = this.unit_parameter["unit_data"][this.rarity - 1];
            let l = this.level + this.rank;

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
                let current_equipments_data = m.unit_parameter["unit_promotion_data"][m.rank - 1];
                current_equipments_data.forEach(function (eq) {
                    if (eq === 999999) return;
                    let pl = m.unit_parameter["equipment_enhance"][eq]["promotion_level"];
                    let et = m.unit_parameter["enhance_table"][pl];
                    m.result_ids.forEach(function (s) {
                        m[s] += Math.floor(m.unit_parameter["equipment_data"][eq][s]
                            + m.unit_parameter["equipment_enhance"][eq][s]
                            *et);
                    });
                });
            }
            return true;
        }
    }

}