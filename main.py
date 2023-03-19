# write your code h
msg_0 = 'Enter an equation'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
M = 0
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0,msg_1,msg_2,msg_3,msg_4,msg_5,msg_6,msg_7,msg_8,msg_9,msg_10,msg_11,msg_12]

def is_one_digit(v1):
    return True if (-10<float(v1)<10 and float(v1).is_integer()) else False

        
def check(v1, v2, v3):
    msg=''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == '1' or v2 == '2') and v3 == "*":
        msg = msg + msg_7
    if (v1 == '0' or v2 == '0') and ( v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)
                    
    
def calc(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    
while True:
    
    print(msg_0)
    a,oper,b = input().split(' ')
    
    try:
        if (float(M+1 if a=='M' else float(a)+1) and float(M+1 if b=='M' else float(b)+1)) and (oper == '+' or oper =='-' or oper == '*' or oper == '/'):   
            try:
                check(str(M) if a=='M' else a,str(M) if b=='M' else b,oper)
                print(float(calc(float(M if a=='M' else a) ,oper,float(M if b=='M' else b))))
                # if a == 'M' or b == 'M' and oper == '-':
                #     print(abs(float(calc(float(M if a=='M' else a) ,oper,float(M if b=='M' else b)))))
                # else:
                #     print(float(calc(float(M if a=='M' else a) ,oper,float(M if b=='M' else b))))
                
                
                while 1:
                    print(msg_4)
                    ans = input()
                    if ans == 'y':
                        if is_one_digit(float(calc(float(a if a!='M' else M) ,oper,float(b if b!='M' else M)))):
                            msg_index = 10
                            while True:
                                print(msg_[msg_index])
                                global asn1
                                asn1 = input()
                                if asn1 == 'y':
                                    if msg_index < 12:
                                        msg_index+=1
                                        continue
                                    else:
                                        M = float(calc(float(a if a!='M' else M) ,oper,float(b if b!='M' else M)))
                                        break
                                elif asn1 != 'n':
                                    continue
                                else:
                                    break
                        else:
                            M = float(calc(float(a if a!='M' else M) ,oper,float(b if b!='M' else M)))
                               
                            
                    elif ans != 'n':
                        continue
                    while 1:
                        print(msg_5)
                        answ = input()
                        if answ == 'y':
                            break
                        elif answ != 'n':
                            continue
                        break
                    break
                if answ == 'n':
                    break
            except Exception as e:
                print(msg_3)
        else:
            print(msg_2)
            
    except Exception:
        print(msg_1)
