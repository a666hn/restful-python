import jwt

class Token:
  def generate_token(self):
    obj = {
      "jit": self.jit,
      "sub": self.email,
      "iss": "https://coder-eternity.com"
    }

    token = jwt.encode(obj, 'supersecret', algorithm='HS256').decode('utf-8')

    return token