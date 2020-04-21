import React from 'react';
import '../css/navbar.scss'
import {
  NavLink
} from "react-router-dom";

function NavBar() {
  return (
    <div className="nav">
      <NavLink to="/" className="logo">brevi</NavLink>
      <div className="right-nav">
        <NavLink to="/about" activeClassName="active-link">about</NavLink>
        <NavLink to="/">
          <div className="cta-button">
            contact
          </div>
        </NavLink>
      </div>
    </div>
  );
}

export default NavBar;
