from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, DateTime
from datetime import datetime 

db = SQLAlchemy()

class NoteModel(db.Model):
    __tablename__ = 'notes'
    
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    high_frequency_words: Mapped[str] = mapped_column(Text, nullable=True)
    themes: Mapped[str] = mapped_column(Text, nullable=True)
