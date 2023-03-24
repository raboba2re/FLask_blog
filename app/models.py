from flask_sqlalchemy import SQLAlchemy
from app import db, app 
from datetime import datetime
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)
    
posts_tags  = db.Table('post-tags', 
                       db.Column('post_id',db.Integer, 
                        db.ForeignKey('post.id')),
                       db.Column('tag_id',db.Integer, 
                        db.ForeignKey('tag.id'))
                       
                       )
class Post(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    title = db.Column (db.String(140), nullable = False) 
    slug =  db.Column (db.String(140), unique = True, nullable = False)
    body = db.Column (db.Text, nullable = False)
    date_created = db. Column(db.DateTime, default=datetime.utcnow )
    tags = db.relationship('Tag', secondary = posts_tags, backref = db.backref('posts'), lazy= 'dynamic'
                           )
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()
        
    def generate_slug(self): 
        if self.title:
            self.slug = slugify(self.title)
            
    def __repr__(self) -> str:
        return f'<Post id: {self.id}, Post title: {self.title}>'

class Tag(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    title = db.Column (db.String(140), nullable = False) 
    slug =  db.Column (db.String(140), unique = True, nullable = False)
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.title)
        
    def __repr__(self) -> str:
        return f'<Tag Id:{self.id}, Title:{self.title}>'
    
    
with app.app_context():
    db.create_all()
