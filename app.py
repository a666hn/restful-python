from flask import Blueprint
from flask_restful import Api

# ### Import Routes API from Resources
from resources.UserResources import GetAllUser, AddNewUser

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


"""User API

   Methods : GET, POST, DELETE
"""
# ### Method = ['GET']
# ### End point = [baseUrl]/api/v1/resources/user/get
api.add_resource(GetAllUser, '/resources/user/get')

# ### Method = ['POST']
# ### End point = [baseUrl]/api/v1/resources/user/create
api.add_resource(AddNewUser, '/resources/user/create')

