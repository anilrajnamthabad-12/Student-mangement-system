class student:
    def __init__(self,id,name,age,place):
        self.id=id
        self.name=name
        self.age=age
        self.place=place
    def display_details(self):
        print("ID",self.id)
        print("NAME",self.name)
        print("AGE",self.age)
        print("PLACE",self.place)
class studentmanagement:
    def __init__(self):
        self.student=[]
    def add_student(self):
        id=input('enter id:')
        name=input('enter name:')
        age=input('enter age:')
        place=input('enter place :')
        s = student(id,name,age,place)
        self.student.append(s)
        print('stundent success  added')
    def view(self):
        if len(self.student)==0:
            print('empty ')
        else:
            for i in self.student:
                i.display_details()
    def search(self):
        user_search=input('enter search id :')
        if len(self.student)==0:
            print('empty list')
        else:
            for i in self.student:
                    if i.id==user_search:
                     i.display_details()
                     print('student found')
                     break
            else:
                print('NOT Found')
    def updates(self):
        user_update_id=input("enter ID_u :")
        for u in self.student:
            if u.id==user_update_id:
                user_update_name=input("enter name_u :")
                user_update_age=input("enter age_u :")
                user_update_place=input("enter place_u :")    
                u.name=user_update_name
                u.age=user_update_age
                u.place=user_update_place
                u.display_details()
                print('student found')
                break
        else:
            print("sundent not found")
    def delete(self):
        user_d=input('enter id :')
        for d in self.student:
            if d.id==user_d:
                self.student.remove(d)
                print('deleted student')
                break
        else:
            print('student not foud') 
    def menu(self):    
        while True:
            print("\n1.add,2.view,3.search,4.update,5.delete,6.exit")
            ch=input("choose :")
            if ch=='1':
                s.add_student()
            elif ch=='2':
                s.view()
            elif ch=='3':
                s.search()
            elif ch=='4':
                s.updates()
            elif ch=='5':
                s.delete()
            elif ch=='6':
                break
            else:
                print('invalid choice')
s=studentmanagement()
s.menu()