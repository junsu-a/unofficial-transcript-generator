import React, { useState } from "react";
import axios from "axios";

function Home() {
  const [pdfFile, setPdfFile] = useState(null);
  const [pages, setPages] = useState(null);

  const handleFileChange = (event) => {
    setPdfFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!pdfFile) return;

    const formData = new FormData();
    formData.append("file", pdfFile);

    try {
      const response = await axios.post(
        "http://localhost:8000/upload",
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
