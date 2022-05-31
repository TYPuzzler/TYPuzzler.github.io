import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import PuzzleReward from './pages/PuzzleReward';
import PuzzleProgress from './pages/PuzzleProgress';
import Typing from './pages/Typing';

function Main() {
  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path='/typing' element={<Typing />} />
      <Route path='/puzzleprogress' element={<PuzzleProgress />} />
      <Route path='/puzzlereward' element={<PuzzleReward />} />
    </Routes>
  );
}

export default Main;