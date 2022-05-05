/**
 * This function generates a random sample text and returns it as a string.
 * Returns a sample 200 characters long by default, but can be customized
 * with the length parameter.
*/
export const generate = async (length = 200) => {
    var temp;
    await fetch('https://fakerapi.it/api/v1/texts?_quantity=1&_characters=' + length)
        .then(response => response.json())
        .then(data => {
            temp = data.data[0].content;
        }).finally(() => temp);
    return temp;
};