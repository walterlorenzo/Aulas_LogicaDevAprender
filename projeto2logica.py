# Projeto - chute o número
''''
Escreva um programa que, ao iniciar gera um valor aleatório 1 a 19 e permite que o usuário
chute um número de até que o valor gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início
do programa.

# Método 5Q's para montar um algoritmo:

Analise criticamente o projeto e descubra:
(Tente explicar esse problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- Valor aleatório de 1 a 10
- chute do usuário
2. O que devo fazer com esses dados?
- Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no início do programa e
dizer se o chute foi maior, menor ou igual ao valor que foi gerado no início do programa
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
- O resultado esperado é de que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início
do programa.
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if valor_aleatorio > chute:
    print "Chute foi maior que o valor gerado"
if chute < valor_aleatorio
    print "Chute foi menor que o valor gerado"
if chute = valor_aleatorio
    print "Você acertou"

'''

import ramdom
valor_aleatorio = random.randint(
