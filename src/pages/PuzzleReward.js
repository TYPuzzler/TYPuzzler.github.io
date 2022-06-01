import '../App.css';
import { Link } from "react-router-dom";
const puzzles = {
  1 : "JS_logo",
  2 : "husky_logo",
  3 : "python_logo"
}


/**
 * This represents the page that rewards the user with a puzzle piece after a typing exercise.
 */
function PuzzleReward() {
  var level = localStorage.getItem("level") ?? 1;
  var piece;
  var text;
  var puzzleName;
  if (level < 1) {
    text = "Please complete an exercise before earning a puzzle piece.";
  } else {
    text = "Great job! You got a puzzle piece.";
  }

  puzzleName = puzzles[level]; // Get which puzzle the user is on
  var last_earned = JSON.parse(localStorage.getItem("last_earned")); // Get the user's earned pieces
  
  if (level < 0 || level > 3) {
    piece = "";
  } else {
    piece = last_earned[1];
  }

  return (
    <div className="App">
      <p>{text}</p>
      <br/>
      <img className="Puzzle-piece" src={piece}></img>
      <br/>
      <Link to="/puzzleprogress">
        <button variant="outlined">
          Next
        </button>
      </Link>
    </div>
  );
}

export default PuzzleReward;
