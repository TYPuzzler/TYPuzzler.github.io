import logo from './logo.svg';
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
      <Link to="/signup">
        <button variant="outlined">
          Sign up
        </button>
      </Link>
      
      <Main />
    </div>
  );
}

export default App;
