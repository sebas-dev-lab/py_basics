from composite import Composite
from article import Article


class Box(Composite):
    def __init__(self):
        super().__init__()
        self.name = "box"
        
        
class Bread(Article):
    def __init__(self):
        super().__init__()
        self.set_price(25)
        self.set_name('bread')


class Soda(Article):
    def __init__(self):
        super().__init__()
        self.set_price(15)
        self.set_name('soda')




ppalBox = Box()
sodaBox = Box()

ppalBox.add_articles(Soda())
ppalBox.add_articles(Bread())
sodaBox.add_articles(Soda())
sodaBox.add_articles(Soda())
ppalBox.add_articles(sodaBox)


print(sodaBox.get_price())
print(ppalBox.get_price())
