from flask import Blueprint, request, Response, render_template, make_response

server_api = Blueprint('server_controller', __name__)


@server_api.route('/add_data', methods=['POST'])
def receive_data():
    data_received = request.get_json()

    if "name" not in data_received or "hits" not in data_received:
        return Response("Bad arguments", 400)
    print(data_received)
    return Response("Data received successfully", 200)

