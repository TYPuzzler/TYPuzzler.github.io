import '../App.css';
import { Link } from "react-router-dom";
//import { draw } from "../utils/drawProgress";

function PuzzleInventory() {
  var puzzleName = "JS_logo"
  var piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/" + puzzleName + "/" + puzzleName + "_piece_10.png?raw=true";
  var puzzle = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/" + puzzleName + "/gray_puzzle_"+ puzzleName +".png?raw=true";
  var pieceLocation = {
    position: 'absolute',
    top: '100px',
    left: '300px',
  };

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

  //var test = draw("JS_logo", [10, 1])
  var temp = (
    <div style={inventory}>
      <img src={puzzle} style={puzzleLocation}></img>
      <img src={piece} style={pieceLocation}></img>
    </div>
  )
  return (
    <div className="App">
      <p>Here's your puzzle progress so far. Keep it up!</p>
      
      {temp}
    </div>
  );
}

export default PuzzleInventory;
