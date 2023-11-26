import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'
import UploadFile from './UploadFile';

const AdminPanel = () => {

  return (
      <>
      <Header />
      <UploadFile/>
      </>
  );
};

export default AdminPanel;