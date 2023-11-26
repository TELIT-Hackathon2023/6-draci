import { useState } from 'react'
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import UploadPDF from './components/UploadPDF'
import AdminPanel from './components/AdminPanel'
import Dashboard from './components/Dashboard';

const App = () => {
  return (
    
      <div id="app">
        <Dashboard />
      </div>
  
  );
};

export default App
