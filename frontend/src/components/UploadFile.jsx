import React, { useState } from 'react';
import axios from 'axios';

const UploadFile = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [customFilename, setCustomFilename] = useState('');
  

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleCustomFilenameChange = (e) => {
    setCustomFilename(e.target.value);
  };

  const handleUpload = async () => {
    
    if (!selectedFile) {
      alert('Please select a file.');
      return;
    }

    try {
      const formData = new FormData();
      formData.append('txtFile', selectedFile);

      const response = await axios.post('http://127.0.0.1:5000/uploadtxt', formData);

      console.log('Upload success:', response.data);
    } catch (error) {
      console.error('Upload failed:', error.message);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleUpload();

    console.log('File:', selectedFile);
    console.log('Custom Filename:', customFilename);

    // Reset form state
    setSelectedFile(null);
    setCustomFilename('');
  };

  return (
    <div className='select'>
      <h2>Upload File <br></br>Form</h2>
      <form onSubmit={handleSubmit} encType="multipart/form-data">

        <label htmlFor="fileSelect">Select a File:</label>
        <input
          type="file"
          id="fileSelect"
          name="pdfFile"
          onChange={handleFileChange}
        />

        <br />

        

        <br />

        <input type="submit" value="Upload File" />
        
      </form>
    </div>
  );
};


export default UploadFile;