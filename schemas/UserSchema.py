from configs.schemaconfig import ma

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'first_name', 'last_name', 'email', 'username' 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)