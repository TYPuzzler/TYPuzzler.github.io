/**
 * Returns the html for the puzzle reward given the user's level
 */
export const draw = async (level = 1) => {
    var pieceCount = level;
    var result = [];
    var puzzleName;
    var gray;
    var pieces;
    if (level <= 25) {
        puzzleName = "JS_logo";
    } else if (level <= (25 + 108)) {
        puzzleName = "husky_logo"
        pieceCount = pieceCount - 25;
    } else {
        puzzleName = "python_logo"
        pieceCount = pieceCount - 25 - 108;
    }

    // Get the grayscale background
    gray = await getGray(puzzleName);
    var inventory = {
        position: 'relative',
        // TODO: Replace with puzzle dimensions
        width: gray[1], 
        height: gray[2],
        marginLeft: 'auto',
        marginRight: 'auto'
      };
    result.push(<img src={gray[0]} style={{position : 'absolute', top :'0px', left: '0px'}}></img>);

    // Add the pieces earned on top of the gray scale background
    pieces = await metaData(puzzleName);
    //console.log(pieces[1])
    for (var i = 1; i <= pieceCount; i++) {
        result.push(<img src={pieces[i][0]} style={{position : 'absolute',
            left : pieces[i][2] + "px",
            top : pieces[i][3] + "px"}}></img>);
    }
    
    console.log(result)
    return (
        <div style={inventory}>
            {result}
        </div>
    )
};

export const metaData = async (puzzleName = "JS_logo") => {
    var url = "https://typuzzler.pythonanywhere.com/test/\"" + puzzleName + "\"";
    var result;
    await fetch(url)
        .then(response => response.json())
        .then(data => {
            result = data;
        });
    console.log(result)
    return result;
}

export const getGray = async (puzzleName = "JS_logo") => {
    var url = "https://typuzzler.pythonanywhere.com/gray/\"" + puzzleName + "\"";
    var result;
    await fetch(url)
        .then(response => response.json())
        .then(data => {
            result = data;
        })
    console.log(result)
    return result;
}