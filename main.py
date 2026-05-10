import os,time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class todo_user:
    
    def __init__(self,name,id):
        self.__d = dict()
        self.uid = id
        self.name = name
        self.__d[-1] = -1
        self.update_dict()

        
    def view(self):
        print("\n\nTask\n----")
        if not self.__d:
            print("<no task>")

        for i in self.__d:
            print(str(i) + "> " + str(self.__d[i]))
        print("\n\n")

    def add(self,task):
        if(self.__d.keys()):
            self.__d[list(self.__d.keys())[-1]+1] = task
        else:
            self.__d[1] = task
        self.update_dict()

    def update(self,t_id):
        if(t_id in self.__d):
            print("\n\nOld = " + self.__d[id] + "\n")
            self.__d[t_id] = input("Update Task = ").strip()
            self.update_dict()
        else:
            print("\n\nIncorrect Task ID\n")
            input("Press Enter to Continue...")

    def delete(self,t_id):
        self.__d.pop(t_id,"")
        self.update_dict()

    def update_dict(self):

        if -1 in self.__d.keys():
            self.__d.pop(-1)
            f = open(f"{str(self.uid)}.txt","a+")
            f.seek(0)
            if not f.read(): 
                f.write(f"{self.name}\n")
            f.seek(0)
            d0 = f.readlines()[1:]
            f.close()
            for i in d0:
                self.__d[int(i[0:i.find(',')])] = i[i.find(',')+1:][0:-1]
        else:
            d2 = []
            k = 1
            for i in self.__d:
                d2.append(str(k) + "," + self.__d[i] + "\n")
                k += 1
            f = open(f"{str(self.uid)}.txt","w")
            f.writelines(list(self.name+"\n") + d2)
            f.close()
            self.__d = dict()
            self.__d[-1] = [-1]
            self.update_dict()
        
        
        

def app(usr):
    clear_screen()

    print(f"\n\nLogging In as {usr.name}...")
    time.sleep(3)
    clear_screen()
        
    ch = ''

    while(1):
        clear_screen()
        print(f"TO-DO List Application\nUser = {usr.name}\n\nUID = {usr.uid}\n")
        print("Commands\n--------\nv          -    View Task\na <task>   -    Add Task\nu <id>     -    Update Task\nd <id>     -    Delete Task\ne          -    Logout\n\n")
            
        if not ch:
            ch = ' '
            
        match ch[0]:
            case ' ':
                ch = ' '
            case 'v':
                usr.view()
            case 'a':
                usr.add(ch[1:].strip())
            case 'u':
                usr.update(int(ch[1:].strip()))
                ch = ''
            case 'd':
                usr.delete(int(ch[1:].strip()))
            case 'e':
                break
            case _:
                print("Wrong Command!!")
                time.sleep(2)

        if not ch:
            continue
        ch = input("Enter command = ").strip().lower()
        
    clear_screen()     



def signup(name):
    u = dict()
    f = open("u_list.txt","a+")
    f.seek(0)
    if not f.read(): 
        f.write("0\n")
    f.seek(0)
    u0 = f.readlines()[1:]
    f.close()
    for i in u0:
        u[int(i[0:i.find(',')])] = i[i.find(',')+1:][0:-1]
    
    if(u.keys()):
        u[list(u.keys())[-1]+1] = name
    else:
        u[0] = name

    uid = list(u.keys())[-1]

    u2 = []
    for i in u:
        u2.append(str(i) + "," + u[i] + "\n")

    f = open("u_list.txt","w")
    f.writelines(list(str(len(u2)) + "\n") + u2)
    f.close()

    print(f"Name = {name} \nUID = {uid}\n\n")
    input("Press Enter to Continue...")


def login(id):
    u = dict()
    f = open("u_list.txt","a+")
    f.seek(0)
    if not f.read(): 
        f.write("0\n")
    f.seek(0)
    u0 = f.readlines()[1:]
    f.close()
    for i in u0:
        u[int(i[0:i.find(',')])] = i[i.find(',')+1:][0:-1]
    
    if(id in u):
        return [u[id],id]
    else: 
        return list()



def start():
    clear_screen()

    print("\n\nEntering TO-DO List Application...")
    time.sleep(3)
    clear_screen()
        
    ch = ''

    while(1):
        clear_screen()
        print(f"TO-DO List Application Login Window\n")
        print("Commands\n--------\ns <name>    -    Sign Up\nl <uid>     -    Login\ne           -    Exit\n\n")
            
        if not ch:
            ch = ' '
            
        match ch[0].lower():
            case ' ':
                ch = ' '
            case 's':
                signup(ch[1:].strip())
                ch = ''
            case 'l':
                data = login(int(ch[1:].strip()))

                if(data):
                    user = todo_user(data[0],data[1])
                    app(user)
                else:
                    print("USER NOT FOUND\n")
                    input("Press Enter to Continue...\n\n\n")

                ch = ''
            case 'e':
                break
            case _:
                print("Wrong Command!!")
                time.sleep(2)

        if not ch:
            continue
        ch = input("Enter command = ").strip()
        
    clear_screen()


if __name__ == "__main__":
    start()