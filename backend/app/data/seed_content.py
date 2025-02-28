from app import db
from app.models.content import Content

def seed_content():
    dummy_content = [
        Content(
            type='video',
            title='Best Pizza Spots in Dyker Heights',
            creator='Brooklyn Food Guide',
            thumbnail='https://images.unsplash.com/photo-1513104890138-7c749659a591',
            video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            upvotes=245,
            downvotes=12
        ),
        Content(
            type='blog',
            title='Hidden Gems of Dyker Heights',
            creator='Local Explorer',
            content="""
            Dyker Heights is famous for its Christmas lights, but there's so much more to discover!
            
            1. Authentic Italian Bakeries
            - Mona Lisa Pastry Shop
            - Villabate Alba
            
            2. Local Parks
            - Dyker Beach Park
            - McKinley Park
            
            3. Shopping Districts
            - 13th Avenue Shopping Strip
            - 86th Street Shopping
            """,
            upvotes=189,
            downvotes=5
        ),
        Content(
            type='image',
            title='Sunset at Dyker Beach Golf Course',
            creator='NYC Photography',
            image_url='https://images.unsplash.com/photo-1572491769738-23bcba94e2a4',
            upvotes=421,
            downvotes=15
        )
    ]
    
    for content in dummy_content:
        db.session.add(content)
    
    db.session.commit()