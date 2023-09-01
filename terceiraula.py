import random

"""print ("random.randrange(100): ",  random.randrange (100))
print ("random.randrange(50,100): ",random.randrange (50,100))
print ("random.randrange( [20,5,10,15,54] ): ", random.randrange ([20, 5, 10, 15, 54] ))
print ("random.randrange( ):", random.randrange ( ))
print ("random.randrange(30,60):", random.randrange (30,60))"""



escola = "Taboao da Serra"
print (len (escola))

"""print (escola.count("a"))

print (escola.find("a"))


print (escola.upper())


print (escola.lower())


print (escola.capitalize())


print (escola.title())"""



"""print ("$".join("Taboao da Serra"))
print (escola.split(" "))
print (escola.replace('Serra', 'trevas'))"""


 
"""a= input("informe um numero para a variavel  a:")
b = input("informe um numero para a variavel b:")

if a > b:
    x = a
    a = b 
    b = x
 
print ("o valro da variavel a agora é: ", a)
print ("o valro da variavel b agora é: ", b)"""




"""a = input ("informe um numero para a variavel a:")
b = input ("informe um numero para a variavel b:")

x = int (a) + int (b)

if x > 10:
    print("resultado da soma:", x," é maior que 10")
else:
    print("resultado da soma:", x, " nao sendo maior que 10 ")"""








"""nht = float(input("iforme o numero de horas trabalhadas"))
vph = float(input("informe o valor pago por hora"))
pd = float(input("informe a porcentagem do desconto"))

sb = vph*nht
desc = sb*(pd/100)
sl = sb - desc

print("valor do salario bruto é", sb)
print("valor do salario liquido é", sl)"""







nht = float(input("informe o valor de horas trabalhadas"))
vph = float(input("informe o valor pago por hora"))


sb = nht * vph 
if sb < 1000:
    desc = sb*0.05
elif sb > 2000:
    desc = sb*0.15
else: 
    desc = sb*0.1

sl = sb-desc

print (sb,desc,sl)  




