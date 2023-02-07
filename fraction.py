def mul(f1,f2):
    result = {}
    result['s'] = f1['s'] * f2['s']
    result['m'] = f1['m'] * f2['m']
    return result

def sum(f1,f2):
    result = {}
    result['s'] = (f1['s']*f2['m']) + (f1['m']*f2['s'])
    result['m'] = f1['m']*f2['m']
    return result

def sub(f1,f2):
    result = {}
    result['s'] = (f1['s']*f2['m']) - (f1['m']*f2['s'])
    result['m'] = f1['m']*f2['m']
    return result

def div(f1,f2):
    result = {}
    result['s'] = f1['s'] * f2['m']
    result['m'] = f1['m'] * f2['s']
    return result

def show(f):
    print(f['s'],'/',f['m'])

while True:
    f1_s= int(input("enter numerator of the first fraction: "))
    f1_m= int(input("enter denominator of the first fraction: "))
    f2_s= int(input("enter numerator of the second fraction: "))
    f2_m= int(input("enter denominator of the second fraction: "))

    a= {'s':f1_s, 'm':f1_m}
    b= {'s':f2_s, 'm':f2_m}
    show(a)
    show(b)
    confrimation= input("Is this correct?? y/n :")
    if confrimation == "y":
        op= input("enter an operation(* or + or - or /):")
        if op == "*":
            mul_result= mul(a , b)
            show(mul_result)

        if op == "+":
            sum_result= sum(a , b)
            show(sum_result)

        if op == "-":
            sub_result= sub(a , b)
            show(sub_result)

        if op == "/":
            div_result= div(a, b)
            show(div_result)
           
        
        exit= input("Would you like to continue(c) or exit(e) : ")
        if exit == "c":
            continue
        if exit == "e":
            break
        
    if confrimation == "n":
        continue