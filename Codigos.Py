#Calculo de média de notas
nota1 = nota2 = 0.0
media = 0.0
pim = 0.0
exame = 0.0
media = 0.0
media_final = 0.0

"entrada de dados é do tipo string e devemos tranforma la para tipo float"

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
pim = float(input("Digite a nota do pim: "))

print()
"Calcular a média  das notas"
media = (nota1 * 4 + nota2 * 4 + pim * 2)/10

if media >= 7:
    print("aprovado", "\n")

    print("Sua média foi", media, "\n")

else:
    print("voce precisa fazer o exame")

    print("Sua média foi", media, "\n")

if media <= 6:
 
 print()
 exame = float(input("adicione a nota do exame: "))
 media = float(input("adicione a media: ")) 

 print()
 media_final = (media + exame)/2

 print("Sua Media Final foi", media_final, "\n")
else:
   print("E isso ai")   

if media_final >= 5:
   print("APROVADO")

elif media == 0.0:
   print("REPROVADO")

elif media_final == 0.0:
   print("PARABENS")

else:
   print("REPROVADO")   

'------------------------------------------------------------------'
#saida de dados
nome = "Luizz"
idade = 19
altura = 1.75


print("1 - Usando Concatenacao")
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos e altura " + str(round(altura, 3)) , "\n")

print("2 - Usando método .format()")
print("Meu nome é {} e tenho {} anos e altura {:.3f}.".format(nome, idade, altura), "\n")

print("3 - Interpolação (f-strings)")
print(f"Meu nome é {nome} e tenho {idade} anos e altura {altura:.3f}.", "\n")

print("4 - Interpolação (f-strings) atribuindo a uma variável")

frase = f"Meu nome é {nome} e tenho {idade} anos e altura {altura:.3f}"

print(frase, "\n")
