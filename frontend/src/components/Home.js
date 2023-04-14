import React, { useState, useEffect } from "react";
import axios from "axios";

function Home() {
  const url = "http://localhost:8000"
  const [pdfFile, setPdfFile] = useState(null);
  const [pages, setPages] = useState(null);
  const [totalStudentMoneySaved, setTotalStudentMoenySaved] = useState(null)

  useEffect(() => {
    const fetchTotalStudentMoneySaved = async () => {
      try {
        const response = await axios.get(url + "/total-student-money-saved")
        setTotalStudentMoenySaved(response.data);
      } catch (error) {
        console.error("Error fetching total student money saved data:", error);
      }
    };

    fetchTotalStudentMoneySaved();
  }, []);

  const handleFileChange = (event) => {
    setPdfFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!pdfFile) return;

    const formData = new FormData();
    formData.append("file", pdfFile);

    try {
      const response = await axios.post(
        url + "/upload",
        formData
      );
      setPages(response.data.pages);
    } catch (error) {
      console.error("Error uploading PDF:", error);
    }
  };

  return (
    <div className="Home">
      <header className="Home-header">
        <h1>PDF Uploader</h1>
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
        />
        <button onClick={handleUpload}>Upload PDF</button>
        {totalStudentMoneySaved != null && (
          <div>
            <h2>Total student money saved: ${totalStudentMoneySaved}</h2>
          </div>
        )}
        {pages && (
          <div>
            <h2>Extracted Text</h2>
            {pages.map((pageText, index) => (
              <div key={index}>
                <h3>Page {index + 1}</h3>
                <p>{pageText}</p>
              </div>
            ))}
          </div>
        )}
      </header>
    </div>
  );
}

export default Home;
