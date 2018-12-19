import React from "react";
import { withRouter } from "react-router-dom";

import ZillowLogo from "./ZillowLogo";
import "./index.scss";

class Navbar extends React.Component {
  routeToLanding = () => {
    const { history } = this.props;
    history.push("/");
  };

  routeToMyProfile = () => {
    const { history } = this.props;
    history.push("/");
  };

  render() {
    return (
      <nav className="navbar-wrapper">
        <div className="navbar-start">
          <ZillowLogo
            routeToLanding={this.routeToLanding}
            cssClass="navbar-start__item navbar-start--logo pointer-cursor"
          />
          <span
            className="navbar-start__item pointer-cursor no-highlight"
            onClick={this.routeToLanding}
          >
            Zillow Clone
          </span>
        </div>

        <div className="navbar-end">
          <div
            className="navbar-end__item pointer-cursor no-highlight"
            onClick={this.routeToMyProfile}
          >
            My Profile
          </div>
        </div>
      </nav>
    );
  }
}
export default withRouter(Navbar);
