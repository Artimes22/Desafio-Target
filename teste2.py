print('-=' * 20)
print('Sequência de Fibonacci')
print('-='*20)
#Informar o valor para vereficar
numero_vereficar = int(input('Quantos termos você quer mostrar? '))
#Define os primeiros dois valores da sequência
t1 = 0
t2 = 1
fibonacci = [0,1]
#Cria a Sequência de fibonacci
print('~' *40)
print('{} -> {}' .format(t1, t2), end='')
cont = 3
while cont <= numero_vereficar:    
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(' -> {}' .format(t3), end='')
print(' -> FIM!')  

#Descobre se o valor informado pertence ou não a sequência de fibonacci
while fibonacci[-1] < numero_vereficar:
    novo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novo_termo)
    
if numero_vereficar in fibonacci:
    print(f"{numero_vereficar} pertence à sequência de Fibonacci!")
else:
    print(f"{numero_vereficar} não pertence à sequência de Fibonacci.")    



