# num1 = 5
# num2 = 7.9
# print(num1 + num2)
# print(type(num1))
# print(type(num2))
# num3 = float(round(3.3224, 2))
# print('O numero com duas casas decimais é',num3,'.')
# print('O numero com duas casas decimais é'+str(num3)+'.')
# print('O número com 2 casas decimais é {:.2f}.'.format(num3))
# num4 = float(round(5.3224, 3))
# print(f"o numero com 3 casas decimais é {num4:.2f}")
# x = True
# z = False
# print(type(z))
# a = 5 + 5
# print('a',a,)
# b = 7 - 2
# print('b',b,)
# c = 2 * 2
# print('c',c,)
# d = 4 / 2
# print('d',d,)
# e = 10 % 3
# print('e',e,)
# f = 4**2
# print('f',f,)
# g = 10//3
# print('g',g,)
# nota = 6
# media = 7
# aprovado = nota >= media
# print(aprovado)
# print(type(not))
media_final = float(input("Média final da discplina de 0 a 10 = "))
frequencia = int(input("Frequência da disciplina em porcentagem = "))
if media_final >= 6 and frequencia >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")
