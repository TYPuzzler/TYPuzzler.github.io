import '../App.css';
import { Link } from "react-router-dom";
import React, { useCallback, useState } from 'react';
import { draw } from "../utils/drawPuzzle";

/**
 * This represents the page that presents the user's progress on the current puzzle.
 */
function PuzzleProgress() {
  const puzzles = {
    1 : "JS_logo",
    2 : "husky_logo",
    3 : "python_logo"
  }
  const pieceCounts = {
    1 : 25,
    2 : 108,
    3 : 108
  }

  var level = JSON.parse(localStorage.getItem("level")) || 0;
  var puzzleName;
  if (level < 1 || level > 3) {
    puzzleName = puzzles[1];
  } else {
    puzzleName = puzzles[level];
  }
  var earnedPieces = JSON.parse(localStorage.getItem(puzzleName));
  var last_earned = JSON.parse(localStorage.getItem("last_earned"));
  console.log(earnedPieces);

  var [text, setText] = useState('Here\'s your puzzle progress so far. Keep it up!');
  var [reward, setReward] = useState(['']);

  const fetchData = useCallback(async () => {
    // Get the formatted images for the reward screen and display them.
    var data = await draw(level, earnedPieces, last_earned);
    setReward(data);
    if (earnedPieces[0] >= pieceCounts[level]) {
      if (level < 3) {
        localStorage.setItem("level", level + 1);
        setText('Congratulations! \n Thanks to your effort, you\'ve completed this puzzle!\n Don\'t forget to give your hands a rest.');
      } else {
        setText('You\'ve completed all the puzzles! You can clear your data to start over on the home page.');
      }
    }
  });

  React.useEffect(() => {
    // Retrieve the formatted images immediately when the page is loaded
    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  }, [])

  return (
    <div className="App">
      <p>{text}</p>
      <Link to="/typing">
        <button variant="outlined">
          Type more
        </button>
      </Link>
      {reward}
    </div>
  );
}

export default PuzzleProgress;
