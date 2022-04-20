/**
 * This function generates a random sample text stored as a string in an array.
*/
export const generate = () => {
    // TODO: Return text in a different format so that we don't have to extract it from an array.
    var temp = new Array();
    fetch('https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500')
        .then(text => text.json())
        .then(data => temp.push(data["data"][0]["content"].toString()));
    return temp;
};