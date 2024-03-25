'''def calculate(a):
    print(a*2)'''


#DOCKSTRING

'''def summer(arg1,arg2):
    """
    Sum of two variables

    Parameter/Args
    ----------
    arg1:int,float
    arg2:int,float
    ----------
    Returns:
      float,int arg1+arg2
    """
    print(arg1+arg2)

help(summer)'''

#Ön Tanımlı Fonksiyon

'''def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")'''

'''def calculate(warm,moisture,charge):
    print((warm + moisture)/charge)'''

'''def calculate(warm,moisture,charge):
    warm=warm*2
    moisture=moisture*2
    charge=charge*2
    output=(warm + moisture)/charge
    return warm,moisture,charge,output'''

def calculate(warm,moisture,charge):
    output=(warm + moisture)/charge
    return output

'''warm,moisture,charge,output =calculate(98,12,78)
print(calculate(98,12,78))'''

#Fonksiyon içerisinde Fonksiyon

def standardization(a,p):
    return a * 10/100 * p * p

'''def all_calculation(warm,moisture,charge,p):
    a=calculate(warm,moisture,charge)
    b=standardization(a,p)
    print(b*10)'''

def all_calculation (varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization (a, p)
    print(b * 10)
    
all_calculation (1, 3, 5, 19, 12)