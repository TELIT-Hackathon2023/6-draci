import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'
import FillBar from './FillBar';

const Mdashboard = (props) => {

  return (
    
    <div className='mdash-box'>
        <div className='mdash'>
            <h1>Matching Dashboard</h1>
            <div className='scores'>
                
                <p>Technical Matching Score 
                <FillBar fillPercentage={props.tech} />
                </p>
                <p>Function Matching Score
                <FillBar fillPercentage={props.func} />
                </p>
                <p>Domain Matching Score
                <FillBar fillPercentage={props.domain} />
                </p>
                <p>Compliance Matching Score
                <FillBar fillPercentage={props.comp} />
                </p>
            </div>
        </div>
    </div>
  );
};

export default Mdashboard;