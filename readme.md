# Algoritmo python que verifica os divisores de um número

Inicialmente o algoritmo verifica e mostra em tela todos os divisores de um número dado como input pelo usuario.

Este número passa para a função com o nome de 'divisores', que recebe como parametro o valor digitado.

Em seguida, a classe MyTest, que executa o teste unitario, que executa a função acima, e em seguida pede um array(que é o retorno esperado pela função), e se a função for igual ao resultado esperado. 

Aqui o exemplo do algoritmo, com o teste com o input 90.


```
Atividade algoritmo - Materia - TESTE
Digite um numero para descobrir seus divisores

Digite um numero: 90

[1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45]

[1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45]


----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

Ele dá OK se o retorno da função estiver exatamente igual ao esperado na função.

Agora eu irrei fazer uma demonstração de saida se o algoritmo esperar um retonro como (sem o número 45).

```
[1, 2, 3, 5, 6, 9, 10, 15, 18, 30]
```

Com a mesma entrada do input 90.

```
FAIL: test (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dev3/Documentos/teste_unitario/AtividadeAlgoritmoTESTE.py", line 37, in test
    self.assertEqual(divisores(90), [1, 2, 3, 5, 6, 9, 10, 15, 18, 30])
AssertionError: Lists differ: [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45] != [1, 2, 3, 5, 6, 9, 10, 15, 18, 30]

First list contains 1 additional elements.
First extra element 10:
45

- [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45]
?                                  ----

+ [1, 2, 3, 5, 6, 9, 10, 15, 18, 30]

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)

```

Repare que ele mostra o erro, mostra a classe que o erro aconteceu e ainda compara o parametro esperado com o parametro retirado da função e lhe mostra visualmente o que esta diferente.

Agora para apenas executar os testes e verificar os retornos dados pela expressão irei comentar a linha 11 e 30, com os input do usuário.

Fique a vontade para descomentar o código e usufrir dele.

