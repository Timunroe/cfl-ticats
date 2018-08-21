function build_options(new_list, old_list, identifier, menu_kind) {
    // new_list: new options for next menu
    // old_list: current selection in next menu
    // db_list: values currently in db for asset
    // menu_kind: categories, topics or tags
    console.log("New list is:", new_list);
    console.log("Old list is:", old_list);
    var html = [];
    html = new_list.map((val) => {
        if (old_list.includes(val)) {
            console.log("current selection");
            return '<option value="' + identifier + '__' + menu_kind + '_user__' + val + '" selected>' + val + "</option>";
        } else {
            console.log("new selection");
            return '<option value="' + identifier + '__' + menu_kind + '_user__' + val + '">' + val + "</option>";
        }
    });
    console.log("HTML is: ", html);
    return html.join("");
}

function findProp(obj, key, out) {
    var i,
        proto = Object.prototype,
        ts = proto.toString,
        hasOwn = proto.hasOwnProperty.bind(obj);

    if ("[object Array]" !== ts.call(out)) out = [];

    for (i in obj) {
        if (hasOwn(i)) {
            if (i === key) {
                out.push(obj[i]);
            } else if (
                "[object Array]" === ts.call(obj[i]) ||
                "[object Object]" === ts.call(obj[i])
            ) {
                findProp(obj[i], key, out);
            }
        }
    }
    return out;
}

$(document).ready(function () {
    $(".test").select2(); // initialize

    var taxonomy = {
        News: {
            Municipal_Election: {
                mayor: ["eisenberger", "graydon"],
                wards: ["ward_1", "ward_2"]
            }
        },
        Opinion: {
            Column: {
                col: [""]
            },
            Commentary: {
                comm: [""]
            }
        },
        Sports: {
            Basketball: {
                NBA: ['Raptors'],
            },
            Baseball: {
                MLB: ['Jays'] // playoffs 'ALCS', 'ALDS', 'NLCS', 'NLDS', 'Wildcard'
            },

            Football: {
                CFL: ["Ticats"], // playoffs "East semifinal", "East final", "West semifinal", "West final",
                NFL: ["Bills"], // playoffs "Wildcard", "Division", "Conference"
                NCAA: ["BCS"],
                USPORTS: ['McMaster'] // playoffs
            },
            Golf: {
                PGA: [],
                LPGA: [],
                Champions: [],
            },
            Hockey: {
                NHL: ["Leafs", "Sabres"],
                OHL: ["Bulldogs", "Rangers", "Storm"],
                AHL: ["Marlies"]
            },
            Soccer: {
                MLS: ['TFC'],
                EPL: [],
                WorldCup: [],
            },
            Tennis: {
                ATP: [],
                WTA: []
            },
            Auto: {
                F1: [],
                Indy: [],
                NASCAR: [],
            }
        }
    };

    var nextUp = {
        sections: "categories",
        categories: "topics",
        topics: "tags"
    };

    $(".test").change(function () {
        var nextMenuOptions = [];
        // NEED TO KEEP ORIGINAL SELECTED VALUES AS PAGE BUILT WITH
        // Get the id, type of this module
        var menuID = String($(this).attr("id"));
        var string_parts = menuID.split("__");
        var assetID = string_parts[0];
        // console.log("Asset is: ", assetID);
        var menuKind = string_parts[1];
        if (menuKind != 'tags') {
            // get the kind of the next menu
            var nextMenuKind = nextUp[menuKind];
            // Get the selection in this module
            var menuSelection = $(this).val();
            // Then get the selector for the next menu in this module
            var nextMenuID = "#" + assetID + "__" + nextUp[menuKind];
            console.log("Next Menu ID is: ", nextMenuID);
            // Get the selection for the next menu in this module
            var nextMenuSelection = $(nextMenuID).val().map(function (value, index) {
                return ((value.split("__"))[2]).replace('_user', '');
            });
            console.log("nexMenuSelection is:", nextMenuSelection);
            // Calculate the possible options available for next menu
            // while re-selecting the current selection
            $.each(menuSelection, function (index, value) {
                console.log("Value is: ", value);
                value = (value.split("__"))[2]
                var temp = findProp(taxonomy, value);
                console.log(temp);
                if (menuKind == "topics") {
                    var nextMenuItems = temp[0];
                } else {
                    var nextMenuItems = Object.keys(temp[0]);
                }
                $.each(nextMenuItems, function (index, value) {
                    nextMenuOptions.push(value);
                }); // end inner each
            }); // end outer each
            // console.log("Child list is: ", nextMenuOptions);
            var html = build_options(
                nextMenuOptions,
                nextMenuSelection,
                assetID,
                nextMenuKind
            );
            console.log("HTML is: ", html);
            $(nextMenuID).html(html);
        }
    }); // end change
    $(".test").trigger('change');
}); // end ready function