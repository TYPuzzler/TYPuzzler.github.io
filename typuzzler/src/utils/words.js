/**
 * This function generates a random sample text and returns it as a string
*/
export const generate = async () => {
    // TODO: Return text in a different format so that we don't have to extract it from an array.
    //var temp = "";
    var temp;
    await fetch('https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500')
        .then(response => response.json())
        .then(data => {
            temp = data.data[0].content;
        }).finally(() => temp);
    //console.log(temp);
    return temp;
};