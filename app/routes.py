from app import app
from flask_restful import Resource, Api
from app import get_topics

api = Api(app)

class getTopics(Resource):

    def get(self, passion_and_topic):
        passion_and_topic = passion_and_topic.split(",")     
        return get_topics.get_topics_list(passion_and_topic)



api.add_resource(getTopics, "/<string:passion_and_topic>")
