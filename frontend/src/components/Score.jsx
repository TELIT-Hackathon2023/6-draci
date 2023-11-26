import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'

const Score = (props) => {

  return (
        <div id='score-box'>
            <div className='score'>
            <h1>Score {props.score}</h1>
            </div>
            
        </div>
  );
};

export default Score;