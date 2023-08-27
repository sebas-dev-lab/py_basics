class Article:
    def __init__(self) -> None:
        self.price = None
        self.name = None
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def set_name(self, name):
        self.name = name
        
    def set_price(self, price):
        self.price = price
        
        
        