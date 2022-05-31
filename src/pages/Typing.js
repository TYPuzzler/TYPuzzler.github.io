import '../App.css';
import useKeyPress from '../hooks/useKeypress';
import { Link } from "react-router-dom";
import { generate } from '../utils/words'
import React, { useCallback, useState } from 'react';
import { randomPiece } from '../utils/randomPiece';

/**
 * This represents the page that is presented to the user when they start a typing session.
 */
function Typing() {
  var level = parseInt(localStorage.getItem("level")) || 1;
  var puzzleName;
  if (level == 1) {
    puzzleName = "JS_logo";
  } else if (level == 2) {
    puzzleName = "husky_logo";
  } else {
    puzzleName = "python_logo";
  }

  const pieceCounts = {
    1 : 25,
    2 : 108,
    3 : 108
}


  var earnedPieces = JSON.parse(localStorage.getItem(puzzleName)) ?? Array(109).fill(0);

  const [reward, setReward] = useState([]);

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

  const[nextButton, setNextButton] = useState([]);


  const fetchData = useCallback(async () => {
    // Get text sample from generator
    const text = await generate(50);
    const rand = await randomPiece(puzzleName);
    setReward(rand);

    // set state with the result
    setCurrentChar(text.charAt(0));
    setIncomingChars(text.substring(1));
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

          
          earnedPieces[0] = earnedPieces[0] + 1;
          earnedPieces[reward[0]] = 1;
          localStorage.setItem("level", JSON.stringify(level));
          localStorage.setItem("last_earned", JSON.stringify(reward));
          localStorage.setItem(puzzleName, JSON.stringify(earnedPieces));
          setNextButton([<button variant="outlined">
          Next
        </button>]);
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
      {nextButton}
      </Link>
    </div>
  );
}

export default Typing;
