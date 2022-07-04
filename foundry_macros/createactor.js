
/*
    Stats Constants
*/
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
const SKILLS = [
    ATHLETICS,
    ACROBATICS,
    SLEIGHT_OF_HAND,
    STEALTH,
    ARCANA,
    HISTORY,
    INVESTIGATION,
    NATURE,
    RELIGION,
    ANIMAL_HANDLING,
    INSIGHT,
    MEDICINE,
    PERCEPTION,
    SURVIVAL,
    DECEPTION,
    INTIMIDATION,
    PERFORMANCE,
    PERSUASION
];

const STRENGTH = "strength",
DEXTERITY = "dexterity",
CONSTITUTION = "constitution",
INTELLIGENCE = "intelligence",
WISDOM = "wisdom",
CHARISMA = "charisma";

const STRENGTH_MOD = "strength mod",
DEXTERITY_MOD = "dexterity mod",
CONSTITUTION_MOD = "constitution mod",
INTELLIGENCE_MOD = "intelligence mod",
WISDOM_MOD = "wisdom mod",
CHARISMA_MOD = "charisma mod";

const STRENGTH_SAVE = "strength save",
DEXTERITY_SAVE = "dexterity save",
CONSTITUTION_SAVE = "constitution save",
INTELLIGENCE_SAVE = "intelligence save",
WISDOM_SAVE = "wisdom save",
CHARISMA_SAVE = "charisma save";

const SAVES = [STRENGTH_SAVE,
DEXTERITY_SAVE,
CONSTITUTION_SAVE,
INTELLIGENCE_SAVE,
WISDOM_SAVE,
CHARISMA_SAVE];

const XP = "xp",
AC = "ac",
CLASS = "class",
SIZE = "size",
LINEAGE = "lineage",
SPEED = "speed",
BACKGROUND = "background",
HIT_DICE = "hit dice",
PROF_BONUS = "prof bonus",
FEATS = "feats",
DESCRIPTION = "description",
LEVEL = "level",
UNUSED = "unused";

const LIGHT_ARMOR = "light armor",
MEDIUM_ARMOR = "medium armor",
HEAVY_ARMOR = "heavy armor",
SHIELDS = "shields";
const ARMORS = [LIGHT_ARMOR, MEDIUM_ARMOR, HEAVY_ARMOR, SHIELDS];

const ARMOR_PROFS = "armor_profs",
WEAPON_PROFS = "weapon_profs",
TOOL_PROFS = "tool_profs",
LANGUAGE_PROFS = "languages",
SKILL_PROFS = "skill_profs",
SAVE_PROFS = "saving throws";

const COMMON = "common",
ELVISH = "elvish",
GNOMISH = "gnomish",
DWARVEN = "dwarven",
BEAST_TONGUE = "beast tongue",
ONE_OTHER = "one other";

const LANGUAGES = [COMMON, ELVISH, GNOMISH, DWARVEN, BEAST_TONGUE, ONE_OTHER];

const ABILITIES = [
    STRENGTH,
    DEXTERITY,
    CONSTITUTION,
    INTELLIGENCE,
    WISDOM,
    CHARISMA
];

const ATTACKS = "attacks",
ATTACK_NAME = "Attack",
TO_HIT = "To Hit",
ATTACK_DAMAGE = "Damage";

