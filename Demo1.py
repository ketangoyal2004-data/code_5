class std:
    def __init__(self,name,course,branch):
        self.branch = branch
        self.course = course
        self.name = name
        print(f"Name: {self.name} Course: {self.course} Branch: {self.branch}")

obj = std("John","B.Tech","CSE")