

/**
 * Returns the html for the user's puzzle progress
 * @param {*} level The user's level
 * @param {*} earnedPieces The pieces that the user has earned
 * @param {*} last_earned The last piece that the user has earned
 * @returns 
 */
export const draw = async (level = 1, earnedPieces = Array(109).fill(0), last_earned) => {
    const puzzles = {
        1 : "JS_logo",
        2 : "husky_logo",
        3 : "python_logo"
    }

    const pieceCounts = {
        1 : 25,
        2 : 108,
        3 : 108
    }

    var result = [];

    // Get the name of the puzzle that the user is currently working on
    var puzzleName;
    if (level < 1 || level > 3) {
        puzzleName = puzzles[1];
    } else {
        puzzleName = puzzles[level];
    }
    var gray;

    // Get the puzzle outline (previously a grayscale background)
    gray = await getGray(puzzleName);
    var inventory = {
        position: 'relative',
        width: gray[1], 
        height: gray[2],
        marginLeft: 'auto',
        marginRight: 'auto',
        "borderStyle": 'solid',
        "border-width": '3px',
        "border-color": '#000000'
    };

    // Add the pieces earned on top of the gray scale background
    var pieces;
    if (earnedPieces[0] >= pieceCounts[level]) {
        pieces = await getFull(puzzleName);
        result.push(<img src={pieces[0]} style={{position : 'absolute',
                    left : '0px',
                    top : '0px'}}></img>)
    } else if (earnedPieces[0] > 0) {
        // User has earned at least one puzzle piece
        pieces = await metaData(puzzleName);
        for (var i = 1; i <= pieceCounts[level]; i++) {
            if (last_earned[0] == i) { {
                // TODO: draw last earned piece normally
                result.push(<img src={last_earned[1]} style={{position : 'absolute',
                    left : last_earned[3] + "px",
                    top : last_earned[4] + "px"}}></img>);
            }
            } else if (earnedPieces[i] == 1) {
                result.push(<img src={pieces[i][0]} style={{position : 'absolute',
                    left : pieces[i][1] + "px",
                    top : pieces[i][2] + "px"}}></img>);
            }
        }
    }
    
    console.log(result)
    return (
        <div style={inventory}>
            {result}
        </div>
    )
};

/**
 * Returns the metadata of the puzzle pieces of a puzzle
 * @param {string} puzzleName the name of the puzzle
 * @returns JSON metadata of the puzzle pieces
 */
export const metaData = async (puzzleName = "JS_logo") => {
    var url = "https://typuzzler.pythonanywhere.com/trans/\"" + puzzleName + "\"";
    var result;
    await fetch(url)
        .then(response => response.json())
        .then(data => {
            result = data;
        });
    return result;
}

/**
 * Returns the grayscale version of a puzzle to be used as the backgroudn of the reward screen
 * @param {string} puzzleName the name of the puzzle
 * @returns Json of metadata of the grayscale version of the puzzle
 */
export const getGray = async (puzzleName = "JS_logo") => {
    var url = "https://typuzzler.pythonanywhere.com/gray/\"" + puzzleName + "\"";
    var result;
    await fetch(url)
        .then(response => response.json())
        .then(data => {
            result = data;
        })
    return result;
}

export const getFull = async (puzzleName = "JS_logo") => {
    var url = "https://typuzzler.pythonanywhere.com/full/\"" + puzzleName + "\"";
    var result;
    await fetch(url)
        .then(response => response.json())
        .then(data => {
            result = data;
        })
    return result;
}