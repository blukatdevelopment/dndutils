/*##############################################################################
#                    ______ _                                                  #
#                    |  _  (_)                                                 #
#                    | | | |_  ___ ___                                         #
#                    | | | | |/ __/ _ \                                        #
#                    | |/ /| | (_|  __/                                        #
#                    |___/ |_|\___\___|                                        #
#                                                                              #
##############################################################################*/
if(!actor) return;

function generate_roll_html(roll, purpose = false){
    let msg = "";
    msg += `<table border="1">`;
    msg += "<tbody>";
    if(purpose){
        msg += `<tr><td display="inline-block"><b>${purpose}</b></td></tr>`;
    }
    msg += `<tr><td>Formula: ${roll._formula}</td></tr>`;
    result_text_list = []
    for(i in roll.terms[0].results){
        let result = roll.terms[0].results[i];
        let result_text = result.discarded ? `<s>${result.result}</s>` : `${result.result}`;
        if(typeof result.result !== 'undefined'){
            result_text_list.push(result_text);    
        }
    }
    total_result_text = result_text_list.join(",");

    msg += `<tr><td display="inline-block">Dice: ${total_result_text}</td></tr>`;
    msg += `<tr><td>Total: ${roll._total}</td></tr>`;
    msg += "</tbody>";
    return msg;
}

function roll(formula){
    return new Roll(formula).roll(async=false);
}

function roll_and_display(formula, purpose){
    let roll_result = roll(formula);
    let html = generate_roll_html(roll_result, purpose);
    ChatMessage.create({content: html});
}

/*##############################################################################
#        ___       _              ______      _                                #
#       / _ \     | |             |  _  \    | |                               #
#      / /_\ \ ___| |_ ___  _ __  | | | |__ _| |_ __ _                         #
#      |  _  |/ __| __/ _ \| '__| | | | / _` | __/ _` |                        #
#      | | | | (__| || (_) | |    | |/ / (_| | || (_| |                        #
#      \_| |_/\___|\__\___/|_|    |___/ \__,_|\__\__,_|                        #
#                                                                              #
##############################################################################*/

const ATHLETICS = "athletics",
ACROBATICS = "acrobatics",
SLEIGHT_OF_HAND = "sleight of hand",
STEALTH = "stealth",
ARCANA = "arcana",
HISTORY = "history",
INVESTIGATION = "investigation",
NATURE = "nature",
RELIGION = "religion",
ANIMAL_HANDLING = "animal handling",
INSIGHT = "insight",
MEDICINE = "medicine",
PERCEPTION = "perception",
SURVIVAL = "survival",
DECEPTION = "deception",
INTIMIDATION = "intimidation",
PERFORMANCE = "performance",
PERSUASION = "persuasion";

const STRENGTH = "strength",
DEXTERITY = "dexterity",
CONSTITUTION = "constitution",
INTELLIGENCE = "intelligence",
WISDOM = "wisdom",
CHARISMA = "charisma";

const STRENGTH_MOD = "strength_mod",
DEXTERITY_MOD = "dexterity_mod",
CONSTITUTION_MOD = "constitution_mod",
INTELLIGENCE_MOD = "intelligence_mod",
WISDOM_MOD = "wisdom_mod",
CHARISMA_MOD = "charisma_mod";

const XP = "xp",
AC = "ac",
CLASS = "class",
SIZE = "size",
LINEAGE = "lineage",
SPEED = "speed",
BACKGROUND = "background",
HIT_DICE = "hit dice",
PROF_BONUS = "prof bonus",
UNUSED = "unused";

const ARMOR_PROFS = "armor_profs",
WEAPON_PROFS = "weapon_profs",
TOOL_PROFS = "tool_profs",
LANGUAGES = "languages",
SKILL_PROFS = "skill_profs",
SAVE_PROFS = "saving throws";

const ABILITIES = [
    STRENGTH,
    DEXTERITY,
    CONSTITUTION,
    INTELLIGENCE,
    WISDOM,
    CHARISMA
];

const NAME = "name";

const SKILL_ABILITIES_MAP = {
    [ATHLETICS]: STRENGTH,
    [ACROBATICS]: DEXTERITY,
    [SLEIGHT_OF_HAND]: DEXTERITY,
    [STEALTH]: DEXTERITY,
    [ARCANA]: INTELLIGENCE,
    [HISTORY]: INTELLIGENCE,
    [INVESTIGATION]: INTELLIGENCE,
    [NATURE]: INTELLIGENCE,
    [RELIGION]: INTELLIGENCE,
    [ANIMAL_HANDLING]: WISDOM,
    [INSIGHT]: WISDOM,
    [MEDICINE]: WISDOM,
    [PERCEPTION]: WISDOM,
    [SURVIVAL]: WISDOM,
    [DECEPTION]: CHARISMA,
    [INTIMIDATION]: CHARISMA,
    [PERFORMANCE]: CHARISMA,
    [PERSUASION]: CHARISMA
};

const STATS_TABLE_FIELDS = [
    [UNUSED, UNUSED, UNUSED, UNUSED, XP],
    [UNUSED, STRENGTH, STRENGTH_MOD, AC, CLASS],
    [UNUSED, DEXTERITY, DEXTERITY_MOD, SIZE, LINEAGE],
    [UNUSED, CONSTITUTION, CONSTITUTION_MOD, SPEED, BACKGROUND],
    [UNUSED, INTELLIGENCE, INTELLIGENCE_MOD, UNUSED, HIT_DICE],
    [UNUSED, WISDOM, WISDOM_MOD, UNUSED, PROF_BONUS],
    [UNUSED, CHARISMA, CHARISMA_MOD, UNUSED, UNUSED]
];

