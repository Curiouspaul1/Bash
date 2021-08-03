from flask_migrate import Migrate
from bammysite import __call__,db
import os

app = __call__(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        app=app
    )

if __name__ == '__main__':
    app.run()
