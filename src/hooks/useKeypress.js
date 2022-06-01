import { useState, useEffect } from 'react';

// This represents the key press hook for getting the character of the key the user presses
const useKeyPress = callback => {
  // Create a state for the pressed key
  const [keyPressed, setKeyPressed] = useState();

  // Update the key pressed
  useEffect(() => {
    // When the key is pressed down, update the key pressed if it isn't the same key being held
    // for longer, or a non-character key like shift
    const downHandler = ({ key }) => {
      if (keyPressed !== key && key.length === 1) {
        setKeyPressed(key);
        callback && callback(key);
      }
    };

    // When the key is up (released from the press), set the key pressed to null
    const upHandler = () => {
      setKeyPressed(null);
    };

    // Listen for the keydown and keyup events from the browser window for the handlers
    window.addEventListener('keydown', downHandler);
    window.addEventListener('keyup', upHandler);

    // Clean up the handlers
    return () => {
      window.removeEventListener('keydown', downHandler);
      window.removeEventListener('keyup', upHandler);
    };
  });
  
  return keyPressed;
};

export default useKeyPress;
