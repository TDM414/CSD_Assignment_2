from controller.DataStructure import LinkedList
from time import sleep

def str_split(data, key):
    list_str = LinkedList()
    Str = ''
    if key == "":
        for char in data:
            list_str.append(char)
        return list_str    
    else:
        index_check = 0
        while index_check < len(data):
            if data[index_check] == key[0] and index_check + len(key)-1 < len(data):
                check_key_in_data = True
                for x in range(len(key)):
                    if data[index_check+x] != key[x]:
                        check_key_in_data = False
                        break
                
                if check_key_in_data == False:
                    Str += data[index_check]
                    index_check += 1
                else: 
                    list_str.append(Str)
                    Str = ""
                    index_check += len(key)
            else:
                Str += data[index_check]
                index_check += 1

        list_str.append(Str)
        return list_str  

def Print(Str, End='\n', time=0.015):
    for c in Str:
        print(c, end='', flush=True)
        sleep(time)
    print(End, end='')

def Input(Str) -> str:
    Print(Str, End='')
    return input()

    