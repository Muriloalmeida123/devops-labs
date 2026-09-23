"""Camada de serviços: regras de negócio simples, sem banco de dados."""

_items = []
_next_id = 1


def get_health():
    return {"status": "ok"}


def get_hello():
    return {"message": "Hello from DevOps API"}


def list_items():
    return _items


def create_item(data):
    global _next_id

    if not data or "name" not in data:
        raise ValueError("Field 'name' is required")

    item = {"id": _next_id, "name": data["name"]}
    _items.append(item)
    _next_id += 1

    return item