const ATTACK_FIELDS = [
    ATTACK_NAME,
    TO_HIT,
    ATTACK_DAMAGE
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
FEATS_TABLE = 3;

/*
    Unchained Worlds Data
*/

// Weapon names
const UNARMED = "unarmed",
CLUB = "club",
DAGGER = "dagger",
GREATCLUB = "greatclub",
HANDAXE = "handaxe",
JAVELIN = "javelin",
LIGHT_HAMMER = "light hammer",
MACE = "mace",
QUARTERSTAFF = "quarterstaff",
SICKLE = "sickle",
SPEAR = "spear",
LIGHT_CROSSBOW = "light crossbow",
DART = "dart",
SHORTBOW = "shortbow",
SLING = "sling",
BATTLEAXE = "battleaxe",
FLAIL = "flail",
GLAIVE = "glaive",
GREATAXE = "greataxe",
GREATSWORD = "greatsword",
HALBERD = "halberd",
LANCE = "lance",
LONGSWORD = "longsword",
MAUL = "maul",
MORNINGSTAR = "morningstar",
PIKE = "pike",
RAPIER = "rapier",
SCIMITAR = "scimitar",
SHORTSWORD = "shortsword",
TRIDENT = "trident",
WAR_PICK = "war pick",
WARHAMMER = "warhammer",
WHIP = "whip",
BLOWGUN = "blowgun",
HAND_CROSSBOW = "hand crossbow",
HEAVY_CROSSBOW = "heavy crossbow",
LONGBOW = "longbow",
NET = "net";

// Item packs
const EXPLORER_PACK = "Explorer's Pack",
PEASANT_PACK = "Peasant's Pack",
TINKER_PACK = "Tinker's Pack",
NOBLE_PACK = "Noble's Pack",
SCHOLAR_PACK = "Scholar's Pack",
GUILDMEMBER_PACK = "Guildmember's Pack",
ARTIST_PACK = "Artist's Pack",
PRIEST_PACK = "Priest's Pack",
BURGLAR_PACK = "Burglar's Pack";
const PACKS = new Map([
    [EXPLORER_PACK, []],
    [PEASANT_PACK, ["backpack", "common clothes", "5lb sack of wheat", "pouch of 5sp"]],
    [TINKER_PACK, []],
    [NOBLE_PACK, []],
    [SCHOLAR_PACK, []],
    [GUILDMEMBER_PACK, []],
    [ARTIST_PACK, []],
    [PRIEST_PACK, []],
    [BURGLAR_PACK, []]
]);

// Weapon properties
const WEAPON_PROPERTIES = "weapon properties",
AMMUNITION = "ammunition",
FINESSE = "finesse",
HEAVY = "heavy",
LIGHT = "light",
LOADING = "loading",
RANGE = "range",
REACH = "reach",
SPECIAL = "special",
THROWN = "thrown",
TWO_HANDED = "two-handed",
VERSATILE = "versatile";

// Weapon Type
const WEAPON_TYPE = "weapon type",
NATURAL_WEAPON = "natural weapon",
MARTIAL_WEAPON = "martial weapon",
SIMPLE_WEAPON = "simple weapon";

// Damage types
const BLUDGEONING = "bludgeoning",
PIERCING = "piercing",
SLASHING = "slashing";

const INVENTORY = "inventory";

const WEAPONS = new Map([
    [UNARMED, {
        [ATTACK_DAMAGE]: "1",
        [WEAPON_PROPERTIES]: [],
        [WEAPON_TYPE]: NATURAL_WEAPON
    }],
    [CLUB, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [LIGHT],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [DAGGER, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [FINESSE, LIGHT, THROWN],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [GREATCLUB, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [TWO_HANDED],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [HANDAXE, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [LIGHT, THROWN],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [JAVELIN, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [THROWN],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [LIGHT_HAMMER, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [LIGHT, THROWN],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [MACE, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [QUARTERSTAFF, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [VERSATILE],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [SICKLE, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [LIGHT],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [SPEAR, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [THROWN, VERSATILE],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [LIGHT_CROSSBOW, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [AMMUNITION, TWO_HANDED],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [DART, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [FINESSE, THROWN],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [SHORTBOW, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [AMMUNITION, TWO_HANDED],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [SLING, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [AMMUNITION],
        [WEAPON_TYPE]: SIMPLE_WEAPON
    }],
    [BATTLEAXE, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [VERSATILE],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [FLAIL, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [GLAIVE, {
        [ATTACK_DAMAGE]: "1d10",
        [WEAPON_PROPERTIES]: [HEAVY, REACH, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [GREATAXE, {
        [ATTACK_DAMAGE]: "1d12",
        [WEAPON_PROPERTIES]: [HEAVY, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [GREATSWORD, {
        [ATTACK_DAMAGE]: "2d6",
        [WEAPON_PROPERTIES]: [HEAVY, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [HALBERD, {
        [ATTACK_DAMAGE]: "1d10",
        [WEAPON_PROPERTIES]: [HEAVY, REACH, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [LANCE, {
        [ATTACK_DAMAGE]: "1d12",
        [WEAPON_PROPERTIES]: [REACH, SPECIAL],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [LONGSWORD, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [VERSATILE],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [MAUL, {
        [ATTACK_DAMAGE]: "2d6",
        [WEAPON_PROPERTIES]: [HEAVY, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [MORNINGSTAR, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [PIKE, {
        [ATTACK_DAMAGE]: "1d10",
        [WEAPON_PROPERTIES]: [HEAVY, REACH, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [RAPIER, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [FINESSE],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [SCIMITAR, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [FINESSE, LIGHT],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [SHORTSWORD, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [FINESSE, LIGHT],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [TRIDENT, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [THROWN, VERSATILE],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [WAR_PICK, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [WARHAMMER, {
        [ATTACK_DAMAGE]: "1d8",
        [WEAPON_PROPERTIES]: [VERSATILE],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [WHIP, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [FINESSE, REACH],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [BLOWGUN, {
        [ATTACK_DAMAGE]: "1",
        [WEAPON_PROPERTIES]: [AMMUNITION, LOADING],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [HAND_CROSSBOW, {
        [ATTACK_DAMAGE]: "1d6",
        [WEAPON_PROPERTIES]: [AMMUNITION, LIGHT, LOADING],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [HEAVY_CROSSBOW, {
        [ATTACK_DAMAGE]: "1d10",
        [WEAPON_PROPERTIES]: [AMMUNITION, HEAVY, LOADING, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [LONGBOW, {
        [ATTACK_DAMAGE]: "1d4",
        [WEAPON_PROPERTIES]: [AMMUNITION, HEAVY, TWO_HANDED],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }],
    [NET, {
        [ATTACK_DAMAGE]: "0",
        [WEAPON_PROPERTIES]: [SPECIAL, THROWN],
        [WEAPON_TYPE]: MARTIAL_WEAPON
    }]
]);

const LINEAGES = new Map([
    ["soot", {
        strength: 2,
        wisdom: 1,
        languages: [COMMON],
        feats: [
            {
                name: "Apprenticeship",
                description: "During your childhood you worked as an apprentice to help pay the bills. You are proficient in one tool of your choice."
            },
            {
                name: "Conscript",
                description: "You were recruited and served a few months in the army before being returned. In that time you learned to wield a pole arm in formation. You are proficient with pikes.",
                requirements: {
                    strength: 15
                }
            }
        ]
    }]
]);

const BACKGROUNDS = new Map([
    ["farmer", {
        proficiencies: [SICKLE],
        items: [SICKLE, "chicken", PEASANT_PACK]
    }],
    ["rat catcher", {
        proficiencies: ["live trap"],
        items: ["live trap", PEASANT_PACK]
    }],
]);

const CLASSES = new Map([
    ["commoner", {
        feats: [],
        hit_die: "d4",
        skill_count: 2,
        SKILL_PROFS: [ ATHLETICS, INSIGHT, HISTORY, NATURE, RELIGION],
        equipment: [ "(5)torch", "waterskin", CLUB],
        [SAVE_PROFS]: [CONSTITUTION_SAVE]
    }]
]);


/*
    Dice
*/
async function rollTotal(formula){
    let roll = new Roll(formula)
    let result = await roll.roll();
    return result._total;
}

function hasWeaponProficiency(stats, weapon){
    let retVal = false;
    if(!WEAPON_PROFS in stats){
        stats[WEAPON_PROFS] = [];
    }
    stats[WEAPON_PROFS].forEach(prof => {
        if(prof === weapon){
            retVal = true;
        }
    });
    if(retVal){
        return retVal;
    }
    let weapon_stats = WEAPONS.get(weapon);
    if(weapon_stats[WEAPON_TYPE] in stats[WEAPON_PROFS]){
        return true;
    }
    if(weapon_stats[WEAPON_TYPE] === NATURAL_WEAPON){
        return true;
    }
    return false;
}

function getWeaponAbility(stats, weapon){
    let weapon_stats = WEAPONS.get(weapon);
    if(AMMUNITION in weapon_stats[WEAPON_PROPERTIES]){
        return DEXTERITY;
    }
    if(FINESSE in weapon_stats[WEAPON_PROPERTIES]){
        return stats[DEXTERITY] > stats[STRENGTH] ? DEXTERITY: STRENGTH;
    }
    return STRENGTH;
}

function getWeaponAttacks(stats, weapon){
    let attacks = [];
    let weapon_stats = WEAPONS.get(weapon);
    let proficiency = hasWeaponProficiency(stats, weapon);
    let ability = getWeaponAbility(stats, weapon);
    let ability_mod = getAbilityMod(stats[ability]);
    let attack_modifier = ability_mod;
    if(proficiency){
        attack_modifier += parseInt(stats[PROF_BONUS]);
    }
    let attack_damage = weapon_stats[ATTACK_DAMAGE];
    attack_damage += ability_mod < 0 ? ability_mod : "+" + ability_mod;
    attacks.push({
        [ATTACK_NAME]: weapon,
        [TO_HIT]: attack_modifier,
        [ATTACK_DAMAGE]: attack_damage
    });
    if(VERSATILE in weapon_stats[WEAPON_PROPERTIES]){
        attack_damage = versatileDamage(weapon_stats[ATTACK_DAMAGE])
        attack_damage += ability_mod < 0 ? ability_mod : "+" + ability_mod;
        attacks.push({
            [ATTACK_NAME]: weapon + "(versatile)",
            [TO_HIT]: attack_modifier,
            [ATTACK_DAMAGE]: attack_damage
        });
    }
    if(LIGHT in weapon_stats[WEAPON_PROPERTIES]){
        attack_damage = weapon_stats[ATTACK_DAMAGE];
        attacks.push({
            [ATTACK_NAME]: weapon + "(offhand)",
            [TO_HIT]: attack_modifier,
            [ATTACK_DAMAGE]: attack_damage
        });
    }
    return attacks;
}

function versatileDamage(damage){
    let size = parseInt(damage.split('d')[1]);
    return "1d"+size;
}

function getAbilityMod(abilityScore){
    let map = {
        0: -5,
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5
    }
    return map[abilityScore];
}

/*
    Generate actor stats
*/


function debugOpts(){
    let backgrounds = [ ...BACKGROUNDS.keys() ];
    let opts = {};
    opts[STRENGTH] = 10;
    opts[DEXTERITY] = 12;
    opts[CONSTITUTION] = 14;
    opts[INTELLIGENCE] = 16;
    opts[WISDOM] = 18;
    opts[CHARISMA] = 8;
    opts.roll_abilities = false;
    opts[CLASS] = "commoner";
    opts[NAME] = "John Smith";
    opts[LINEAGE] = "soot";
    opts[BACKGROUND] = backgrounds[Math.floor(Math.random() * backgrounds.length)];
    opts[SKILL_PROFS] = [ACROBATICS, DECEPTION];
    return opts;
}

async function getStats(opts){
    let stats = {};
    stats[SKILL_PROFS] = opts[SKILL_PROFS];
    stats[NAME] = opts[NAME];
    await applyAbilities(stats, opts);
    applyLineage(stats, opts);
    applyClass(stats, opts);
    applyBackground(stats, opts);
    return stats;
}


async function applyAbilities(stats, opts){
    if(opts.roll_abilities){
        // TODO: Async isn't populating before the mods are calculated
        ABILITIES.forEach(async (ability) => {
            stats[ability] = await rollTotal("4d6kh3");
        });
    }
    else{
        ABILITIES.forEach((ability) => {
            stats[ability] = opts[ability];
        });    
    }
    ABILITIES.forEach((ability) => {
        stats[ability + " mod"] = getAbilityMod(stats[ability]);
    });
}

function applyLineage(stats, opts){
    let lineage = LINEAGES.get(opts.lineage);
    if(typeof(lineage) === "undefined"){
        console.log("Lineage " + opts.lineage + " does not exist");
        return;
    }
    lineage.languages.forEach((language) => {
        apply_proficiency(stats, language);
    });
    ABILITIES.forEach((ability) => {
        let asi = lineage[ability];
        if(typeof(asi) !== "undefined"){
            stats[ability] += asi;
            stats[ability + "_mod"] = getAbilityMod(stats[ability]);
        }
        stats[SPEED] = typeof(lineage[SPEED]) === "undefined" ? "30ft" : lineage[SPEED];
        stats[SIZE] = typeof(lineage[SIZE]) === "undefined" ? "medium" : lineage[SIZE];
    });

    stats[LINEAGE] = opts.lineage;
    stats[FEATS] = [];
    lineage.feats.forEach((feat) => {
        if(isEligibleForFeat(stats, feat)){
            stats[FEATS].push({
                name: feat.name,
                description: feat.description
            });
        }
    });
}

function isEligibleForFeat(stats, feat){
    if(typeof(feat.requirements) === "undefined"){
        return true;
    }
    let isEligible = true;
    ABILITIES.forEach((ability) => {
        let requirement = feat.requirements[ability];
        if(typeof(requirement) !== "undefined" && requirement > stats[ability]){
            isEligible = false;
        }
    });
    return isEligible;
}

function applyClass(stats, opts){
    let _class = CLASSES.get(opts.class);
    if(typeof(_class) === "undefined"){
        console.log("Invalid class: " + opts.class);
        return;
    }
    stats[SAVE_PROFS] = [];
    _class[SAVE_PROFS].forEach( (prof) => {
        apply_proficiency(stats, prof);
    });
    stats[SKILL_PROFS] = [];
    opts[SKILL_PROFS].forEach((skill) => {
        apply_proficiency(stats, skill);
    });
    stats[CLASS] = opts.class;
    stats[CLASS] += opts.class === "commoner" ? " 0" : " 1";
    stats[PROF_BONUS] = "+1";
    stats[HIT_DICE] = "1" + _class.hit_die;
    _class.feats.forEach((feat) => {
        if(isEligibleForFeat(stats, feat)){
            stats[feats].push({
                name: feat.name,
                description: feat.description
            });
        }
    });
}

function applyBackground(stats, opts){
    let background = BACKGROUNDS.get(opts[BACKGROUND]);
    if(typeof(background) === "undefined"){
        console.log("Invalid background: " + opts[BACKGROUND]);
        return;
    }
    stats[BACKGROUND] = opts[BACKGROUND];
    background.proficiencies.forEach((prof) => {
        apply_proficiency(stats, prof);
    })
    background.items.forEach(item => {
        apply_item(stats, item);
    });
}

function apply_item(stats, item){
    let packs = [ ...PACKS.keys() ];
    if(packs.includes(item)){
        pack = PACKS.get(item);
        pack.forEach(pack_item => {
            apply_item(stats, pack_item);
        });
    }
    else{
        if(typeof(stats[INVENTORY]) === "undefined"){
            stats[INVENTORY] = [];
        }
        stats[INVENTORY].push(item);
    }
}

function apply_proficiency(stats, prof){
    stats[SKILL_PROFS] = SKILL_PROFS in stats ? stats[SKILL_PROFS] : [];
    stats[WEAPON_PROFS] = WEAPON_PROFS in stats ? stats[WEAPON_PROFS] : [];
    stats[ARMOR_PROFS] = ARMOR_PROFS in stats ? stats[ARMOR_PROFS] : [];
    stats[LANGUAGE_PROFS] = LANGUAGE_PROFS in stats ? stats[LANGUAGE_PROFS] : [];
    stats[SAVE_PROFS] = SAVE_PROFS in stats ? stats[SAVE_PROFS] : [];
    stats[TOOL_PROFS] = TOOL_PROFS in stats ? stats[TOOL_PROFS] : [];
    let weapons = [ ...WEAPONS.keys() ];
    if(SKILLS.includes(prof)){
        if(!stats[SKILL_PROFS].includes(prof)){
            stats[SKILL_PROFS].push(prof);    
        }
    }
    else if(weapons.includes(prof)){
        if(!stats[WEAPON_PROFS].includes(prof)){
            stats[WEAPON_PROFS].push(prof);
        }
    }
    else if(ARMORS.includes(prof)){
        if(!stats[ARMOR_PROFS].includes(prof)){
            stats[ARMOR_PROFS].push(prof);
        }
    }
    else if(LANGUAGES.includes(prof)){
        if(!stats[LANGUAGE_PROFS].includes(prof)){
            stats[LANGUAGE_PROFS].push(prof);
        }
    }
    else if(SAVES.includes(prof)){
        if(!stats[SAVE_PROFS].includes(prof)){
            stats[SAVE_PROFS].push(prof);
        }
    }
    else{
        if(!stats[TOOL_PROFS].includes(prof)){
            stats[TOOL_PROFS].push(prof);
        }
    }
}

async function createActorDocument(name, biography){
    let actor = await Actor.create({
        name: name,
        type: "character",
        folder: "30JW8wUVMABUvnly",
        img: "https://assets.forge-vtt.com/5fc57cb47467ca168ff9134a/blank.png"
    });
    actor.data.data.biography = biography;
}


function printAllActorFolders(){
    for(const actor of game.actors.values()){
        let name = actor.data.data.name;
        let folder = actor.data.data.folder;
        console.log(actor.data.name + ": " + actor.data.folder);
    }
}

function build_creation_content(){
    let content = "";
    
    // Add name
    content += `<div><label>Name</label><input id="name"></input></div>`;

    // Add lineage options
    content += `<div><label>Lineage</label><select id="lineage">`;

    let lineages_list = [ ...LINEAGES.keys() ];
    lineages_list.forEach((lineage) => {
        content += `
            <option value "${lineage}">${lineage}</option>
        `;
    });
    content += `</select></div><br>`;

    return content;
}

function build_creation_buttons(){
    let buttons = [];
    buttons.push({
        label: "Create Commoner",
        callback: async(html) => {
            console.log(html);
        }
    });
    return buttons;
}

function creation_dialogue(){
    return new Dialog({
        title: "Create commoner",
        content: build_creation_content(),
        buttons: build_creation_buttons()
    }).render(true);
}

/*
    HTML generation for actor
*/

function getArmorClass(stats){
    return stats[DEXTERITY_MOD] + 10;
}

function generateBio(stats){
    let bio = "";
    // Main table
    bio += generateStatsTable(stats);
    bio += generateProficienciesTable(stats);
    bio += generateAttacksTable(stats);
    bio += generateFeatsTable(stats);
    return bio;
}

function generateStatsTable(stats){
    let bio = "";
    bio += `<table border="1"><tbody>`
    bio += `<tr>`;
    bio += `<td>ABILITY</td>`;
    bio += `<td>SCORE</td>`;
    bio += `<td>MOD</td>`;
    bio += `<td></td>`;
    bio += `<td>XP: 0</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>STR</td>`;
    bio += `<td>${stats[WISDOM]}</td>`;
    bio += `<td>${stats[WISDOM_MOD]}</td>`;
    bio += `<td>AC: ${getArmorClass(stats)}</td>`;
    bio += `<td>${stats[CLASS]}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>DEX</td>`;
    bio += `<td>${stats[DEXTERITY]}</td>`;
    bio += `<td>${stats[DEXTERITY_MOD]}</td>`;
    bio += `<td>Size: ${stats[SIZE]}</td>`;
    bio += `<td>Lineage: ${stats[LINEAGE]}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>CON</td>`;
    bio += `<td>${stats[CONSTITUTION]}</td>`;
    bio += `<td>${stats[CONSTITUTION_MOD]}</td>`;
    bio += `<td>Speed: ${stats[SPEED]}</td>`;
    bio += `<td>Background: ${stats[BACKGROUND]}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>INT</td>`;
    bio += `<td>${stats[INTELLIGENCE]}</td>`;
    bio += `<td>${stats[INTELLIGENCE_MOD]}</td>`;
    bio += `<td></td>`;
    bio += `<td>Hit Dice: ${stats[HIT_DICE]}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>WIS</td>`;
    bio += `<td>${stats[WISDOM]}</td>`;
    bio += `<td>${stats[WISDOM_MOD]}</td>`;
    bio += `<td></td>`;
    bio += `<td>Proficiency Bonus: ${stats[PROF_BONUS]}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>CHA</td>`;
    bio += `<td>${stats[CHARISMA]}</td>`;
    bio += `<td>${stats[CHARISMA_MOD]}</td>`;
    bio += `<td></td>`;
    bio += `<td></td>`;
    bio += `</tr>`;
    bio += `</tbody></table>`;
    return bio;
}

function generateProficienciesTable(stats){
    let bio = "";
    bio += `<table border="1"><tbody>`;
    bio += `<tr>`;
    bio += `<td>Armor</td>`;
    bio += `<td>${stats[ARMOR_PROFS].join(",")}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>Weapons</td>`;
    bio += `<td>${stats[WEAPON_PROFS].join(",")}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>Tools</td>`;
    bio += `<td>${stats[TOOL_PROFS].join(",")}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>Languages</td>`;
    bio += `<td>${stats[LANGUAGE_PROFS].join(",")}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>Skills</td>`;
    bio += `<td>${stats[SKILL_PROFS].join(",")}</td>`;
    bio += `</tr>`;
    bio += `<tr>`;
    bio += `<td>Saving Throws</td>`;
    let cleaned_saves = [];
    stats[SAVE_PROFS].forEach((prof) => {
        cleaned_saves.push(prof.replace(" save", ""));
    });
    bio += `<td>${cleaned_saves.join(",")}</td>`;
    bio += `</tr>`;

    bio += `</tbody></table>`;
    return bio;
}

function getActorAttacks(stats){
    let attacks = [];
    attacks = attacks.concat(getWeaponAttacks(stats, UNARMED));
    attacks.push();
    let weapons = [ ...WEAPONS.keys() ];
    stats[INVENTORY].forEach((item) => {
        if(weapons.includes(item)){
            attacks = attacks.concat(getWeaponAttacks(stats, item))
        }
    });
    return attacks;
}

function generateAttacksTable(stats){
    let bio = "";
    bio += `<table border="1"><tbody>`;
    bio += `<tr>`;
    bio += `<td>Attack</td>`;
    bio += `<td>To hit</td>`;
    bio += `<td>Damage</td>`;
    bio += `</tr>`;
    let attacks = getActorAttacks(stats);
    attacks.forEach((attack) => {
        bio += `<tr>`;
        bio += `<td>${attack[ATTACK_NAME]}</td>`;
        bio += `<td>${attack[TO_HIT] < 0 ? attack[TO_HIT] : "+" + attack[TO_HIT]}</td>`;
        bio += `<td>${attack[ATTACK_DAMAGE]}</td>`;
        bio += `</tr>`;
    });

    bio += `</table></tbody>`;
    return bio;
}

function generateFeatsTable(stats){
    let bio = "";
    bio += `<table border="1"><tbody>`;
    bio += `<tr>`;
    bio += `<td>Feat</td>`;
    bio += `<td>Description</td>`;
    bio += `</tr>`;
    stats[FEATS].forEach(feat => {
        bio += `<tr>`;
        bio += `<td>${feat[NAME]}</td>`;
        bio += `<td>${feat[DESCRIPTION]}</td>`;
        bio += `</tr>`;
    });
    bio += `</tbody></table>`;
    return bio;
}

let stats = await getStats(debugOpts());
let bio = generateBio(stats);
createActorDocument(stats[NAME], bio);

//creation_dialogue();