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

    get_input(level, rank, rarity, love) {
        this.level = level;
        this.rank = rank;
        this.rarity = rarity;
        this.love = love;

        if (isNaN(this.level) || isNaN(this.rank) || isNaN(this.rarity) || isNaN(this.love)) {
            return false;
        }

        return true;
    }

    calc(level, rank, rarity, love) {
        if (!(Object.keys(this.unit_parameter).length === 0 && this.unit_parameter.constructor === Object)) {
            if (!this.get_input(level, rank, rarity, love)) {
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


            // get rank data
            if (m.rank > 1) {
                let current_rank_data = m.unit_parameter["unit_rank_data"][m.rank - 2];
                m.result_ids.forEach(function (s) {
                    m[s] = Math.round(current_rank_data[s] + m[s]);
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
                        m[s] += Math.ceil(m.unit_parameter["equipment_data"][eq][s]
                            + m.unit_parameter["equipment_enhance"][eq][s]
                            *et);
                    });
                });
            }

            // apply love status
            if (m.love > 1) {
                for (let i=2; i <= m.love; i++) {
                    let love_status = m.unit_parameter["love_table"][i - 2];
                    Object.keys(love_status).forEach(function (s) {
                        m[s] += love_status[s];
                    });
                }
            }
            return true;
        }
    }

}