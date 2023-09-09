import React from "react";

const Guide = () => {
  return (
    <section>
      <div className="general-text">
        <h1>User Guide</h1>
        <h3>For an accurate transcript, please follow the following steps</h3> 
        <ol>
          <li>Log into your Student Service Center
            <br></br>
            <a href="https://ssc.adm.ubc.ca/sscportal/servlets/SRVSSCFramework" target="_blank" rel="noopener noreferrer">UBC SSC</a>
          </li>
          <li>Navigate to Your Grades Summary</li>
          <li>Download PDF via Print located on the top-right
            <br></br>
          </li>
          <li>Submit PDF in the homepage</li>
          <li>Voilà!</li>
        </ol>
      </div>
    </section>
  );
};

export default Guide;
