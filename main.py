from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class Classify(Resource):
    def get(self,transactionName):
        return {'name':transactionName,'class':'food'}

api.add_resource(Classify,"/Classify/<string:transactionName>")

if __name__ == "__main__":
    app.run(debug=True)