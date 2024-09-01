class User:
  total = 0

  def __init__(self, name, email, role):
    self.name = name
    self.email = email
    self.__role = role
    User.total += 1

  def info(self):
    return f"{self.name} - {self.email} - {self.__role}"

  @property
  def role(self):
    return self.__role

  @role.setter
  def role(self, new_role):
    if self.__role != "user":
      self.__role = new_role

  @classmethod
  def setTotal(cls, total):
    cls.total = total

  @classmethod
  def from_string(cls, str_param):
    name, email, role = str_param.split("-")
    return cls(name, email, role)

  @staticmethod
  def tweet(tweet):
    return tweet

oby = User("Robby", "robby@gmail.com", "moderator")
str_param = "robby-robby@gmail.com-admin"
oby_update = User.from_string(str_param)

tweet = User.tweet("Hallo sedang belajar OOP python")
print(tweet)

print(oby_update.info())

