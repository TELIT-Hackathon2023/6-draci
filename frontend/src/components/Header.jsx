import React from 'react';
import { Link,Route, Routes } from 'react-router-dom';

const Header = () => {

  return (
    <div className='header'>
      <section id="top-bar">
            <p className='admin'><Link to="/">Sales CoPilot</Link></p>
            <p className='admin'><Link to="./adminpanel">Admin panel</Link></p>
      </section>
    </div>
  );
};

export default Header;