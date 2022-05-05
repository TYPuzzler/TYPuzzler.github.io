import '../App.css';
import { Link } from "react-router-dom";

function PuzzleInventory() {
  return (
    <div className="App">
      PuzzleInventory
      <Link to="/">
        <button variant="outlined">
          Home
        </button>
      </Link>
    </div>
  );
}

export default PuzzleInventory;
