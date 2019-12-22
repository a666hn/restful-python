from configs.dbconfig import db

class UserModel(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String)
  email = db.Column(db.String)
  username = db.Column(db.String)
  password = db.Column(db.String)

  def __init__(self, first_name, last_name, email, username, password):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.username = username
    self.password = password