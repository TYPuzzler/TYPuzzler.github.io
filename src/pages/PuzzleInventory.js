import '../App.css';
import { Link } from "react-router-dom";

function PuzzleInventory() {
  var puzzle = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/full_puzzle_JS_logo.png?raw=true"
  
  return (
    <div className="App">
      <p>Here's your puzzle progress so far. Keep it up!</p>
      <br/>
      <img src={puzzle}></img>
      <br/>
      <Link to="/">
        <button variant="outlined">
          Home
        </button>
      </Link>
    </div>
  );
}

export default PuzzleInventory;
