#Código A
listaA =[x for x in range(5)]
print(listaA)

#Código B
listaB = list(range(5))
print(listaB)

#Código C
listaC = []
i = 0
while i < 5:
    listaC.append(i)
    i += 1
print(listaC)

'''
Saída Obtida: [0, 1, 2, 3, 4]

Resposta correta: Todos os códigos A, B e C

Resposta que marquei: Apenas código A e C

Análise: Afirmo que apenas os códigos A e C têm uma abordagem semelhante em como constroem a lista, nisso eu pensei que não era todos executavam o mesmo resultado.
'''
