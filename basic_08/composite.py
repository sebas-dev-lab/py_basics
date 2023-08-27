from article import Article

class Composite(Article):
    def __init__(self):
        super().__init__()
        self.articles = []
    
    def add_articles(self, article):
        self.articles.append(article)
    
    def get_price(self):
        return sum(article.get_price() for article in self.articles)