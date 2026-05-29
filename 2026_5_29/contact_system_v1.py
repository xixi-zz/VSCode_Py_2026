import os
import json
def clear():
    os.system("clear")
def load_contacts(contacts):#加载
    try:
        with open("contacts.json","r") as file:
            data=json.load(file)
            contacts.extend(data)
    except FileNotFoundError:
        return
def save_contacts(contacts):#保存  
    with open("contacts.json","w") as file:
        json.dump(contacts,file, ensure_ascii=False, indent=4)
def add_contact(contacts):#添加联系人  
    names={person['name'].lower() for person in contacts}
    phones={person['phone'] for person in contacts}
    emails={person['email'] for person in contacts}
    while True:
        print("如要退出在任意输入时输入Exit或其首字母")
        while True:
            name=input("请输入要添加联系人名字:").strip()
            if not name:
                print("待添加联系人名字不能为空")
                continue
            if name.lower() in ("exit","e"):
                print("退出成功")
                return
            if name.lower() in names:
                print("此名字已存在,请重新输入")
                continue
            else:
                names.add(name.lower())
                break
        while True:
            phone=input("请输入要添加联系人电话:").strip()
            if not phone:
                print("待添加联系人电话不能为空")
                continue
            if phone.lower() in ("exit","e"):
                print("退出成功")
                return
            if phone in phones:
                print("此电话已存在,请重新输入")
                continue
            else:
                phones.add(phone)
                break
        while True:
            email=input("请输入要添加联系人邮箱:").strip()
            if not email:
                print("待添加联系人邮箱不能为空")
                continue
            if email.lower() in ("exit","e"):
                print("退出成功")
                return
            if email in emails:
                print("此邮箱已存在,请重新输入")
                continue
            else:
                emails.add(email)
                break
        contacts.append({'name':name,'phone':phone,'email':email})
        print("添加成功")        
def delete_contact(contacts):#删除
    while True:
        print("如要退出在任意输入时输入Exit或其首字母")
        name=input("请输入要删除联系人名字:").strip().lower()
        if not name:
            print("待删除联系人名字不能为空")
            continue
        if name.lower() in ("exit","e"):
            print("退出成功")
            return
        findflag=False
        deleteflag=False
        for person in contacts:
            if name==person['name'].lower():
                contacts.remove(person)
                print("删除成功")
                deleteflag=True
                break
            elif name in person['name'].lower():
                print(person['name'])
                findflag=True
        if deleteflag:
            continue
        if findflag:
            print("已显示所有相关联系人")
            continue
        if not deleteflag and not findflag:
            print("暂无相关联系人")
            continue
def update_contact(contacts):#替换
    while True:
        names={person['name'].lower() for person in contacts}
        phones={person['phone'] for person in contacts}
        emails={person['email'] for person in contacts}
        print("如要退出在任意输入时输入Exit或其首字母")
        updateflag=False
        name=input("请输入要修改的联系人").lower().strip()
        if not name:
            print("暂无相关联系人")
            continue
        if name in ("exit","e"):
            print("退出成功")
            return
        for person in contacts:
            if name==person["name"].lower():
                names.remove(person['name'].lower())
                phones.remove(person['phone'])
                emails.remove(person['email'])
                while True:
                    newname=input("请输入修改后的名字:").strip()
                    if not newname:
                        print("修改后的名字不能为空")
                        continue
                    if newname.lower() in ("exit","e"):
                        return
                    if newname.lower() in names:
                        print("此名字已存在")
                        continue
                    else:
                        break#修改后的名字可行直接退出输入名字的循环
                while True:
                    newphone=input("请输入修改后的电话:").strip()
                    if not newphone:
                        print("修改后的电话不能为空")
                        continue
                    if newphone.lower() in ("exit","e"):
                        return
                    if newphone in phones:
                        print("此电话已存在")
                        continue
                    else:
                        break
                while True:
                    newemail=input("请输入修改后的邮箱:").strip()
                    if not newemail:
                        print("修改后的邮箱不能为空")
                        continue
                    if newemail.lower() in ("exit","e"):
                        return
                    if newemail in emails:
                        print("此邮箱已存在")
                        continue
                    else:
                        break
                person["name"]=newname
                person["phone"]=newphone
                person["email"]=newemail
                print("修改成功")
                updateflag=True
                break
        if updateflag:
            continue
        findflag=False
        for person in contacts:
            if name in person["name"].lower():
                print(person["name"])
                findflag=True
        if findflag:
            print("已显示所有相关联系人")
            continue
        if not updateflag and not findflag:
            print("暂无相关联系人")   
def search_contact(contacts):#查找
    while True:
        print("如要退出在任意输入时输入Exit或其首字母")
        name=input("请输入要查找的联系人名字:").lower().strip()
        if not name:
            print("暂无相关联系人")
            continue
        if name in ("exit","e"):
            print("退出成功")
            return
        searchflag=False
        for person in contacts:
            if name==person["name"].lower():
                print("查找成功")
                print(f"name:{person['name']} "
                    f"phone:{person['phone']} "
                    f"email:{person['email']}"
                    )
                searchflag=True
                break
        if searchflag:
            continue
        findflag=False
        for person in contacts:
            if name in person["name"].lower():
                print(person["name"])
                findflag=True
        if findflag:
            print("已显示所有相关联系人,请再次输入以获取详细信息")
            continue
        if not searchflag and not findflag:
            print("暂无相关联系人信息")
            continue
def view_contacts(contacts):#查看
    if not contacts:
        print("暂无任何联系人信息")
        return
    for person in contacts:
        print(f"name:{person['name']} "
            f"phone:{person['phone']} "
            f"email:{person['email']}"
            ) 
def main():
    contacts=[]
    load_contacts(contacts)
    while True:
        clear()
        print("---------通讯录---------")
        print("-----输入add添加联系人----")
        print("---输入delete删除联系人---")
        print("---输入update修改联系人---")
        print("---输入search查找联系人---")
        print("-----输入view查看联系人---")
        print("------输入exit退出-------")
        print("----可输入首字母执行操作---")
        choice=input("请选择你要执行的操作:").lower().strip()
        if choice in ("exit","e"):
            save_contacts(contacts)
            print("退出成功")
            return
        elif choice in ("add","a"):
            add_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("delete","d"):
            delete_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("update","u"):
            update_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("search","s"):
            search_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("view","v"):
            view_contacts(contacts)
            input("请输入回车返回菜单...")
        else:
            print("输入错误,请重新输入...")
            input("请输入回车返回菜单...")
main()

