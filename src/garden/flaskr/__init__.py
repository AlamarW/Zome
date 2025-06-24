import os
import uuid
from flask import Flask, request, jsonify
from typing import Dict, Any
from garden.models.note import Note


def note_to_dict(note: Note) -> Dict[str, Any]:
    """Convert Note Domain object to dictionary for JSON"""
    return {
        "id": note.uuid,
        "name": note.name,
        "text": note.text,
        "created_at": note.date_created,
        "updated_at": note.date_edited,
    }


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/note")
    def client_test():
        return "TEST"

    @app.route("/note", methods=["POST"])
    def test_create_note():
        data = request.get_json()
        note = Note()
        note.set_name(data["name"])
        text = data.get("text", "")
        note.set_text(text)
        response_data = note_to_dict(note)

        return jsonify(response_data), 201

    return app
