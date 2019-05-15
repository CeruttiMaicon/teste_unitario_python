
import unittest

print("Atividade algoritmo - Materia - TESTE")
print("Digite um numero para descobrir seus divisores")

#recebe o input na variavel e o converte para numero inteiro

# Comentado para execucao dos teste, mas aqui recebe os testes
# numero = int(input("Digite um numero: "))



def divisores(numero):
  array = []
  #faz as interacoes com o input digitado
  for i in range(numero):
    #verifica se o contador do numero eh diferente de 0
    # se for 0 ele ignora o resultado
    if i != 0:
      #verifica se o resto de divissao eh igual a zero
      #que identifica os numeros que sao divisiveis
      if numero % i == 0:
        #imprime os resultados dos numeros divisiveis 
        #pelo numero  digitado
        array.append(i) 
  print(array)
  return array

#chama a funcao para o usuario executar um input
#divisores(numero)


#classe de teste que chama e funcao e a executa
#a segunda entrada (o array), é o resultado esperado pela funcao de teste
class MyTest(unittest.TestCase):
  def test(self):
    self.assertEqual(divisores(90), [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45])

if __name__ == '__main__':
  unittest.main()


## Este teste funciona

# if(numero == 0):
#   msg = 'O número zero é improprio para a função de divisores'
#   assert False, msg

# if(numero < 0):
#   msg = 'Não pode ser passado como parametro um número negativo para encontrar seus divisores'
#   assert False, msg