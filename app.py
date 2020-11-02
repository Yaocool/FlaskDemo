from app.user_blueprint import app
from db.users import engine, Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run()
