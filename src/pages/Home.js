import '../App.css';
import { Link } from "react-router-dom";

var puzzles = {
  1 : "JS_logo",
  2 : "husky_logo",
  3 : "python_logo"
}

function Home() {
  return (
    <div className="App">
      <h1>Welcome to TYPuzzler!</h1>
      <p>It's never been so unpuzzling to learn typing!</p>
      <Link to="/typing">
        <button variant="outlined">
          Start typing
        </button>
      </Link>
      <button onClick={() => clear()}>
        Clear data
      </button>
    </div>
  );
}

// Clears puzzle progress if user confirms
function clear() {
  var answer = window.confirm("Are you sure you want to clear your data? This will delete all your progress!");
  if (answer) {
    localStorage.removeItem("level");
    localStorage.removeItem("round");
    localStorage.removeItem("last_earned");
    for (var i = 1; i <= 3; i++) {
      localStorage.removeItem(puzzles[i]);
      localStorage.removeItem(puzzles[i] + "_order");
    }
  }
}


export default Home;
