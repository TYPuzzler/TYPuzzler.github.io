import '../App.css';
import useKeyPress from '../hooks/useKeypress';
import { Link } from "react-router-dom";

function KeyPress() {
  useKeyPress(key => {
    console.log(key)
  });
}

function Typing() {
  return (
    <div className="App">
      Typing
      <Link to="/puzzleSelect">
        <button variant="outlined">
          Next
        </button>
      </Link>
      <KeyPress></KeyPress>
    </div>
  );
}

export default Typing;
