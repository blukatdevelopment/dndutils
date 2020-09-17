// JQuery required.
// Characters page scripts
var myCharacters = {};

$(document).ready(function(){
    myCharacters.characters = getCharacterData();
    viewCharacter(myCharacters.characters[0].character_id);
});

function getCharacterData(){
    var characters = [];
    $(".character_data").each(function(){
        var element = $(this);
        var raw = element.text();
        var data = JSON.parse(raw);
        characters.push(data);
    }); 
    return characters;
}

function getCharacterById(character_id){
    let ret = null;
    myCharacters.characters.forEach(function(character){
        if(character.character_id == character_id){
            console.log(`Found character ${character_id} `);
            ret = character;
        }
    });
    return ret;
}

function viewCharacter(id){
    let character = getCharacterById(id);

    if(!character){
        return;
    }

    getStringFields().forEach(function(field){
        let val = character[field];
        $(`#${field}`).val(character[field]);
    });

    get_list_fields().forEach(function(field){
        let table = $(`#${field}_list`);
        $(`#${field}_list tr`).remove();

        let header = getListFieldHeader(field);
        table.append($(`<tr><th>${header}</th></tr>`));


        let vals = character[field] || [];


        vals.forEach(function(val){
            let input = $('<input type="text">');
            input.val(val);
            let tr = $('<tr></tr>');
            let td = $('<td></td>');

            td.append(input);
            tr.append(td);
            table.append(tr);
        });
    });

    getCheckboxFields().forEach(function(field){
        let val = character[field];
        $(`#${field}`).prop('checked', val);
    });
}

function get_list_fields(){
    return ["known_spells",
    "inventory",
    "features_and_traits",
    "proficiencies"];
}

function getListFieldHeader(fieldName){
    switch(fieldName){
        case "known_spells":
            return "Known Spells";
            break;
        case "inventory":
            return "Equipment";
            break;
        case "features_and_traits":
            return "Features and Traits";
            break;
        case "proficiencies":
            return "Proficiencies";
            break;
    }
    return "No header found";
}

function getCheckboxFields(){
    return[
    // Saving throw proficiencies
    "strength_save_prof",
    "dexterity_save_prof",
    "constitution_save_prof",
    "intelligence_save_prof",
    "wisdom_save_prof",
    "charisma_save_prof",
    // skill proficiencies
    "acrobatics_prof",
    "animal_handling_prof",
    "arcana_prof",
    "athletics_prof",
    "deception_prof",
    "history_prof",
    "insight_prof",
    "intimidation_prof",
    "investigation_prof",
    "medicine_prof",
    "nature_prof",
    "perception_prof",
    "performance_prof",
    "persuasion_prof",
    "religion_prof",
    "sleight_of_hand_prof",
    "stealth_prof",
    "survival_prof"];
}

function getStringFields(){
    return [
    "user_id",
    "character_id",
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
    "strength_mod",
    "dexterity_mod",
    "constitution_mod",
    "intelligence_mod",
    "wisdom_mod",
    "charisma_mod",
    "strength_save",
    "dexterity_save",
    "constitution_save",
    "intelligence_save",
    "wisdom_save",
    "charisma_save",
    "strength_save_prof",
    "dexterity_save_prof",
    "constitution_save_prof",
    "intelligence_save_prof",
    "wisdom_save_prof",
    "charisma_save_prof",
    "acrobatics",
    "animal_handling",
    "arcana",
    "athletics",
    "deception",
    "history",
    "insight",
    "intimidation",
    "investigation",
    "medicine",
    "nature",
    "perception",
    "performance",
    "persuasion",
    "religion",
    "sleight_of_hand",
    "stealth",
    "survival",
    "acrobatics_prof",
    "animal_handling_prof",
    "arcana_prof",
    "athletics_prof",
    "deception_prof",
    "history_prof",
    "insight_prof",
    "intimidation_prof",
    "investigation_prof",
    "medicine_prof",
    "nature_prof",
    "perception_prof",
    "performance_prof",
    "persuasion_prof",
    "religion_prof",
    "sleight_of_hand_prof",
    "stealth_prof",
    "survival_prof",
    "biography",
    "proficiency_bonus",
    "character_name",
    "class_and_level",
    "background",
    "player_name",
    "race",
    "alignment",
    "experience_points",
    "armor_class",
    "initiative",
    "speed",
    "hit_point_maximum",
    "hit_dice",
    "attack_1",
    "attack_bonus_1",
    "attack_damage_1",
    "attack_2",
    "attack_bonus_2",
    "attack_damage_2",
    "attack_3",
    "attack_bonus_3",
    "attack_damage_3",
    "spell_dc",
    "spell_attack_bonus",
    "spellslots_1st",
    "spellslots_2nd",
    "spellslots_3rd",
    "spellslots_4th",
    "spellslots_5th",
    "spellslots_6th",
    "spellslots_7th",
    "spellslots_8th",
    "spellslots_9th",
    "gold_pieces"];
}

function getImmutableFields(){
    return [
    "user_id",
    "character_id",
    "ability_scores_array"
    ];
}