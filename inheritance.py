# inheritance, extande, override, polymorphism

class Employee:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def work(self):
    return f"{self.name} is working"

class Programmer(Employee):
  def __init__(self, name, email, level):
    super().__init__(name, email)
    self.level = level

  def debug(self):
    return "Debugging"
  
  def work(self):
    return f"{self.name} is writing code..."
  
class UiDesign(Employee):
  def __init__(self, name, email, level, tools):
    super().__init__(name, email)
    self.level = level
    self.tools = tools

  def work(self):
    return f"{self.name} is designing cool application..."
  

employee = Employee("Roby", "gifary@gmail.com")
programmer = Programmer("Tamara", "tamara@ac.id", "Junior")
ui_design = UiDesign("Jane", "jane@ymail.com", "senior", "Figma")

def working(system):
  print(system.work())

class Manager:
  def __init__(self, name):
    self.name = name

  def work(self):
    return f"{self.name} is presentation"

manager = Manager("Manager Harik")
working(manager)

