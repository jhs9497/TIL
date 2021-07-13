import React from 'react';
import "./Home.css"
import { Button } from 'react-bootstrap'
import { Link } from 'react-router-dom';
  
  
function Home() {
  return (
    <div>
      <div className="jumbo"></div>
      <h2>Hi Hi ~</h2>
      <br/>
      <div>
        <Link to="login">
          <Button variant="info" size="lg">Login</Button>
        </Link>
      </div>
      <br/>
      <div>
        <Link to="signup">
          <Button variant="secondary" size="lg">Sign up</Button>
        </Link>
      </div>
    </div>

  )
}


export default Home;