// JQuery required.
// Characters page scripts
var myCharacters = {};

$(document).ready(function(){
    myCharacters.characters = getCharacterData();
    populateCharacters();
    setUpJsonButtons();
});

function setUpJsonButtons(){
    $("#get_json_button").click(function(){
        let character = getCharacterById(getActiveCharacterId());
        $("#json_area").text(JSON.stringify(character));
    });

    $("#load_json_button").click(function(){
        try{
            let characterJson = $("#json_area").val();
            let data = JSON.parse(characterJson);
            setCharacterById(getActiveCharacterId(), data);
            viewCharacter(getActiveCharacterId());
        }
        catch(err){
            alert("Could not parse JSON" + err);
        }
    });
}

function getActiveCharacterId(){
    return myCharacters.activeCharacter;
}

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

function populateCharacters(){
    var charList = $("<ul></ul>");
    for(let i = 0; i < 3; i++){
        let character = myCharacters.characters.find( chrctr => chrctr.character_id == i);
        if(character){
            var listElement = $(`<li id="character${i}"></li>`);
            listElement.append(generateCharacterView(character));
            charList.append(listElement);
        }
        else{
            var listElement = $(`<li id="character${i}"></li>`);
            listElement.append(newCharacterButton(i));
            charList.append(listElement);
        }
    }
    $("#root").append(charList);
}

function generateCharacterView(character){
    let user_id = $('#user_id').text().trim();
    let id = character.character_id;
    let name = character.character_name == "" ? "Unnamed character": character.character_name;
    let abilities = JSON.stringify(character.ability_scores_array);
    let li = $(`<li><p>Character ${id}: ${name} Abilities:${abilities}</p></li>`);
    li.append(makeViewButton(id));
    li.append($(`<a href="/character/view/${user_id}/${id}/"><button>View On separate Page.</button></a>`));
    return li;
}

function setCharacterById(character_id, character){
    let oldCharacter = getCharacterById(character_id);
    if(oldCharacter){
        getImmutableFields().forEach(function(field){
            let oldVal = oldCharacter[field];
            let newVal = character[field];
            character[field] = oldVal;
            newVal = character[field];
        });
        removeCharacterById(character_id);
    }
    myCharacters.characters.push(character);
}

function removeCharacterById(id){
    let index = -1;
    for(let i = 0; i < myCharacters.characters.length; i++){
        let character = myCharacters.characters[i];
        if(character.character_id == id){
            index = i;
        }
    }
    if(index != -1){
        myCharacters.characters.splice(index, 1);
    }
}

function getCharacterById(character_id){
    let ret = null;
    myCharacters.characters.forEach(function(character){
        if(character.character_id == character_id){
            ret = character;
        }
    });
    return ret;
}

function makeSaveButton(id){
    let saveButton = $(`<button id="save_${id}"">Save</button>`);
    saveButton.click(function(){
       saveCharacter(id);
    });
    return saveButton;
}

function makeViewButton(id){
    let viewButton = $(`<button id="view_${id}"">View Here</button>`);
    viewButton.click(function(){
       viewCharacter(id); 
    });
    return viewButton;
}

function resetViewButtons(){
    for(let i = 0; i < 3; i++){
        let editButton = $(`#save_${i}`);
        if(editButton){
            editButton.replaceWith(makeViewButton(i));
        }
    }
}

function viewCharacter(id){
    let character = getCharacterById(id);
    if(!character){
        console.log("Could not find character " + id);
        return;
    }

    resetViewButtons();

    $(`#view_${id}`).replaceWith(makeSaveButton(id));

    getStringFields().forEach(function(field){
        let val = character[field];
        $(`#${field}`).val(character[field]);
    });

    get_list_fields().forEach(function(field){
        let table = $(`#${field}_list`);
        $(`#${field}_list tr`).remove();

        
        get_list_header(table, character, field);

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

    myCharacters.activeCharacter = id;
}

function get_list_header(table, character, field, vals){
    
    let tableRow = $(`<tr>/tr>`);
    let headerTable = $(`<table></table>`);

    let headerText = getListFieldHeader(field);
    let headerLabel = $(`<th>${headerText}</th><`);
    
    tableRow.append(headerLabel)

    let headerPlusData = $(`<td></td>`);
    let headerPlusButton = $('<button class="plus">+</button>');
    headerPlusButton.click(function(){
        addListItem(field);
    });
    headerPlusData.append(headerPlusButton);
    tableRow.append(headerPlusData);

    let headerMinusData = $(`<td></td>`);
    let headerMinusButton = $('<button class="minus">-</button>');
    headerMinusButton.click(function(){
        removeListItem(field);
    });
    headerPlusData.append(headerMinusButton);
    tableRow.append(headerMinusData);

    headerTable.append(tableRow);

    table.prepend(headerTable);
}

function removeListItem(fieldName){
    let table = $(`#${fieldName}_list`); 
    let rows = $(`tr`, table);
    if(rows.length > 1){
        rows.last().remove();
    }
}

function addListItem(fieldName){
    let table = $(`#${fieldName}_list`);
    let row = $('<tr><td><input type="text"></input></td></tr>');
    table.append(row);
}

function saveCharacter(id){

    let character = getCharacterById(id);
    $(`#save_${id}`).replaceWith(makeViewButton(id));

    getStringFields().forEach(function(field){
        let val = $(`#${field}`).val();
        if(val){
            character[field] = val;
        }
    });

    get_list_fields().forEach(function(field){
        character[field] = [];
        $(`#${field}_list :input`).each(function(){
            let val = $(this).val();
            if(val && val != ''){
                character[field].push(val);    
            }
        });
    });

    getCheckboxFields().forEach(function(field){
        character[field] = $(`#${field}`).is(":checked");
    });

    setCharacterById(id, character);

    updateCharacter(id);
}

function newCharacterButton(i){
    var button = $("<button>Create Character</button>");
    button.click(function(){
        requestCharacter(i);
    });
    return button;
}

function updateRequestedCharacter(raw){
    let character = JSON.parse(raw);
    setCharacterById(character.character_id, character);
    viewCharacter(character.character_id);
    
    let id = character.character_id;
    $(`#character${id}`).replaceWith(generateCharacterView(character));   
}

function updateCharacter(id){
    let data = JSON.stringify({character: getCharacterById(id)});
    $.ajax({
        type: 'POST',
        url: "/update_character",
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function(resp) {
            updateRequestedCharacter(resp.character)
        },
        error: function(error){
          if(error.responseJSON){
            var responseJSON = error.responseJSON;
            console.log(error);
            var msg = responseJSON.msg;
            $("#response_div").text(msg);
          }
          else{
            $("#response_div").text("Unexpected error. Please try again later."); 
          }
        }
    });
}

function requestCharacter(i){

    $.ajax({
        type: 'POST',
        url: "/request_character",
        data: JSON.stringify({character_id: i}),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function(resp) {
            updateRequestedCharacter(resp.character)
        },
        error: function(error){
          if(error.responseJSON){
            var responseJSON = error.responseJSON;
            console.log(error);
            var msg = responseJSON.msg;
            $("#response_div").text(msg);
          }
          else{
            $("#response_div").text("Unexpected error. Please try again later."); 
          }
        }
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