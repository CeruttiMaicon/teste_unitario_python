
#unittest importacao de um framework para teste unitario em python
import unittest

print("Atividade algoritmo - Materia - TESTE")
print("Digite um numero para descobrir seus divisores")

#recebe o input na variavel e o converte para numero inteiro

# Comentado para execucao dos teste, mas aqui recebe os testes
# nota1 = int(input("Digite a nota 1: "))
# nota2 = int(input("Digite a nota 2: "))
# nota3 = int(input("Digite a nota 3: "))
# nota4 = int(input("Digite a nota 4: "))

def media_notas(nota1, nota2, nota3, nota4):
  if(nota1 < 0 or nota1 > 10 ):
    return False  
  if(nota2 < 0 or nota2 > 10):
    return False  
  if(nota3 < 0 or nota3 > 10):
    return False  
  if(nota4 < 0 or nota4 > 10):
    return False  
  #faz as interacoes com o input digitado
  media = (nota1 + nota2 + nota3 + nota4) / 4

  if(media == 5 or media == 6):
    print('EM FINAL')
    print(media)
    return(0)
  else:
    if(media >= 7):
      print('APROVADO')
      print(media)
      return 1
    else:
      print('REPROVADO')
      print(media)
      return -1

#chama a funcao para o usuario executar um input
# media_notas(nota1, nota2, nota3, nota4)


#classe de teste que chama e funcao e a executa
#a segunda entrada (o array), é o resultado esperado pela funcao de teste
class MyTest(unittest.TestCase):
  def test(self):
    self.assertEqual(media_notas(7, 2, 10, 9), 0)
    self.assertEqual(media_notas(7, 2, 2, 2), -1)
    self.assertEqual(media_notas(5, 5, 5, 5), 0)

if __name__ == '__main__':
  unittest.main()
