from app import app, db
from models import User, Content, Skill

with app.app_context():
    # Create the database and tables
    db.create_all()

    # Create a default user
    admin = User(username='admin', password='admin')
    db.session.add(admin)

    # Create default content
    content = Content(about_me="Informacje o mnie...")
    db.session.add(content)

    # Create default skills
    skills = [
        Skill(name='python', info='Skill info', image='python.png'),
        Skill(name='discord', info='Informacje o umiejętnościach', image='discord.png'),
        Skill(name='html', info='Informacje o umiejętnościach', image='html.png'),
        Skill(name='db', info='Informacje o umiejętnościach', image='db.webp')
    ]
    db.session.add_all(skills)

    # Commit changes
    db.session.commit()
