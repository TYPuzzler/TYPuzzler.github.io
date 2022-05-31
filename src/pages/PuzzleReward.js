import '../App.css';
import { Link } from "react-router-dom";

/**
 * This represents the page that rewards the user with a puzzle piece after a typing exercise.
 */
function PuzzleReward() {
  var level = localStorage.getItem("level") ?? 0;
  var piece;
  var text;
  if (level < 1) {
    text = "Please complete an exercise before earning a puzzle piece.";
  } else {
    text = "Great job! You got a puzzle piece.";
  }

  if (level == 0) {
    piece = "";
  } else if (level <= 25) {
    piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/JS_logo_piece_" + level + ".png?raw=true";
  } else if (level <= 108 + 25) {
    piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/husky_logo/husky_logo_piece_"+ (level - 25) +".png?raw=true"
  } else if (level <= 108 + 108 + 25) {
    piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/python_logo/python_logo_piece_"+ (level - 25 - 108) +".png?raw=true"
  }

  return (
    <div className="App">
      <p>{text}</p>
      <br/>
      <img src={piece}></img>
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
