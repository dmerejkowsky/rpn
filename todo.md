# TODO

* Replace Repository with a real implementation for persistent storage (we can keep the current Repository
  for tests)
* Fix the `create_app` factory to add support for test and production configuration, possibly using dotenv
* Return 409 conflict if trying to create two tasks with the same ID
* Fix handling of bad requests so that they are more usable as a Rest API:
   * Use content-type `application/json`, not `text/html`
   * Make sure errors are returned like `{"error": {"code": ..., "details": ...}}`
* Improve validation of requests
* Add CI/CD
* Add swagger definition (written by hand) or generate it with flask-swagger?
