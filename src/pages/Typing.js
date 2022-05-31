import '../App.css';
import useKeyPress from '../hooks/useKeypress';
import { Link } from "react-router-dom";
import { generate } from '../utils/words'
import React, { useCallback, useState } from 'react';
import { draw } from '../utils/drawPuzzle';

/**
 * This represents the page that is presented to the user when they start a typing session.
 */
function Typing() {
  var level = parseInt(localStorage.getItem("level")) || 0;

  // The substring of the sample text that has been correctly typed
  const [correctChars, setCorrectChars] = useState('');

  // The current character to be typed
  const [currentChar, setCurrentChar] = useState('');

  // The rest of the sample text
  const [incomingChars, setIncomingChars] = useState('Loading...');

  // Note: correctChars + currentChar + incomingChars creates the whole sample text

  // The time when user started typing
  const [startTime, setStartTime] = useState(0);

  // Users words per minute
  const [wpm, setWpm] = useState('');

  // The user's typing accuracy
  const[accuracy, setAccuracy] = useState('');

  // The characters that the user has typed
  const[typed, setTyped] = useState('');


  const fetchData = useCallback(async () => {
    // Get text sample from generator
    const data = await generate()

    // set state with the result
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
      console.log(key) // For testing purposes

      setTyped(typed + key);

      if (correctChars.length == 0) {
        // Start timing when the user starts typing
        setStartTime(new Date().getTime());
      }

      // Validate typed character against text sample and update state if correct
      if (key == currentChar) {
        // change background color of current character back to normal color
        document.getElementById("curr").style.backgroundColor = "#d1a428";

        setCorrectChars(correctChars + currentChar);
        setCurrentChar(incomingChars.charAt(0));
        setIncomingChars(incomingChars.substring(1));
        if (incomingChars.length == 0) {
          // User is done typing, so let's calculate the user's WPM and Accuracy

          var duration = ((new Date().getTime()) - startTime) / 60000.0; // convert to minutes
          setWpm("WPM: " + ((correctChars.length / 5) / duration).toFixed(2)); 
          setAccuracy("ACC: " + ((correctChars.length * 100) / typed.length).toFixed(2) + "%")
          localStorage.setItem("level", (level + 1));
        }
      } else {
        // change background color of current color to red to indicate wrong character was entered
        document.getElementById("curr").style.backgroundColor = "#e0503a";
      }
    });
  }

  return (
    <div className="App">
      <p>Type the text you see below. Aim for perfect accuracy first, then try improving your speed!</p>
      <p className="Typing-text">
        <span className="Character-correct">
          {correctChars}
        </span>
        <span id="curr" className="Character-current">
          {currentChar}
        </span>
        <span>
          {incomingChars}
        </span>
      </p>
      <p>
        {wpm}
      </p>
      <p>
        {accuracy}
      </p>
      <KeyPress></KeyPress>
      <Link to="/puzzlereward">
        <button variant="outlined">
          Next
        </button>
      </Link>
    </div>
  );
}

export default Typing;
