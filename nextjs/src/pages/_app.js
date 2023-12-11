import Header from "@/components/Header/Header";
import "bootswatch/dist/journal/bootstrap.min.css";
import { Container } from "react-bootstrap";

export default function App({ Component, pageProps }) {
  return (
    <>
      <Header />
      <Container
        fluid
        className="d-flex flex-column"
        style={{ minHeight: "90vh" }}
      >
        <Component {...pageProps} />
      </Container>
    </>
  );
}
