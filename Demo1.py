class std:
    def __init__(self,name,course,branch,city):
        self.branch = branch
        self.course = course
        self.name = name
        self.city = city
        print(f"Name: {self.name} Course: {self.course} Branch: {self.branch}")


obj = std("John","B.Tech","CSE","Jaipur")