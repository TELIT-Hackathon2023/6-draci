import { useState } from 'react'
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import UploadPDF from './components/UploadPDF'

const App = () => {
  return (
    
      <div id="app">
        <h1>Sales CoPilot</h1>
        <UploadPDF />
      </div>
  
  );
};

export default App
