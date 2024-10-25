#A) Calcule e informe o IMC da pessoa

def calc_imc(peso,altura):
    imc = peso/(altura * altura)
    print(imc)
    return imc

#B) Informe a classificação segundo a OMS dessa pessoa
def class_imc(imc):
    if imc < 17:
        print('Muito abaixo do peso')
    elif imc < 18.5:
        print('Abaixo do peso')
    elif imc < 25:
        print('Peso normal')
    elif imc < 30:
        print('Sobre peso')
    elif imc < 35:
        print('Obsidade Grau I')
    elif imc < 40:
        print('Obsidade Grau II')
    else:
        print('Obesidade Grau III')


# Eu acertei a questão porém eu perdi 0.1 pelo fato de eu ter colocado "÷" no lugar de "/" e "•" ao invés de "*".

# A execusão do código com a correção dos sinais, é correta, por isso eu acertei.
