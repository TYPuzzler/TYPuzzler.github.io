/**
 * Returns the metadata of a random piece of a puzzle
 * @param {string} puzzleName the name of the puzzle
 * @returns JSON metadata of the puzzle pieces
 */
 export const randomPiece = async (puzzleName = "JS_logo") => {
    var url = "https://typuzzler.pythonanywhere.com/random/\"" + puzzleName + "\"";
    var result;
    await fetch(url)
        .then(response => response.json())
        .then(data => {
            result = data;
        });
    return result;
}