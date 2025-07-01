import os
import json
import sqlalchemy as db
from flask import Flask, request, jsonify # type: ignore
from garden.domain_models.note import Note
from garden.models.note_model import NoteModel, db as sqlalchemy_db



def note_to_dict(note: Note) -> dict[str, object]:
    """Convert Note Domain object to dictionary for JSON"""
    return {
        "id": note.uuid,
        "name": note.name,
        "text": note.text,
        "created_at": note.date_created,
        "updated_at": note.date_edited,
        "high_frequency_words": note.high_frequency_words,
        "themes": note.themes

    }


def create_app(test_config: dict[str, object] | None=None)-> Flask:
    app = Flask(__name__, instance_relative_config=True)
    _ = app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
        SQLALCHEMY_DATABASE_URI="sqlite:///app.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    
    sqlalchemy_db.init_app(app)

    if test_config is None:
        _ = app.config.from_pyfile("config.py", silent=True)
    else:
       _ = app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        sqlalchemy_db.create_all()

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
        
        # Save to database
        note_model = NoteModel(
            id=str(note.uuid),
            name=note.name,
            text=note.text,
            created_at=note.date_created,
            updated_at=note.date_edited,
            high_frequency_words=json.dumps(note.high_frequency_words) if note.high_frequency_words else None,
            themes=json.dumps(note.themes) if note.themes else None
        )
        sqlalchemy_db.session.add(note_model)
        sqlalchemy_db.session.commit()

        response_data = note_to_dict(note)
        return jsonify(response_data), 201

    @app.route("/note/<string:name>")
    def get_note_by_name(name):
        note_model = sqlalchemy_db.session.query(NoteModel).filter(NoteModel.name == name).first()
        
        if not note_model:
            return jsonify({"error": "Note not found"}), 404
        
        # Convert NoteModel to Note domain object for consistency
        note = Note()
        note.uuid = note_model.id
        note.name = note_model.name
        note.text = note_model.text or ""
        note.date_created = note_model.created_at
        note.date_edited = note_model.updated_at
        note.high_frequency_words = json.loads(note_model.high_frequency_words) if note_model.high_frequency_words else {}
        note.themes = json.loads(note_model.themes) if note_model.themes else []
        
        response_data = note_to_dict(note)
        return jsonify(response_data), 200

    return app
