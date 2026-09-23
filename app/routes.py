from flask import Blueprint, jsonify, request

from . import services

bp = Blueprint("api", __name__)


@bp.get("/health")
def health():
    return jsonify(services.get_health())


@bp.get("/api/hello")
def hello():
    return jsonify(services.get_hello())


@bp.get("/api/items")
def list_items():
    return jsonify(services.list_items())


@bp.post("/api/items")
def create_item():
    data = request.get_json(silent=True)

    try:
        item = services.create_item(data)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(item), 201
