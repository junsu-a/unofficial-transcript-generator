import React from "react";
// import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from './components/navbar/Layout.js';
import Home from "./components/navbar/Home.js";
import Contact from './components/navbar/Contact.js';
import AboutUs from "./components/navbar/AboutUs.js";
import "./App.css";


function App() {
  return (
    <div className="home">
      <div className="navbar">
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="contact" element={<Contact />} />
                <Route path="*" element={<AboutUs />} />
              </Route>
            </Routes>
          </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
