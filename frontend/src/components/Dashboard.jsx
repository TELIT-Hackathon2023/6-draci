import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'
import UploadPDF from './UploadPDF';
import Score from './Score';
import Mdashboard from './Mdashboard';
import Summary from './Summary';
import { Link,Route, Routes } from 'react-router-dom';
import ResponseSchemas from './ResponseSchemas';
import io from 'socket.io-client';

const Dashboard = () => {

  const [jsonData, setJsonData] = useState({
    "response_schemas": [
      {"name": "problem_statement", "data": "YeS"},
      {"name": "scope_of_work", "data": "Defines the project's boundaries, detailing what tasks will be undertaken and the expected outcomes."},
      {"name": "required_technology_stack", "data": "Lists the essential technology tools, frameworks, and languages needed to successfully complete the project."},
      {"name": "pricing_model", "data": "Outlines the approach to calculating and charging for the work, whether it's Time and Materials (T&M) or a Fixed Price."},
      {"name": "service_level_agreements", "data": "Specifies the agreed-upon levels of service performance, availability, and potential penalties for non-compliance."},
      {"name": "selection_criteria", "data": "Defines the standards or requirements that proposals must meet to be considered for selection in the evaluation process."},
      {"name": "timelines", "data": "Highlights key dates and milestones crucial to the RFP processing schedule, providing a timeline for project completion."},
      {"name": "contact_details", "data": "Includes information for the point of contact, such as name, address, phone number, and email, ensuring effective communication."},
      {"name": "penalty_clauses", "data": "Specifies conditions under which penalties may be applied if the contractor fails to meet the terms of the contract."},
      {"name": "required_offer_type", "data": "Addresses whether the proposals are legally binding and the specific conditions under which they may or may not be binding."}
    ]
  });


  const socket = io('http://127.0.0.1:5000', { transports: ['websocket'] });

  socket.on('connection', ()=> {
    console.log("Pripojil som sa");
    socket.emit('connection', 'success');
  });
  socket.on('jsonData', (data) => {
    if(data != undefined){
      setJsonData(data)
    }
    
  });

  
  function poziadajJson() {
    socket.emit('sendJson', "now");
  }

  return (
    <div>
        <Header />
        <div className='upload-and-score'>
            <UploadPDF poziadajJson={poziadajJson}/>
            <Score score="--"/>
        </div>
        <Mdashboard 
            tech = "5"
            func = "0"
            domain = "0"
            comp = "0"
        />
        <div className='summary-box'>
          <div className='summary'>
            <h1>Summary</h1>
            
            <ResponseSchemas  responseData={jsonData} targetName="problem_statement" displayName="Problem Statement"/>
            <ResponseSchemas  responseData={jsonData} targetName="scope_of_work" displayName="Scope of Work"/>
            <ResponseSchemas  responseData={jsonData} targetName="required_technology_stack" displayName="Requiered Technology Stack"/>
            <ResponseSchemas  responseData={jsonData} targetName="pricing_model" displayName="Pricing Model"/>
            <ResponseSchemas  responseData={jsonData} targetName="service_level_agreements" displayName="Service Level Agreements"/>
            <ResponseSchemas  responseData={jsonData} targetName="selection_criteria" displayName="Selection Criteria"/>
            <ResponseSchemas  responseData={jsonData} targetName="timelines" displayName="Timelines"/>
            <ResponseSchemas  responseData={jsonData} targetName="contact_details" displayName="Contact Details"/>
            <ResponseSchemas  responseData={jsonData} targetName="penalty_clauses" displayName="Penalty Clauses"/>
            <ResponseSchemas  responseData={jsonData} targetName="required_offer_type" displayName="Required Offer Type"/>
            
          </div>
        </div>
    </div>
  );
};

export default Dashboard;