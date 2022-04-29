import '../App.css';
import { Link } from "react-router-dom";

function PuzzleSelect() {
  return (
    <div className="App">
      PuzzleSelect
      <Link to="/puzzle">
        <button variant="outlined">
          Next
        </button>
      </Link>
    </div>
  );
}

export default PuzzleSelect;
