class student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def introduce(self):
        print("大家好")
        print(f"我是{self.name}")
        print(f"我今年{self.age}岁")
        print(f"我的成绩是{self.score}分")
s1=student("Tom",18,30)
s1.introduce()


contacts=[]
class contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def show(self):
        print(f"姓名:{self.name}")
        print(f"电话:{self.phone}")
        print(f"邮箱:{self.email}")
contacts.append(contact("Tom","123","a@qq.com"))
contacts.append(contact("Jack","456","b@qq.com"))
for person in contacts:
    person.show()
    print('')

class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def show(self):
        print(f"书名:{self.title}")
        print(f"作者:{self.author}")
        print(f"价格:{self.price}")
    def discount(self,rate):
        self.price=self.price*rate
