from flask import request, jsonify
from flask_restful import Resource
from configs.dbconfig import db
from models.UserModel import UserModel
from schemas.UserSchema import UserSchema, user_schema, users_schema
from utils.utils import Token

import bcrypt
import uuid

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

    isEmailExists = UserModel.query.filter_by(email=data['email']).first()

    if isEmailExists:
      return { 'message': 'Email is already been taken!' }, 403

    passs = data['password'].encode('utf-8')

    hashPassword = bcrypt.hashpw(passs, bcrypt.gensalt())

    public_id = str(uuid.uuid4())
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    username = data['username']
    password = hashPassword

    new_user = UserModel(public_id, first_name, last_name, email, username, password)

    db.session.add(new_user)
    db.session.commit()

    userResult = user_schema.dump(new_user)

    token = Token()

    token.jit = new_user.public_id
    token.email = new_user.email

    tokens = token.generate_token()

    return { 'status': 'success', 'token': tokens }, 201