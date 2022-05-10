import '../App.css';
import { Link } from "react-router-dom";

function PuzzleInventory() {
  var piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/JS_logo_piece_10.png?raw=true";
  var puzzle = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/gray_puzzle_JS_logo.png?raw=true";
  var pieceLocation = {
    position: 'absolute',
    top: '300px',
    left: '750px'
  };
  var puzzleLocation = {
    position: 'absolute',
    top: '200px',
    left: '450px'
  };
  return (
    <div className="App">
      PuzzleInventory
      <Link to="/">
        <button variant="outlined">
          Home
        </button>
      </Link>
      <br/>
      <div>
        <img src={puzzle} style={puzzleLocation}></img>
        <img src={piece} style={pieceLocation}></img>
      </div>
      
    </div>
  );
}

export default PuzzleInventory;
