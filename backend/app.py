import json
import uuid

from flask import Flask, Response, request

from utils import generate_file, read_file, generate_report

app = Flask(__name__)
api_root = "/api/v1"


@app.route(f"{api_root}/generate/", methods=["GET"])
def generate():
    """
    Generate file with 4 types (2MB file)
    :return: {
        "id": uuid,
        "file_name": uuid.txt,
        "link": http://127.0.0.1:5000/api/v1/download/uuid.txt,
        "report" : {
            "alpha_count": 1,
            "num_count": 1,
            "alpha_num_count": 1,
            "alpha_num_count": 1
        }
    }
    """
    _id = str(uuid.uuid4())

    # Generate function.
    file = generate_file(_id)

    data = dict()
    data["id"] = _id
    data["file_name"] = f"{_id}.txt"
    data["link"] = f"http://{request.host}/api/v1/download/{_id}.txt"
    data["report"] = file.get("report")

    response = app.response_class(
        response=json.dumps(data), status=200, mimetype="application/json"
    )
    return response


@app.route(f"{api_root}/download/<uid>.txt", methods=["GET"])
def download(uid):
    file = read_file(uid)

    if file:
        return Response(
            file,
            mimetype="text/plain",
            headers={"Content-Disposition": f"attachment;filename={uid}.txt"},
        )
    else:
        data = dict()
        data["error"] = "Not a valid URL"

        response = app.response_class(
            response=json.dumps(data), status=404, mimetype="application/json"
        )
        return response


@app.route(f"{api_root}/report/<uid>/", methods=["GET"])
def report(uid):
    """
    Return 4 type count.
    :return: {
        "file_name": uuid.txt,
        "report" : {
            "alpha_count": 1,
            "num_count": 1,
            "alpha_num_count": 1,
            "alpha_num_count": 1
        }
    }
    """
    data = dict()
    reports = generate_report(uid)

    if reports:
        data["file_name"] = f"{uid}.txt"
        data["report"] = reports.get("report")

        response = app.response_class(
            response=json.dumps(data), status=200, mimetype="application/json"
        )
        return response
    else:
        data = dict()
        data["error"] = "Not a valid UUID"

        response = app.response_class(
            response=json.dumps(data), status=404, mimetype="application/json"
        )
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
