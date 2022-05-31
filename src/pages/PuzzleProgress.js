import '../App.css';
import { Link } from "react-router-dom";
import React, { useCallback, useState } from 'react';
import { draw } from "../utils/drawPuzzle";

/**
 * This represents the page that presents the user's progress on the current puzzle.
 */
function PuzzleProgress() {
  var level = localStorage.getItem("level") || 0;
  var [reward, setReward] = useState(['']);
  const fetchData = useCallback(async () => {
    // Get the formatted images for the reward screen and display them.
    var data = await draw(level);
    setReward(data);
    console.log(data)
  });

  React.useEffect(() => {
    // Retrieve the formatted images immediately when the page is loaded
    fetchData()
      // make sure to catch any error
      .catch(console.error);;
  }, [])

  return (
    <div className="App">
      <p>Here's your puzzle progress so far. Keep it up!</p>
      {reward}
    </div>
  );
}

export default PuzzleProgress;
