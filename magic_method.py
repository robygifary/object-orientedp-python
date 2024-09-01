class Game:
  def __init__(self, title, price):
    self.title = title
    self.price = price

  def __str__(self) -> str:
    return f"{self.title} - ${self.price}"
  
  def __eq__(self, other) -> bool:
    return self.title == other.title
  
  def __gt__(self, other):
    return self.price > other.price

  def __add__(self, other):
    return self.price + other.price

oby = Game("NFS", 80)
oby2 = Game("NFS Wanted", 70)

print(oby + oby2)