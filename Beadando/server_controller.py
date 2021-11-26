from flask import Blueprint, request, Response, render_template, make_response
import server_service as service

server_api = Blueprint('server_controller', __name__)


@server_api.route('/add_data', methods=['POST'])
def receive_data():
    data_received = request.get_json()

    if "name" not in data_received or "Hits" not in data_received:
        return Response("Bad arguments", 400)
    print(data_received)
    service.push_to_database(data_received)
    return Response("Data received successfully", 200)


@server_api.route('/get_data', methods=["GET"])
def return_data():
    last_element = service.query_last_element()
    print(last_element)
    return Response(last_element, 200)


@server_api.route('/get_dataAll', methods=["GET"])
def return_dataAll():
    all_element = service.query_last_element()
    print(all_element)
    return Response(all_element, 200)
