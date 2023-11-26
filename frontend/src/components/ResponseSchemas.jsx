import React from 'react';

const ResponseSchemas = ({ responseData, targetName, displayName }) => {
    const contactDetailsItem = responseData.response_schemas.find(item => item.name == targetName);

  return (
        <div className='response-schemas'>
        <p><b>{displayName} : </b></p>
        <p> {contactDetailsItem.data}</p>
        </div>
  );
};

export default ResponseSchemas;