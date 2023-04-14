import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Guide from "./Guide";
import Navbar from "./Navbar";
import Footer from "./Footer";

const AppRouter = () => {
  return (
    <Router basename="">
      <div id="page-container">
        <div id="content-wrap">
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/guide" element={<Guide />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
  );
};

export default AppRouter;
