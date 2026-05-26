def load_people(people):
    with open("student_system.txt","r") as file:
        lines=file.readlines()
        if not lines:
            return
        else:
            for line in lines:
                part=line.split()
                name=part[0].split(":")[1]
                age=part[1].split(":")[1]
                number=part[2].split(":")[1]
                people.append({'name':name,'age':int(age),'number':number})
            return
def add_people(people):
    name=input("Name:")
    if not people:
        people.append({'name':name,'age':int(input("Age:")),'number':input("Number:")})
    else:
        for person in people:
            if person['name']==name:
                print("此名字已经在系统中")
                break
        else:
            people.append({'name':name,'age':int(input("Age:")),'number':input("Number:")})
def update_people(people):
     name=input("Name:")
     for person in people:
         if person['name']==name:
            person['name']=input("newname:")
            person['age']=int(input("newage:"))
            person['number']=input("newnumber:")
            print("修改成功")
            break
     else:
        print("库中不存在这个人")
def delete_people(people):
    name=input("Name:")
    for person in people:
        if person['name']==name:
            people.remove(person)
            print("删除成功")
            break
    else:
        print("库中不存在这个人")
def search_people(people):
    name=input("Name:")
    for person in people:
        if person['name']==name:
            print(f"Name:{person['name']} Age:{person['age']} Number:{person['number']}")
            break
    else:
        print("库中不存在这个人")
def view_people(people):
    if not people :
        print("库中暂无数据")
    else:
        for person in people:
            print(f"Name:{person['name']} Age:{person['age']} Number:{person['number']}")
def save_people(people):
    with open("student_system.txt","w") as file:
        for person in people:
            file.write(
                f"Name:{person['name']} "
                f"Age:{person['age']} " 
                f"Number:{person['number']}\n"
                )
def main():
    people=[]
    load_people(people)
    while True:
        print("-----学生信息档案表-----")
        print("------输入exit退出-----")
        print("----输入add添加信息-----")
        print("----输入update修改信息---")
        print("---输入delete删除信息---")
        print("---输入search查找某人信息--")
        print("--输入view查看所有信息---")
        print("可输入首字母来表示想要的操作")
        choice=input("请做出选择:").lower().strip()
        if choice in ("exit","e"):
            print("退出成功")
            save_people(people)
            break
        elif choice in ("add","a"):
            add_people(people)
            input("按回车返回菜单...")
        elif choice in ("update","u"):
            update_people(people)
            input("按回车返回菜单...")
        elif choice in ("delete","d"):
            delete_people(people)
            input("按回车返回菜单...")
        elif choice in ("search","s"):
            search_people(people)
            input("按回车返回菜单...")
        elif choice in ("view","v"):
            view_people(people)
            input("按回车返回菜单...")
main()
        
