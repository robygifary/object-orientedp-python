
def info(func):
  def wrapper():
    print("*" * 10)
    func()
    print("#" * 10)
  return wrapper

@info
def say_hello():
  print("Hello World in Python")

say_hello()