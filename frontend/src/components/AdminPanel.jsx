import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'

const AdminPanel = () => {

  return (
    <div>
      <Header />
      <Data />
    </div>
  );
};

export default AdminPanel;