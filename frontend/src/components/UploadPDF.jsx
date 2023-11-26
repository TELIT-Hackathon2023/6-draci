import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header';

const UploadPDF = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    
    if (!selectedFile) {
      alert('Please select a file.');
      return;
    }

    try {
      const formData = new FormData();
      formData.append('pdfFile', selectedFile);

      const response = await axios.post('http://127.0.0.1:5000/upload', formData);

      console.log('Upload success:', response.data);
    } catch (error) {
      console.error('Upload failed:', error.message);
    }
  };

  return (
        <div id='upload-box'>
        <div className='box'>
            <h1>Upload PDF</h1>
            <div className='button-and-input'>
                <input type="file" accept=".pdf" name="file" onChange={handleFileChange} />
                <button onClick={handleUpload}>Upload</button>
            </div>
        </div>
        </div>
  );
};

export default UploadPDF;