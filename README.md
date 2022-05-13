# form-creator-client
A client for form-creator-server app.

Features:
- Renders form by UID;
- Submits form data.
- Renders all data for a given form UID.

Provides three methods to interact with server-side API:
- `get_form(uid)` - renders form.
- `post_form(uid, data)` - submits form data to server and returns data UID.
- `get_form_data(uid)` - renders all data of a form.
