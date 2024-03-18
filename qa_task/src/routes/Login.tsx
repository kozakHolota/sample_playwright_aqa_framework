import {
  Form,
  LoaderFunctionArgs,
  redirect,
  useActionData,
  useLocation,
  useNavigation,
} from "react-router-dom";
import { fakeAuthProvider } from "../auth";

export async function loginLoader() {
  if (fakeAuthProvider.isAuthenticated) {
    return redirect("/");
  }
  return null;
}

export async function loginAction({ request }: LoaderFunctionArgs) {
  let formData = await request.formData();
  let username = formData.get("username") as string | null;
  let password = formData.get("password") as string | null;

  // Validate our form inputs and return validation errors via useActionData()
  if (!username) {
    return {
      error: "You must provide a username (test) to log in",
    };
  }

  if (!password) {
    return {
      error: "You must provide a password (test) to log in",
    };
  } else {
    password = password.trim();
  }

  if (username === "test" && (password === "test" || password.length === 0)) {
    // Sign in and redirect to the proper destination if successful.
    try {
      await fakeAuthProvider.signin(username);
    } catch (error) {
      // Unused as of now but this is how you would handle invalid
      // username/password combinations - just like validating the inputs
      // above
      return {
        error: "Invalid login attempt",
      };
    }
    let redirectTo = formData.get("redirectTo") as string | null;
    return redirect(redirectTo || "/");
  } else {
    return {
      error: "Invalid credentials. Username: test, Password: test",
    };
  }
}

export default function Login() {
  let location = useLocation();
  let params = new URLSearchParams(location.search);
  let from = params.get("from") || "/";

  let navigation = useNavigation();
  let isLoggingIn = navigation.formData?.get("username") != null;

  let actionData = useActionData() as { error: string } | undefined;

  return (
    <div className="login-mask">
      <Form method="post" replace>
        <input type="hidden" name="redirectTo" value={from} />
        <input
          id="username"
          name="username"
          placeholder="Username"
          data-testid="username"
        />
        <input
          id="password"
          name="password"
          type="password"
          placeholder="Password"
          data-testid="password"
        />
        <button type="submit" disabled={isLoggingIn} data-testid="signin">
          {isLoggingIn ? "Logging in..." : "Login"}
        </button>
        {actionData && actionData.error ? (
          <div className="error">{actionData.error}</div>
        ) : null}
      </Form>
    </div>
  );
}
