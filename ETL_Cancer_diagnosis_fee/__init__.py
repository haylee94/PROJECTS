from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)

    from flask_app.model import model
    from flask_app.model import predict
    app.register_blueprint(model.bp)
    app.register_blueprint(predict.bp)

    return app
