import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
function App() {
  return (
    <div className="App">
      <Router>
        <Link to="/" > Test </Link>
      </Router>
      <h1> Hello World! </h1>
    </div>
  );
}

export default App;
