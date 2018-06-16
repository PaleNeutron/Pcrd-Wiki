"use strict";

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var UnitDataModel = function () {
    function UnitDataModel() {
        _classCallCheck(this, UnitDataModel);

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

    _createClass(UnitDataModel, [{
        key: "get_input",
        value: function get_input(level, rank, rarity, love) {
            this.level = level;
            this.rank = rank;
            this.rarity = rarity;
            this.love = love;

            if (isNaN(this.level) || isNaN(this.rank) || isNaN(this.rarity) || isNaN(this.love)) {
                return false;
            }

            return true;
        }
    }, {
        key: "calc",
        value: function calc(level, rank, rarity, love) {
            var _this = this;

            if (!(Object.keys(this.unit_parameter).length === 0 && this.unit_parameter.constructor === Object)) {
                var _ret = function () {
                    if (!_this.get_input(level, rank, rarity, love)) {
                        return {
                            v: false
                        };
                    }
                    var m = _this;

                    // prepare parameters
                    var current_param = _this.unit_parameter["unit_data"][_this.rarity - 1];
                    var l = _this.level + _this.rank;

                    // apply level growth
                    _this.result_ids.forEach(function (tag) {
                        if (tag in current_param) {
                            var base = current_param[tag];
                            // since def is escaped to def_field but def_growth not escaped to def_field_growth
                            var growth_tag = (tag + "_growth").replace("_field", "");
                            var growth = 0;
                            if (growth_tag in current_param) {
                                growth = current_param[growth_tag];
                            }
                            m[tag] = base + growth * l;
                        }
                    });

                    // get rank data
                    if (m.rank > 1) {
                        var current_rank_data = m.unit_parameter["unit_rank_data"][m.rank - 2];
                        m.result_ids.forEach(function (s) {
                            m[s] = Math.round(current_rank_data[s] + m[s]);
                        });
                    }

                    // get equipment data
                    if (m.rank > 1) {
                        var current_equipments_data = m.unit_parameter["unit_promotion_data"][m.rank - 1];
                        current_equipments_data.forEach(function (eq) {
                            if (eq === 999999) return;
                            var pl = m.unit_parameter["equipment_enhance"][eq]["promotion_level"];
                            var et = m.unit_parameter["enhance_table"][pl];
                            m.result_ids.forEach(function (s) {
                                m[s] += Math.ceil(m.unit_parameter["equipment_data"][eq][s] + m.unit_parameter["equipment_enhance"][eq][s] * et);
                            });
                        });
                    }

                    // apply love status
                    if (m.love > 1) {
                        var _loop = function _loop(i) {
                            var love_status = m.unit_parameter["love_table"][i - 2];
                            Object.keys(love_status).forEach(function (s) {
                                m[s] += love_status[s];
                            });
                        };

                        for (var i = 2; i <= m.love; i++) {
                            _loop(i);
                        }
                    }
                    return {
                        v: true
                    };
                }();

                if ((typeof _ret === "undefined" ? "undefined" : _typeof(_ret)) === "object") return _ret.v;
            }
        }
    }]);

    return UnitDataModel;
}();