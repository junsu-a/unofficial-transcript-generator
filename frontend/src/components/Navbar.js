import React from "react";
import { Link } from "react-router-dom";
import GitHubButton from "react-github-btn";

const Navbar = () => {
  return (
    <nav className="nav">
      <Link to="/" className="site-title">
        Home
      </Link>
      <ul>
        <li>
          <Link to="/guide">Guide</Link>
        </li>
        <li>
          <a href="https://github.com/anjjunsu/unofficial-transcript-generator/issues">
            Bug Report
          </a>
        </li>
        <li>
          <GitHubButton
            href="https://github.com/anjjunsu/unofficial-transcript-generator"
            data-icon="octicon-star"
            data-size="large"
            data-show-count="true"
            aria-label="Star anjjunsu/unofficial-transcript-generator on GitHub"
          >
            Star
          </GitHubButton>
        </li>
        <li>
          <Link to="/contact">Contact</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
