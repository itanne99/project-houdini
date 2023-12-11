import { Navbar, Container, Nav, Dropdown, ButtonGroup } from "react-bootstrap";
import { Link } from "react-router-dom";

const navItems = [
  {
    title: "Search",
    href: "/Search",
    dropdown: [
      { label: "Action 1", href: "/action1" },
      { label: "Action 2", href: "/action2" },
      { label: "Action 3", href: "/action3" },
    ],
  },
  { label: "About", href: "/about" },
  { label: "Resources", href: "/resources" },
  { label: "Donate", href: "/donate" },
];

const generateNavItems = (items) => {
  return items.map((item, indexA) => {
    if (item.dropdown) {
      return (
        <Dropdown id={item.id || indexA} key={item.id} as={ButtonGroup}>
          <Nav.Link to={item.href} key={item.id} className="pe-0" as={Link}>
            {item.title}
          </Nav.Link>
          <Dropdown.Toggle
            split
            variant="primary"
            id={item.id || indexA}
            as={Nav.Link}
          />
          <Dropdown.Menu>
            {item.dropdown.map((dropdownItem, indexB) => (
              <Dropdown.Item
                to={dropdownItem.href}
                key={dropdownItem.id || `${item.id || indexA}-${indexB}`}
                as={Link}
              >
                {dropdownItem.label}
              </Dropdown.Item>
            ))}
          </Dropdown.Menu>
        </Dropdown>
      );
    } else {
      return (
        <Nav.Link to={item.href} key={item.id} as={Link}>
          {item.label}
        </Nav.Link>
      );
    }
  });
};

const Header = () => {
  return (
    <Navbar expand="lg" bg="primary" data-bs-theme="dark">
      <Container>
        <Nav.Link to="/" as={Link}>
          <Navbar.Brand>
            <img
              alt=""
              src="/img/logo.svg"
              width="30"
              height="30"
              className="d-inline-block align-top"
            />{" "}
            React Bootstrap
          </Navbar.Brand>
        </Nav.Link>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">{generateNavItems(navItems)}</Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

Header.propTypes = {};

export default Header;