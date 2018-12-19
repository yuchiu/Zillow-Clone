import React from "react";
import SearchBar from "./SearchBar";

import "./index.scss";

const LandingPage = () => (
  <div className="landing-page page-wrapper">
    <div className="search-section">
      <div className="search-section-title">Find your way home</div>
      <SearchBar />
    </div>
  </div>
);

export default LandingPage;
