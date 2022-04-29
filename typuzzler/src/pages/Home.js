import '../App.css';
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="App">
      TestPage Home
      <Link to="/typing">
        <button variant="outlined">
          Start typing
        </button>
      </Link>
    </div>
  );
}

export default Home;
