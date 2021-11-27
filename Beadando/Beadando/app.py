from flask import Flask
from server_controller import server_api

app = Flask(__name__)
app.register_blueprint(server_api)


@app.route("/", methods=["GET"])
def print_homepage_message():
    return "<h1>Welcome guardian!</h1> <h2>This is the homepage</h2>"


app.run()
