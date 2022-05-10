import '../App.css';
import { Link } from "react-router-dom";

function PuzzleInventory() {
  var piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/JS_logo_piece_10.png?raw=true";
  var puzzle = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/gray_puzzle_JS_logo.png?raw=true";
  var pieceLocation = {
    position: 'absolute',
    top: '300px',
    left: '775px'
  };
  var puzzleLocation = {
    position: 'absolute',
    top: '200px',
    left: '475px'
  };

  return (
    <div className="App">
      <p>Here's your puzzle progress so far. Keep it up!</p>
      <div>
        <img src={puzzle} style={puzzleLocation}></img>
        <img src={piece} style={pieceLocation}></img>
      </div>
    </div>
  );
}

export default PuzzleInventory;