const PROFICIENCIES_TABLE_FIELDS = [
    [UNUSED, ARMOR_PROFS],
    [UNUSED, WEAPON_PROFS],
    [UNUSED, TOOL_PROFS],
    [UNUSED, LANGUAGES],
    [UNUSED, SKILL_PROFS],
    [UNUSED, SAVE_PROFS]
];

const STATS_TABLE = 0,
PROFICIENCIES_TABLE = 1,
ATTACK_TABLE = 2;

function parse_stats_from_biography(){
    if(!actor) return;
    let bio = actor.data.data.biography;
    let tables = parse_table_data(bio);
    let stats = build_stats_object(tables);
    unpack_list_fields(stats);

    stats[NAME] = actor.data.name;
    
    return stats;
}

function unpack_list_fields(stats){
    stats[SKILL_PROFS] = stats[SKILL_PROFS].replace(" ", "").split(",");
    stats[SAVE_PROFS] = stats[SAVE_PROFS].replace(" ", "").split(",");
}

/* Returns a 2D string array of table contents*/
function parse_table_data(bio){
    let tables_text = bio.match(/<tbody[\S\s]*?>([\S\s]*?)<\/tbody>/g);
    return [
        parse_table(tables_text[STATS_TABLE]),
        parse_table(tables_text[PROFICIENCIES_TABLE])
    ];
}

/* Returns a 2D string array from html representing a table*/
function parse_table(table_text){
    let table = [];
    let rows_text = table_text.match(/<tr[\S\s]*?>([\S\s]*?)<\/tr>/g);
    for(i in rows_text){
        let row_text = rows_text[i];
        if(typeof row_text !== "string") continue;
        let columns_text = row_text.match(/<td[\S\s]*?>([\S\s]*?)<\/td>/g);
        let columns = [];
        for(j in columns_text){
            let column_text = columns_text[j];
            if(typeof column_text !== "string") continue;
            let column_value = column_text.match(/<td[\S\s]*?>([\S\s]*?)<\/td>/)[1];
            columns.push(column_value);
        }
        table.push(columns);

    }
    return table;
}

/* converts two 2D arrays for field and value into an object. */
function build_stats_object(values_table){
    let stats_table = merge_table_fields(STATS_TABLE_FIELDS, values_table[STATS_TABLE]);
    let profs_table = merge_table_fields(PROFICIENCIES_TABLE_FIELDS, values_table[PROFICIENCIES_TABLE]);
    let stats_obj = {
        ...stats_table,
        ...profs_table
    };

    return stats_obj;
}

function merge_table_fields(fields_table, values_table){
    let stats_obj = {};
    let row_length = fields_table.length;
    let column_length = fields_table[0].length;

    for(let row = 0; row < row_length; row++){
        for(let column = 0; column < column_length; column++){
            let field = fields_table[row][column];
            let value = values_table[row][column];
            stats_obj[field] = value;
        }
    }
    return stats_obj;
}

function get_proficiency(skill){
    for(i in STATS[SKILL_PROFS]){
        let skill_prof = STATS[SKILL_PROFS][i];
        if(typeof skill_prof != "string"){
            skill_prof = "";
        }
        if(skill.toLowerCase() === skill_prof.toLowerCase()){
            return true;
        }
    }
    return false;
}

function get_save_proficiency(ability){
    for(i in STATS[SAVE_PROFS]){
        let save_prof = STATS[SAVE_PROFS][i];
        if(typeof save_prof != "string"){
            save_prof = "";
        }
        if(ability.toLowerCase() === save_prof.toLowerCase()){
            return true;
        }
    }
    return false;
}

/*##############################################################################
#       ______ _       _                                                       #
#       |  _  (_)     | |                                                      #
#       | | | |_  __ _| | ___   __ _                                           #
#       | | | | |/ _` | |/ _ \ / _` |                                          #
#       | |/ /| | (_| | | (_) | (_| |                                          #
#       |___/ |_|\__,_|_|\___/ \__, |                                          #
#                               __/ |                                          #
#                              |___/                                           #
##############################################################################*/

function save_dialog(){
    new Dialog({
        title: "Saving Throw",
        content: "content",
        buttons: build_save_buttons()
    }).render(true);
}

function build_save_buttons(){
    let buttons = {};
    for(i in ABILITIES){
        let ability = ABILITIES[i];
        if(typeof ability === "string"){
            buttons[ability] = build_save_button(ability);
        }
    }
    return buttons;
}

function build_save_button(ability){
    let ability_mod = parseInt(STATS[ability+"_mod"]);
    if(isNaN(ability_mod)){
        ability_mod = 0;
    }
    let proficiency_bonus = STATS[PROF_BONUS];
    proficiency_bonus = parseInt(proficiency_bonus.match(/([+-]?[0-9]+)/)[0]);
    let proficiency = get_save_proficiency(ability);

    if(isNaN(proficiency_bonus) || !proficiency){
        proficiency_bonus = 0;
    }
    let modifier = ability_mod + proficiency_bonus;
    modifier = modifier < 0 ? modifier : `+${modifier}`;
    let formula = `1d20${modifier}`;

    return {
        label: ability,
        callback: async (html) => {
            roll_and_display(formula, STATS[NAME] + " made a(n) " + ability + " saving throw");
        }
    };
}


/*##############################################################################
#       ___  ___      _                                                        #
#       |  \/  |     (_)                                                       #
#       | .  . | __ _ _ _ __                                                   #
#       | |\/| |/ _` | | '_ \                                                  #
#       | |  | | (_| | | | | |                                                 #
#       \_|  |_/\__,_|_|_| |_|                                                 #
#                                                                              #
##############################################################################*/

const STATS = parse_stats_from_biography();

save_dialog();