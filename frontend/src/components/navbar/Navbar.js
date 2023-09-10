import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Contact from "./Contact";
import AboutUs from "./AboutUs";
import Home from "./Home";
import Layout from "./Layout";
import "./Navbar.css";
import logo from '../../assets/logo.png';

const Navbar = () => {
    return (
        <BrowserRouter>
            <div className="navbar">
                <div className="navbar__links">
                    <div className="navbar__links_logo">
                        <img src={logo} alt="logo" />
                    </div>
                    <div className="navbar__links_container">
                        <a href="/">Home</a>
                        <a href="/about">About Us</a>
                        <a href="/contact">Contact</a>
                    </div>
                </div>
                <Routes>
                    <Route path="/" element={<Layout />}>
                        <Route index element={<Home />} />
                        <Route path="contact" element={<Contact />} />
                        <Route path="*" element={<AboutUs />} />
                    </Route>
                </Routes>
            </div>
        </BrowserRouter>
    )
}

export default Navbar