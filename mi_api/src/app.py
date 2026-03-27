"""
Módulo principal de la aplicación Flask.
Define los endpoints del API REST.
"""

from flask import Flask, request, jsonify
from src.service import create_item_service, get_items_service, delete_item_service

app = Flask(__name__)


@app.route('/items', methods=['POST'])
def create_item():
    """Crea un nuevo item."""
    item = request.json
    result = create_item_service(item)
    return jsonify(result), 201


@app.route('/items', methods=['GET'])
def get_items():
    """Obtiene todos los items."""
    return jsonify(get_items_service())


@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    """Elimina un item por índice."""
    success = delete_item_service(index)
    if success:
        return '', 204
    return 'Not found', 404