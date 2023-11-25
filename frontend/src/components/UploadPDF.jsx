import React, { useState } from 'react';
import axios from 'axios';

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
      formData.append('pdf', selectedFile);

      const response = await axios.post('YOUR_UPLOAD_URL', formData);

      console.log('Upload success:', response.data);
    } catch (error) {
      console.error('Upload failed:', error.message);
    }
  };

  return (
    <div>
      <h1>Upload PDF</h1>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default UploadPDF;