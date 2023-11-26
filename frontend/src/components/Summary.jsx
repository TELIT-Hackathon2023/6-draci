import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'

const Mdashboard = (props) => {

  return (
    <div className='summary-box'>
    <div className='summary'>
        <h1>Summary</h1>
        <div>
        <p>PROBLEM STATEMENT: {props.ps}</p>
        <p>SCOPE OF THE WORK: {props.sotw}</p>
        <p>REQUIRED TECHNOLOGY STACK: {props.rts}</p>
        <p>PRICING MODEL: {props.pm}</p>
        <p>SERVICE LEVEL AGREEMENTS (SLAS): {props.sla}</p>
        <p>SELECTION CRITERIA: {props.sc}</p>
        <p>TIMELINES: {props.t}</p>
        <p>CONTACT DETAILS: {props.cd}</p>
        <p>PENALTY CLAUSES: {props.pc}</p>
        <p>REQUIRED OFFER TYPE (BINDING OR NON-BINDING): {props.rot}</p>
        </div>
    </div>
</div>
  );
};

export default Mdashboard;