from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

courses = {1: {"name": "Python", "videos": 15}, 
           2: {"name": "Java", "videos": 10}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("videos", type=int)

class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else: 
            return courses[course_id]

    def post(self, course_id):
        courses[course_id] = parser.parse_args()
        return courses
    
    def put(self, course_id):
        courses[course_id] = parser.parse_args()
        return courses

    def delete(self, course_id):
        del courses[course_id]
        return courses

api.add_resource(Main, "/api/courses/<int:course_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")