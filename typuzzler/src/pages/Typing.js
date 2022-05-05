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
  // The substring of the sample text that has been correctly typed
  const [correctChars, setCorrectChars] = useState('');

  // The current character to be typed
  const [currentChar, setCurrentChar] = useState('');

  // The rest of the sample text
  const [incomingChars, setIncomingChars] = useState('Loading...');

  const [wordCount, setWordCount] = useState(0);

  // Note: correctChars + currentChar + incomingChars creates the whole sample text

  // The time when user started typing
  const [startTime, setStartTime] = useState(0);

  // Users words per minute
  const [wpm, setWpm] = useState('');


  const fetchData = useCallback(async () => {
    // Get text sample from generator
    const data = await generate()

    // set state with the result
    setCurrentChar(data.charAt(0));
    setIncomingChars(data.substring(1));
    setWordCount(data.length/5);
  });

  React.useEffect(() => {
    // Retrieve the text sample immediately when this page is loaded
    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  }, [])



  function KeyPress() {
    useKeyPress(key => {
      console.log(key) // For testing purposes

      if (correctChars.length == 0) {
        // Start timing when the user starts typing
        setStartTime(new Date().getTime());
      }

      if (key == currentChar) {
        // Validate typed character against text sample and update state if correct
        setCorrectChars(correctChars + currentChar);
        setCurrentChar(incomingChars.charAt(0));
        setIncomingChars(incomingChars.substring(1));
        if (incomingChars.length == 0) {
          // User is done typing
          var duration = ((new Date().getTime()) - startTime) / 60000.0; // convert to minutes
          setWpm("WPM: " + (wordCount / duration).toFixed(2));
        }
      }


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
      <p>
        {wpm}
      </p>
      <KeyPress></KeyPress>
    </div>
  );
}

export default Typing;
