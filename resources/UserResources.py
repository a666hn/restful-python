from flask import request, jsonify
from flask_restful import Resource
from configs.dbconfig import db
from models.UserModel import UserModel
from schemas.UserSchema import UserSchema, user_schema, users_schema

class GetAllUser(Resource):
  def get(self):
    Users = UserModel.query.all()

    userResult = users_schema.dump(Users)

    return { 'status': 'success', 'data': userResult }, 200

class AddNewUser(Resource):
  def post(self):
    data = request.json

    if not data:
      return { 'messages': 'No data input provided' }, 400

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    username = data['username']
    password = data['password']

    new_user = UserModel(first_name, last_name, email, username, password)

    db.session.add(new_user)
    db.session.commit()

    userResult = user_schema.dump(new_user)

    return { 'status': 'success', 'data': userResult }, 201