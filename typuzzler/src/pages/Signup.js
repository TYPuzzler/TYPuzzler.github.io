import '../App.css';
import useKeyPress from '../hooks/useKeypress';

function KeyPress() {
  useKeyPress(key => {
    console.log(key)
  });
}
  
function Signup() {
  return (
    <div className="App">
      TestPage Signup
      <KeyPress></KeyPress>
    </div>
  );
}

export default Signup;
