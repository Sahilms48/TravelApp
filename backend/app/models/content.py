from datetime import datetime
from app import db

class Content(db.Model):
    __tablename__ = 'contents'
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    creator = db.Column(db.String(100), nullable=False)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # For video content
    thumbnail = db.Column(db.String(500))
    video_url = db.Column(db.String(500))
    
    # For blog content
    content = db.Column(db.Text)
    
    # For image content
    image_url = db.Column(db.String(500))

    def to_dict(self):
        data = {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'creator': self.creator,
            'upvotes': self.upvotes,
            'downvotes': self.downvotes,
            'created_at': self.created_at.isoformat()
        }
        
        if self.type == 'video':
            data.update({
                'thumbnail': self.thumbnail,
                'video_url': self.video_url
            })
        elif self.type == 'blog':
            data.update({
                'content': self.content
            })
        elif self.type == 'image':
            data.update({
                'image_url': self.image_url
            })
            
        return data