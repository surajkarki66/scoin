from flask import Flask

import config


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = config.DEBUG

    return app
