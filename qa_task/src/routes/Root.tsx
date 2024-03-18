import {
  Form,
  NavLink,
  Outlet,
  redirect,
  useFetcher,
  useLoaderData,
  useNavigation,
  useSubmit,
} from "react-router-dom";
import { ContactEntry, getContacts, createContact } from "../contacts";
import { fakeAuthProvider } from "../auth";

export async function rootLoader({ request }: any) {
  // If the user is not logged in and tries to access `/protected`, we redirect
  // them to `/login` with a `from` parameter that allows login to redirect back
  // to this page upon successful authentication
  if (!fakeAuthProvider.isAuthenticated) {
    let params = new URLSearchParams();
    params.set("from", new URL(request.url).pathname);
    return redirect("/login?" + params.toString());
  }

  const url = new URL(request.url);
  const query = url.searchParams.get("query");
  const contacts = await getContacts(query);
  return { contacts, query };
}

export async function createContactAction() {
  const contact = await createContact();
  return redirect(`/contacts/${contact.id}/edit`);
}

export default function Root() {
  const { contacts, query } = useLoaderData() as {
    contacts: Array<ContactEntry>;
    query: string | undefined;
  };
  const navigation = useNavigation();
  const submit = useSubmit();
  const fetcher = useFetcher();

  let isLoggingOut = fetcher.formData != null;

  const searching =
    navigation.location &&
    new URLSearchParams(navigation.location.search).has("query");

  // useEffect(() => {
  //   (document.getElementById("query")! as HTMLInputElement).value = query || "";
  // }, [query]);

  return (
    <>
      <div id="sidebar">
        <footer>
          WEINMANN QA Task{" "}
          <fetcher.Form method="post" action="/logout">
            <button type="submit" disabled={isLoggingOut} data-testid="signout">
              {isLoggingOut ? "Signing out..." : "Sign out"}
            </button>
          </fetcher.Form>
        </footer>
        <div>
          <Form id="search-form" role="search">
            <input
              id="query"
              aria-label="Search contacts"
              placeholder="Search"
              type="search"
              name="query"
              className={searching ? "loading" : ""}
              onChange={(event) => {
                const isFirstSearch = query == null;
                submit(event.currentTarget.form, {
                  replace: !isFirstSearch,
                });
              }}
            />
            <div id="search-spinner" aria-hidden hidden={!searching} />
            <div className="sr-only" aria-live="polite"></div>
          </Form>
          <Form method="post">
            <button type="submit" data-testid="new-contact">New</button>
          </Form>
        </div>
        <nav>
          {contacts.length ? (
            <ul>
              {contacts.map((contact) => (
                <li key={contact.id}>
                  <NavLink
                    to={`contacts/${contact.id}`}
                    className={({ isActive, isPending }) =>
                      isActive ? "active" : isPending ? "pending" : ""
                    }
                  >
                    {contact.first || contact.last ? (
                      <>
                        {contact.first} {contact.last}
                      </>
                    ) : (
                      <i>No Name</i>
                    )}{" "}
                    {contact.favorite && <span data-testid="favorized">★</span>}
                  </NavLink>
                </li>
              ))}
            </ul>
          ) : (
            <p>
              <i>No contacts</i>
            </p>
          )}
        </nav>
      </div>
      <div
        id="detail"
        className={navigation.state === "loading" ? "loading" : ""}
      >
        <Outlet />
      </div>
    </>
  );
}
