import React from "react";
import ReactDOM from "react-dom/client";
import "bootswatch/dist/journal/bootstrap.min.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/home";
import ErrorPage from "./pages/ErrorHandlers/ErrorPage";
import Header from "./components/Header/Header";
import App from "./App";
import NotFound from "./pages/ErrorHandlers/NotFound";

const routes = [
  {
    path: "/",
    element: <Home />,
    errorElement: <ErrorPage />,
  },
  {
    path: "*",
    element: <NotFound />,
  },
];

const createRoutes = (routes) => {
  if (!Array.isArray(routes)) {
    throw new Error("Routes parameter must be an array");
  }

  return routes.map((route) => {
    if (!route.path || !route.element) {
      throw new Error("Each route must have a 'path' and 'element' property");
    }

    return (
      <Route
        key={route.path}
        path={route.path}
        element={route.element}
        errorElement={route.errorElement} // Use fallback prop instead of errorElement
      />
    );
  });
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Header />
      <App>
        <Routes>{createRoutes(routes)}</Routes>
      </App>
    </BrowserRouter>
  </React.StrictMode>
);

//{createRoutes(routes)}
