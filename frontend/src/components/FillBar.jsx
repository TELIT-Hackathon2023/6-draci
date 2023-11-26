import React from 'react';

const FillBar = ({ fillPercentage }) => {
  const fillBarStyle = {
    width: `${fillPercentage}%`,
  };

  return (
    <div className="progress-bar">
        <div className="progress-bar-fill" style={fillBarStyle}></div>
    </div>
  );
};

export default FillBar;