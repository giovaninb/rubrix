export default ({ $auth, route, redirect }) => {
  switch (route.path) {
    case "/login":
      break;
    default:
      if (!$auth.loggedIn) {
        const REDIRECT_URL =
          "/login?redirect=" + encodeURIComponent(route.fullPath);
        redirect(REDIRECT_URL);
      }
  }
};
