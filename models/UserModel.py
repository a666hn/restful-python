from configs.dbconfig import db

class UserModel(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String, unique=True, nullable=False)
  first_name = db.Column(db.String(25), nullable=False)
  last_name = db.Column(db.String(25))
  email = db.Column(db.String(50))
  username = db.Column(db.String(15))
  password = db.Column(db.String)

  def __init__(self, public_id, first_name, last_name, email, username, password):
    self.public_id = public_id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.username = username
    self.password = password