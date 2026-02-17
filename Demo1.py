class std:
    def __init__(self,name,course,branch,city,country):
        self.branch = branch
        self.course = course
        self.name = name
        self.city = city
        self.country = country
        print(f"Name: {self.name} Course: {self.course} Branch: {self.branch} City:{self.city}")


obj = std("John","B.Tech","CSE","Jaipur")