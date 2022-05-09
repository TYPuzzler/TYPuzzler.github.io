import '../App.css';
import { Link } from "react-router-dom";

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
    </div>
  );
}

export default Home;
