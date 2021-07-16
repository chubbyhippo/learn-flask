from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    @staticmethod
    def get():
        return {'hello': 'world'}


@api.route('/<string:input_str>')
class SimpleInput(Resource):
    @staticmethod
    def get(input_str: str):
        return {'hello': input_str}


if __name__ == '__main__':
    app.run(debug=True)
