import './App.css';
import Main from './Main';
import { Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Link to="/">
        <button variant="outlined">
          Home
        </button>
      </Link>
      <Main />
    </div>
  );
}

export default App;
