import '../App.css';
import useKeyPress from '../hooks/useKeypress';
import { Link } from "react-router-dom";
import { generate } from '../utils/words'
import React, { useCallback, useState } from 'react';


/*function KeyPress() {
  useKeyPress(key => {
    console.log(key);
  });
}*/

function Typing() {
  
  // The sample text
  const [initialWords, setInitialWords] = useState('Loading...');

  // The substring of the sample text that has been correctly typed
  const [correctChars, setCorrectChars] = useState('');

  // The current character to be typed
  const [currentChar, setCurrentChar] = useState('');

  // The rest of the sample text
  const [incomingChars, setIncomingChars] = useState('Loading...');

  const fetchData = useCallback(async () => {
    // Get text sample from generator
    const data = await generate()

    // set state with the result
    setInitialWords(data);
    setCurrentChar(data.charAt(0));
    setIncomingChars(data.substring(1));
  });

  React.useEffect(() => {
    // Retrieve the text sample immediately when this page is loaded
    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  }, [])



  function KeyPress() {
    useKeyPress(key => {
      console.log(key);
      if (key == currentChar) {
        setCorrectChars(correctChars + currentChar);
        setCurrentChar(incomingChars.charAt(0));
        setIncomingChars(incomingChars.substring(1));
      }
      setInitialWords(initialWords.substring(1));
    });
  }

  return (
    <div className="App">
      Typing 
      <Link to="/puzzleSelect">
        <button variant="outlined">
          Next
        </button>
      </Link>
      <p>
        <span className="Character-correct">
          {correctChars}
        </span>
        <span className="Character-current">
          {currentChar}
        </span>
        <span>
          {incomingChars}
        </span>
      </p>
      <KeyPress></KeyPress>
    </div>
  );
}

export default Typing;
