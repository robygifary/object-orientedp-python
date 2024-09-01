class Game:
  def __init__(self, title, price) -> None:
    self.title = title
    self.price = price

  def info(self):
    def print_title():
      return f"Title : {self.title}"

    def print_price():
      return f"Price : {self.price}"

    return print_title

oby = Game("NFS Wanted", 76)
title = oby.info()
print(title())
