import os,time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def view(d):
    print("\n\nTask\n----")
    if not d:
        print("<no task>")

    for i in d:
        print(str(i) + "> " + str(d[i]))
    print("\n\n")

def add(d,task):
    d[list(d.keys())[-1]+1] = task
    return d

def update(d,id):
    print("\n\nOld = " + d[id] + "\n")
    d[id] = input("Update Task = ").strip()
    return d

def delete(d,id):
    d.pop(id,"")
    return d

def init(d):
    clear_screen()

    print("\n\nEntering TO-DO List Application...")
    time.sleep(3)
    clear_screen()
    
    ch = ''

    while(1):
        clear_screen()
        print("TO-DO List Application")
        print("Commands\n--------\nv          -    View Task\na <task>   -    Add Task\nu <id>     -    Update Task\nd <id>     -    Delete Task\ne          -    Exit\n\n")
        
        if not ch:
            ch = ' '
        
        match ch[0]:
            case ' ':
                ch = ' '
            case 'v':
                view(d)
            case 'a':
                d = add(d,ch[1:].strip())
            case 'u':
                d = update(d,int(ch[1:].strip()))
                ch = ''
            case 'd':
                d = delete(d,int(ch[1:].strip()))
            case 'e':
                break
            case _:
                print("Wrong Command!!")
                time.sleep(2)

        if not ch:
            continue
        ch = input("Enter command = ").strip().lower()
    
    clear_screen()
    return d





if __name__ == "__main__":

    f = open("data.txt","a+")
    f.seek(0)
    if not f.read(): 
        f.write("0\n")
    
    f.seek(0)
    d = f.readlines()[1:]
    f.close()

    d1 = dict()

    for i in d:
        d1[int(i[0:i.find(',')])] = i[i.find(',')+1:][0:-1]

    d1 = init(d1)
    
    d2 = []

    k = 1
    for i in d1:
        d2.append(str(k) + "," + d1[i] + "\n")
        k += 1
    f = open("data.txt","w")
    f.writelines(list(str(len(d2))+"\n") + d2)
    f.close()