from flask import Flask
from app.routes.todos import todo_bp
from app.core.metrics import init_metrics
from app.utils.logger import setup_logger
from app.db.database import init_db

def create_app():
    app = Flask(__name__)

    setup_logger()
    init_db()
    init_metrics(app)

    app.register_blueprint(todo_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)