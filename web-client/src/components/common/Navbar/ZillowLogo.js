// <!-- Designed by Vexels.com - 2016 All Rights Reserved - https://vexels.com/terms-and-conditions/  -->

import React from "react";
import PropTypes from "prop-types";

const ZillowLogo = ({ routeToLanding, cssClass }) => (
  <svg
    viewBox="0 0 111 90"
    className={cssClass}
    xmlns="http://www.w3.org/2000/svg"
    onClick={routeToLanding}
  >
    <path
      d="M60,1L78,14C78,13,58,15,28,24ZM81,16L109,36L91,37L88,46C87,46,71,45,44,54L81,16L78,14Z"
      fill="#5577bb"
    />
    <path
      d="M7,87C36,74,78,71,78,71L84,56C82,57,58,55,12,73ZM13,70L59,25L12,39L3,50L20,47Z"
      fill="#88bb44"
    />
  </svg>
);

ZillowLogo.propTypes = {
  cssClass: PropTypes.string.isRequired,
  routeToLanding: PropTypes.func.isRequired
};

export default ZillowLogo;
