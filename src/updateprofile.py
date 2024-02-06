import tornado.web
import json

class UpdateProfileHandler(tornado.web.RequestHandler):
    def post(self):
        # Extract form data
        fname = self.get_argument("fname")
        lname = self.get_argument("lname")
        birthdate = self.get_argument("birthdate")
        ppic = self.request.files.get("ppic", None)  # Handle uploaded picture if any

        # Process the received data (e.g., update database)
        # Handle uploaded picture (e.g., save to server)

        # Respond with a success message
        response_data = {"status": "success"}
        self.write(json.dumps(response_data))
