/*
  Rolls out a new character's stats by rolling 4d6, dropping the lowest, and
  assigning each roll in order.
*/

function randomNumber(min, max){
    const r = Math.random()*(max-min) + min
    return Math.floor(r)
}

function rollInOrder()
{
    let r = "Rolling stats in order. 4d6kh3";
    r += "<br>STR: " + new Roll("4d6kh3").evaluate().total;
    r += "<br>DEX: " + new Roll("4d6kh3").evaluate().total;
    r += "<br>CON: " + new Roll("4d6kh3").evaluate().total;
    r += "<br>INT: " + new Roll("4d6kh3").evaluate().total;
    r += "<br>WIS: " + new Roll("4d6kh3").evaluate().total;
    r += "<br>CHA: " + new Roll("4d6kh3").evaluate().total;
    return r;
}

function deliverMessage(message)
{
  let chatData = {
    user: game.user._id,
    speaker: ChatMessage.getSpeaker(),
    content: message
  }
  ChatMessage.create(chatData, {});  
}

deliverMessage(rollInOrder());
