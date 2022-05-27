import '../App.css';
import { Link } from "react-router-dom";
import React, { useCallback, useState } from 'react';
import { draw } from "../utils/drawPuzzle";

function PuzzleInventory() {
  var level = localStorage.getItem("level") || 1;
  var [reward, setReward] = useState(['default']);
  const fetchData = useCallback(async () => {
    // Get text sample from generator
    var data = await draw(level);
    setReward(data);
    console.log(data)
  });

  React.useEffect(() => {
    // Retrieve the text sample immediately when this page is loaded
    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  }, [])

  var puzzleName = "JS_logo"
  var piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/" + puzzleName + "/" + puzzleName + "_piece_10.png?raw=true";
  var puzzle = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/" + puzzleName + "/gray_puzzle_"+ puzzleName +".png?raw=true";

  var puzzleLocation = {
    position: 'absolute',
    top: '0px',
    left: '0px', 
  };

  var inventory = {
    position: 'relative',
    // TODO: Replace with puzzle dimensions
    width: '600px', 
    height: '600px',
    marginLeft: 'auto',
    marginRight: 'auto'
  };

  var test = [];
  test.push(<img src={puzzle} style={puzzleLocation}></img>);
  test.push(<img src={piece} style={{position: 'absolute', top: '100px', left: '300'}}></img>);

  //var test = draw("JS_logo", [10, 1])
  var temp = (
    <div style={inventory}>
      {test}
    </div>
  )
  return (
    <div className="App">
      <p>Here's your puzzle progress so far. Keep it up!</p>
      {reward}
    </div>
  );
}

export default PuzzleInventory;
