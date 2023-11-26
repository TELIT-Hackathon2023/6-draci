import React, { useState } from 'react';
import axios from 'axios';
import Header from './Header'
import Data from './Data'
import UploadPDF from './UploadPDF';
import Score from './Score';
import Mdashboard from './Mdashboard';
import Summary from './Summary';
import { Link,Route, Routes } from 'react-router-dom';

const skuskaJson = {
        "response_schemas": [
          {"name": "problem_statement", "data": "A brief overview of the issue or need that the RFP aims to address. This sets the foundation for the proposed solution."},
          {"name": "scope_of_work", "data": "Defines the project's boundaries, detailing what tasks will be undertaken and the expected outcomes."},
          {"name": "required_technology_stack", "data": "Lists the essential technology tools, frameworks, and languages needed to successfully complete the project."},
          {"name": "pricing_model", "data": "Outlines the approach to calculating and charging for the work, whether it's Time and Materials (T&M) or a Fixed Price."},
          {"name": "service_level_agreements", "data": "Specifies the agreed-upon levels of service performance, availability, and potential penalties for non-compliance."},
          {"name": "selection_criteria", "data": "Defines the standards or requirements that proposals must meet to be considered for selection in the evaluation process."},
          {"name": "timelines", "data": "Highlights key dates and milestones crucial to the RFP processing schedule, providing a timeline for project completion."},
          {"name": "contact_details", "data": "Includes information for the point of contact, such as name, address, phone number, and email, ensuring effective communication."},
          {"name": "penalty_clauses", "data": "Specifies conditions under which penalties may be applied if the contractor fails to meet the terms of the contract."},
          {"name": "required_offer_type", "data": "Addresses whether the proposals are legally binding and the specific conditions under which they may or may not be binding."},
        ]
}

const Dashboard = () => {

  return (
    <div>
        <Header />
        <div className='upload-and-score'>
            <UploadPDF />
            <Score score="--"/>
        </div>
        <Mdashboard 
            tech = "5"
            func = "0"
            domain = "0"
            comp = "0"
        />
        <Summary 
            
        />
    </div>
  );
};

export default Dashboard;