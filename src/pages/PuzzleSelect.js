import '../App.css';
import { Link } from "react-router-dom";
//import {PythonShell} from 'python-shell';

function PuzzleSelect() {
  var piece = "https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS_logo/JS_logo_piece_10.png?raw=true";

  return (
    <div className="App">
      <p>Great job! You got a puzzle piece.</p>
      <Link to="/puzzle">
        <button variant="outlined">
          Next
        </button>
      </Link>
      <br/>
      <img src={piece}></img>
    </div>
  );
}

export default PuzzleSelect;
