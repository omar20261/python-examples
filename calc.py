def num(msg):
    while True:
        x=raw_input(msg)
        try:
            x = int(x);
            break
        except ValueError:
            print("invaild input");
    print("num = {} , type = {}").format(x,type(x));
    return x;

def opera(x,y,msg):
    while True:
        operation = raw_input(msg)
        if(operation == '*'):
          re = x*y;
          break
        elif(operation == '/'):
          re = x/y;
          break
        elif(operation == '-'):
          re = x-y;
          break
        elif(operation == '+'):
          re = x+y;
          break
        else:
            print("invaild operation");
    return re;

def Again():
    while True:
        val = raw_input("again (y/n):");
        if(val == 'y'):
            calc();
            break
        elif(val == 'n'):
            print("---- the end ----")
            break
        else:
            raw_input("again (y/n):");

def calc():
        x = num("fisrt number:");
        y = num("second number:");
        print("the result = {}").format(opera(x,y,"operation:"));
        Again();

calc();
