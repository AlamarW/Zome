import pytest
import json
import tempfile
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)


"""
# SQLAlchemy Note model
class NoteModel(db.Model):
    __tablename__ = 'notes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text,
            'date_created': self.date_created.isoformat(),
            'date_edited': self.date_edited.isoformat()
        }
"""


# Flask API endpoints
@app.route("/notes", methods=["POST"])
def create_note(client):
    from flask import request, jsonify
    from models.note import Note

    data = request.get_json()

    # Use domain model for validation
    domain_note = Note()
    domain_note.set_name(data.get("name", ""))
    domain_note.set_text(data.get("text", ""))

    # Create SQLAlchemy model
    db_note = NoteModel(name=domain_note.get_name(), text=domain_note.get_text())

    db.session.add(db_note)
    db.session.commit()

    return jsonify(db_note.to_dict()), 201


"""
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    from flask import jsonify
    
    note = NoteModel.query.get_or_404(note_id)
    return jsonify(note.to_dict())

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    from flask import request, jsonify
    from models.note import Note
    
    data = request.get_json()
    note = NoteModel.query.get_or_404(note_id)
    
    # Use domain model for validation
    domain_note = Note()
    if 'name' in data:
        domain_note.set_name(data['name'])
        note.name = domain_note.get_name()
    
    if 'text' in data:
        domain_note.set_text(data['text'])
        note.text = domain_note.get_text()
    
    note.date_edited = datetime.utcnow()
    db.session.commit()
    
    return jsonify(note.to_dict())

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    from flask import jsonify
    
    note = NoteModel.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    
    return '', 204

@app.route('/notes', methods=['GET'])
def list_notes():
    from flask import jsonify
    
    notes = NoteModel.query.all()
    return jsonify([note.to_dict() for note in notes])

# Functional test class
class TestNoteCRUDFunctional:
    
    @pytest.fixture
    def client(self):
        with app.test_client() as client:
            with app.app_context():
                db.create_all()
                yield client
                db.drop_all()
    
    def test_full_note_crud_cycle(self, client):
        #Test complete CRUD operations for notes from Flask API to SQLAlchemy to database
        
        # CREATE - Test creating a new note
        note_data = {
            'name': 'Machine Learning Notes',
            'text': 'Machine learning involves algorithms that learn from data. Neural networks are a subset of machine learning techniques.'
        }
        
        response = client.post('/notes', 
                              data=json.dumps(note_data),
                              content_type='application/json')
        
        assert response.status_code == 201
        created_note = json.loads(response.data)
        assert created_note['name'] == note_data['name']
        assert created_note['text'] == note_data['text']
        assert 'id' in created_note
        assert 'date_created' in created_note
        assert 'date_edited' in created_note
        
        note_id = created_note['id']
        
        # READ - Test retrieving the created note
        response = client.get(f'/notes/{note_id}')
        assert response.status_code == 200
        retrieved_note = json.loads(response.data)
        assert retrieved_note['id'] == note_id
        assert retrieved_note['name'] == note_data['name']
        assert retrieved_note['text'] == note_data['text']
        
        # UPDATE - Test updating the note
        updated_data = {
            'name': 'Advanced ML Notes',
            'text': 'Deep learning is a subset of machine learning using neural networks with multiple layers. It excels at pattern recognition tasks.'
        }
        
        response = client.put(f'/notes/{note_id}',
                             data=json.dumps(updated_data),
                             content_type='application/json')
        
        assert response.status_code == 200
        updated_note = json.loads(response.data)
        assert updated_note['id'] == note_id
        assert updated_note['name'] == updated_data['name']
        assert updated_note['text'] == updated_data['text']
        # Verify date_edited was updated
        assert updated_note['date_edited'] != created_note['date_edited']
        
        # READ after UPDATE - Verify persistence
        response = client.get(f'/notes/{note_id}')
        assert response.status_code == 200
        verified_note = json.loads(response.data)
        assert verified_note['name'] == updated_data['name']
        assert verified_note['text'] == updated_data['text']
        
        # LIST - Test listing all notes
        response = client.get('/notes')
        assert response.status_code == 200
        notes_list = json.loads(response.data)
        assert len(notes_list) == 1
        assert notes_list[0]['id'] == note_id
        
        # DELETE - Test deleting the note
        response = client.delete(f'/notes/{note_id}')
        assert response.status_code == 204
        
        # Verify deletion - should return 404
        response = client.get(f'/notes/{note_id}')
        assert response.status_code == 404
        
        # Verify empty list after deletion
        response = client.get('/notes')
        assert response.status_code == 200
        notes_list = json.loads(response.data)
        assert len(notes_list) == 0
    
    def test_domain_model_validation_in_api(self, client):
        #Test that domain model validation is enforced through the API
        
        # Test invalid name (contains forbidden characters)
        invalid_note_data = {
            'name': 'Invalid@Name#',
            'text': 'Valid text content'
        }
        
        response = client.post('/notes',
                              data=json.dumps(invalid_note_data),
                              content_type='application/json')
        
        assert response.status_code == 400 or response.status_code == 500
        
        # Test invalid text type
        invalid_text_data = {
            'name': 'Valid Name',
            'text': 123  # Should be string
        }
        
        response = client.post('/notes',
                              data=json.dumps(invalid_text_data),
                              content_type='application/json')
        
        assert response.status_code == 400 or response.status_code == 500
    
    def test_multiple_notes_operations(self, client):
        #Test operations with multiple notes to verify database persistence
        
        # Create multiple notes
        notes_data = [
            {'name': 'Python Notes', 'text': 'Python is a versatile programming language'},
            {'name': 'JavaScript Notes', 'text': 'JavaScript runs in browsers and servers'},
            {'name': 'Database Notes', 'text': 'SQL databases provide ACID guarantees'}
        ]
        
        created_ids = []
        for note_data in notes_data:
            response = client.post('/notes',
                                  data=json.dumps(note_data),
                                  content_type='application/json')
            assert response.status_code == 201
            created_note = json.loads(response.data)
            created_ids.append(created_note['id'])
        
        # Verify all notes exist
        response = client.get('/notes')
        assert response.status_code == 200
        all_notes = json.loads(response.data)
        assert len(all_notes) == 3
        
        # Update each note
        for i, note_id in enumerate(created_ids):
            updated_data = {
                'text': f'Updated content for note {i+1}'
            }
            response = client.put(f'/notes/{note_id}',
                                 data=json.dumps(updated_data),
                                 content_type='application/json')
            assert response.status_code == 200
        
        # Verify updates persisted
        for note_id in created_ids:
            response = client.get(f'/notes/{note_id}')
            assert response.status_code == 200
            note = json.loads(response.data)
            assert 'Updated content' in note['text']
        
        # Delete one note and verify others remain
        response = client.delete(f'/notes/{created_ids[0]}')
        assert response.status_code == 204
        
        response = client.get('/notes')
        assert response.status_code == 200
        remaining_notes = json.loads(response.data)
        assert len(remaining_notes) == 2
        
        # Verify correct notes remain
        remaining_ids = [note['id'] for note in remaining_notes]
        assert created_ids[0] not in remaining_ids
        assert created_ids[1] in remaining_ids
        assert created_ids[2] in remaining_ids
"""

