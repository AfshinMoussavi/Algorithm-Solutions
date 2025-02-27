# Name: دیجی کالا
# URL:  https://quera.org/problemset/21206


from models import Product, User
from datetime import datetime


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if product not in self.products or self.products[product] < amount:
            raise ValueError("Not Enough Products")
        
        self.products[product] -= amount
        if self.products[product] == 0:
            del self.products[product]

    def add_user(self, username):
        if username in [user.username for user in self.users]:
            return None
        
        user = User(username)
        self.users.append(user)
        return username

    def get_total_asset(self):
        return sum(product.price * amount for product, amount in self.products.items())

    def get_total_profit(self):
        return sum(product.price for user in self.users for product in user.bought_products)
        
        
    def get_comments_by_user(self, user):
        return [comment.text for product in self.products for comment in product.comments if comment.user == user]

    def get_inflation_affected_product_names(self):
        product_prices = {}
        affected_products = set()
        
        for product in self.products:
            if product.name in product_prices:
                product_prices[product.name].append(product.price)
            else:
                product_prices[product.name] = [product.price]
        
        for name, prices in product_prices.items():
            if len(prices) > 1 and min(prices) < max(prices):
                affected_products.add(name)
        
        return list(affected_products)


    def clean_old_comments(self, date:datetime):
        for product in self.products:
            product.comments = [comment for comment in product.comments if comment.date_added >= date]

    def get_comments_by_bought_users(self, product):
        bought_users = [user for user in self.users if product in user.bought_products]
        return [comment.text for comment in product.comments if comment.user in bought_users]
