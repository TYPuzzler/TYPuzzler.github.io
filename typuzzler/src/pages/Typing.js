import '../App.css';
import useKeyPress from '../hooks/useKeypress';
import { Link } from "react-router-dom";
import { generate } from '../utils/words'
import React, { useCallback, useState } from 'react';


function KeyPress() {
  useKeyPress(key => {
    console.log(key)
  });
}

function Typing() {
  // This makes initialWords a mutable string.
  const [initialWords, setInitialWords] = useState('Loading...');
  const fetchData = useCallback(async () => {
    // Get text sample from generator
    const data = await generate()

    // set state with the result
    setInitialWords(data);
  });

  React.useEffect(() => {
    // Retrieve the text sample immediately when this page is loaded
    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  }, [])

  return (
    <div className="App">
      Typing 
      <Link to="/puzzleSelect">
        <button variant="outlined">
          Next
        </button>
      </Link>
      <p>
      {initialWords}
      </p>
      <KeyPress></KeyPress>
    </div>
  );
}

export default Typing;
