import { Container } from "react-bootstrap";
import PropTypes from "prop-types";

const App = ({ children }) => {
  return (
    <Container
      fluid
      className="d-flex flex-column"
      style={{ minHeight: "90vh" }}
    >
      {children}
    </Container>
  );
};

App.propTypes = {
  children: PropTypes.node.isRequired,
};

export default App;
