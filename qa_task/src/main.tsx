import React from "react";
import ReactDOM from "react-dom/client";
import Root, { createContactAction, rootLoader } from "./routes/Root.tsx";
import { createBrowserRouter, redirect, RouterProvider } from "react-router-dom";
import ErrorPage from "./ErrorPage.tsx";
import Contact, { contactLoader, favoriteAction } from "./routes/Contact.tsx";
import EditContact, { editAction } from "./routes/Edit.tsx";
import { destroyContactAction } from "./routes/Destroy.tsx";
import Index from "./routes/Index.tsx";
import Login, { loginAction, loginLoader } from "./routes/Login.tsx";
import Layout from "./Layout.tsx";

import "./index.css";
import { fakeAuthProvider } from "./auth.tsx";
const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    action: createContactAction,
    children: [
      {
        path: "login",
        action: loginAction,
        loader: loginLoader,
        Component: Login,
      },
      {
        path: "/logout",
        async action() {
          // We signout in a "resource route" that we can hit from a fetcher.Form
          await fakeAuthProvider.signout();
          return redirect("/login");
        },
      },
      {
        element: <Root />,
        loader: rootLoader,
        errorElement: <ErrorPage />,
        children: [
          { index: true, element: <Index /> },
          {
            path: "contacts/:contactId",
            element: <Contact />,
            loader: contactLoader,
            action: favoriteAction,
          },
          {
            path: "contacts/:contactId/edit",
            element: <EditContact />,
            loader: contactLoader,
            action: editAction,
          },
          {
            path: "contacts/:contactId/destroy",
            action: destroyContactAction,
          },
        ],
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
