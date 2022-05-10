import '../App.css';
import { Link } from "react-router-dom";

function PuzzleInventory() {
  var puzzle = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/full_puzzle_JS_logo.png?raw=true"
  return (
    <div className="App">
      PuzzleInventory
      <Link to="/">
        <button variant="outlined">
          Home
        </button>
      </Link>
      <br/>
      <img src={puzzle}></img>
    </div>
  );
}

export default PuzzleInventory;
