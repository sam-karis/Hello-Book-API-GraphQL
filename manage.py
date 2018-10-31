import os
from flask_script import Manager, Shell
from app import create_app, db

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


manager = Manager(app)


if __name__ == '__main__':
    manager.run()
