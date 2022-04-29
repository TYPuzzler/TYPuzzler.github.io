import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import PuzzleInventory from './pages/PuzzleInventory';
import PuzzleSelect from './pages/PuzzleSelect';
import Typing from './pages/Typing';

function Main() {
  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path='/typing' element={<Typing />} />
      <Route path='/puzzleselect' element={<PuzzleSelect />} />
      <Route path='/puzzle' element={<PuzzleInventory />} />
    </Routes>
  );
}

export default Main;