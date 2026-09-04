
## Exercícios - Estrutura sequencial

1. Elabore um algoritmo que leia um nome e uma idade e apresente estes dados em uma mensagem.
2. Elabore um algoritmo que leia três números e calcule a média entre eles.
3. Elabore um algoritmo que leia um valor em moeda nacional (real) e apresente o valor convertido para moeda estrangeira, de acordo com uma taxa de conversão.
4. Elabore um algoritmo que leia dois números e calcule as operações de soma, subtração, multiplicação, divisão (apresentando o quociente completo, somente a parte inteira e o resto), potenciação (primeiro elevado ao segundo) e raiz do primeiro na base do segundo.
5. Elabore um algoritmo que leia o consumo em watts por hora de um aparelho elétrico, uma quantidade de horas diária, uma quantidade de dias e calcule quantos watts esse aparelho consumirá em um mês.
6. Elabore um algoritmo que receba uma temperatura em Celsius e apresente-a em Fahrenheit e Kelvin.
7. Elabore um algoritmo que leia um valor numérico inteiro e apresente seu antecessor e seu sucessor.
8. Elabore um algoritmo para ler dois valores, armazená-los em duas variáveis A e B, e trocar o valor entre elas.
9. Elabore um algoritmo que leia o preço de compra, o percentual de lucro e calcule o preço de venda de um produto.
10. Elabore um algoritmo que calcule a área de um círculo.
11. Elabore um algoritmo que calcule a área de um retângulo.
12. Elabore um algoritmo que calcule a área de um losango.
13. Elabore um algoritmo que calcule o volume de um paralelepípedo.
14. Elabore um algoritmo que calcule a hipotenusa de um triângulo com base nos catetos.
15. Elabore um algoritmo que receba a medida de dois ângulos de um triângulo e calcule o terceiro.
16. Elabore um algoritmo que leia um número e mostre sua tabuada do 1 ao 10.
17. Elabore um algoritmo que leia a velocidade de um projétil em metros por segundo e apresente esta velocidade em quilômetros por hora.
18. Elabore um algoritmo que leia a quantidade de horas normais e extras trabalhadas por um profissional, o valor/hora que ele ganha, o percentual total de desconto em impostos e calcule o salário líquido a receber. Considere que a hora extra remunera 50% a mais do que a hora normal.
19. Elabore um algoritmo que leia um montante em dinheiro, uma taxa de rendimento a ser aplicada, e apresente o rendimento em dinheiro e o montante de dinheiro final.
20. Elabore um algoritmo que leia o consumo de um automóvel (quilômetros por litro de combustível), uma distância a ser percorrida e apresente quanto de combustível é necessário para o trajeto.
21. Elabore um algoritmo que leia uma quantidade de minutos e apresente-a no formato `hh:mm` e também a converta em segundos.

## Exercícios - Estrutura condicional

1. Elabore um algoritmo que leia duas notas bimestrais e verifique se o aluno foi aprovado ou não. Para ser aprovado, a média deve ser igual ou maior que 7.
2. Elabore um algoritmo que leia uma temperatura (sem decimais) e apresente sua classificação conforme esta tabela:

   | Temperatura | Classificação |
   |---|---|
   | Menor que 10 | Frio |
   | Entre 10 e 25 | Normal |
   | Maior que 25 e menor que 35 | Quente |
   | 35 ou mais | Indaial |

3. Elabore um algoritmo que calcule o custo de oportunidade na seleção entre dois projetos de uma organização.
4. Elabore um algoritmo que leia duas notas bimestrais e verifique se o aluno foi aprovado ou não. Para ser aprovado, a média ponderada entre as notas (1º bimestre peso 4 + 2º bimestre peso 6) deve ser igual ou maior que 7.
5. Elabore um algoritmo que leia o saldo em conta bancária de uma pessoa, o valor de crédito do seu salário, um valor de retirada e informe o novo saldo em conta. Observação: a retirada não pode ultrapassar o saldo da conta.
6. Elabore um algoritmo que leia dois números e permita escolher entre uma das quatro operações aritméticas entre eles. Use `match`.
7. Elabore um algoritmo que leia três números e mostre o maior deles.
8. Um supermercado decidiu dar descontos a seus clientes conforme a quantidade comprada, seguindo esta tabela:

   | Total comprado | Desconto |
   |---|---:|
   | Até R$ 30,00 | Sem desconto |
   | Mais que R$ 30,00 e até R$ 100,00 | 5% |
   | Mais que R$ 100,00 e até R$ 250,00 | 10% |
   | Acima de R$ 250,00 | 15% |

   Elabore um algoritmo que leia o total comprado e apresente o percentual de desconto, o valor do desconto e o valor total da compra com o desconto aplicado.

9. Elabore um algoritmo que leia três notas de avaliações e informe se o aluno foi aprovado, calculando a média entre as duas notas mais altas entre as três avaliações (método utilizado pela Uniasselvi). A média para ser aprovado é 6.
10. Elabore um algoritmo que leia o comprimento de três segmentos de reta, informe se eles formam um triângulo e, em caso positivo, de qual tipo.
11. Elabore um algoritmo que leia dois números e calcule a diferença do maior pelo menor.
12. Elabore um algoritmo que leia um número e, independentemente de este ser positivo ou negativo, apresente-o sempre como positivo.
13. Elabore um algoritmo que leia três números e os apresente em ordem crescente.
14. Elabore um algoritmo que leia um número e informe se ele está dentro da faixa permitida (1 a 9) ou fora dela.
15. Elabore um algoritmo que leia o número de um mês (1 a 12) e escreva o mês por extenso, informando caso seja um número de mês inválido. Use `match`.
16. Elabore um algoritmo que leia a quantidade de medalhas de ouro (peso 3), prata (peso 2) e bronze (peso 1) de três países e informe a classificação deles.
17. Elabore um algoritmo que escreva por extenso uma data e hora lidas no formato `dd/mm/aa hh24:mm`. Use `match`.
18. Elabore um algoritmo que receba o valor do salário-mínimo, o número de horas trabalhadas, o número de dependentes do funcionário e a quantidade de horas extras trabalhadas, calcule e apresente o salário a receber do funcionário de acordo com as regras a seguir:

    - O valor da hora trabalhada é igual a 1/5 do salário-mínimo;
    - O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
    - Para cada dependente, acrescentar R$ 32,00;
    - Para cada hora extra trabalhada, calcular o valor da hora trabalhada acrescida de 50%;
    - O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras;
    - Calcular o valor do imposto de renda retido na fonte de acordo com a tabela a seguir, usando `match`:

      | IRRF | Salário bruto |
      |---:|---|
      | Isento | Inferior a R$ 200 |
      | 10% | Entre R$ 200 e R$ 500 |
      | 20% | Acima de R$ 500 |

    - O salário líquido é igual ao salário bruto menos o IRRF.

## Exercícios - Estrutura de repetição

1. Elabore um algoritmo que leia 8 preços de produtos, some-os e apresente o preço total.
2. Elabore um algoritmo que calcule o fatorial de um número inteiro positivo menor ou igual a 10.
3. Elabore um algoritmo que leia uma quantidade de minutos e uma quantidade de segundos e faça a contagem regressiva até 0 minutos e 0 segundos.
4. Elabore um algoritmo que leia dois números e calcule o quociente e o resto da divisão do primeiro pelo segundo, sem usar a operação de divisão nem a de divisão inteira.
5. Elabore um algoritmo que calcule os N primeiros elementos da sequência de Fibonacci.
6. Elabore um algoritmo que leia votos até que seja digitado “S” e apresente o resultado da eleição, mostrando qual candidato ganhou e quantos votos nulos ocorreram. Os candidatos são: 1 - Fulano, 2 - Ciclano e 3 - Beltrano.
7. Elabore um algoritmo que imprima todas as possibilidades de que, no lançamento de dois dados, tenhamos o valor 7 como resultado da soma dos lados.
8. Elabore um algoritmo que leia números e informe quais são primos até ser informado 0.
9. Elabore um algoritmo que calcule quantos anos serão necessários para Felisberto ser mais alto que Anacleto, sendo que Anacleto tem 1,50 m e cresce 2 cm por ano, enquanto Felisberto tem 1,10 m e cresce 3 cm por ano.
10. Elabore um algoritmo que apresente a soma dos quadrados dos números inteiros existentes entre 15 e 20.
11. Elabore um algoritmo que apresente os números inteiros entre 2 e 30, contando de 3 em 3.
12. Elabore um algoritmo que apresente, de 9 em 9, os valores entre 0 e 50 °C, convertidos para Fahrenheit.
13. Elabore um algoritmo que leia a opção de 10 clientes: se o cliente compra à vista, com 30 ou 60 dias de prazo, e ao final apresente quantos clientes compram em cada condição.
14. Elabore um algoritmo que leia 10 salários de funcionários de uma empresa e, ao final, apresente o maior e o menor salário, a média salarial da empresa e o valor total dos salários informados.
15. Elabore um algoritmo que leia 2 números e multiplique o primeiro pelo segundo. Como a multiplicação é o resultado de várias adições, apresente passo a passo o cálculo efetuado.
16. Elabore um algoritmo que leia 2 números e calcule o primeiro elevado à potência do segundo. Como a potência é o resultado de várias multiplicações, apresente passo a passo o cálculo efetuado.
17. Elabore um algoritmo que leia um número inteiro e gere sua tabuada, apresentando-a passo a passo.
18. Elabore um algoritmo que gere todas as tabuadas do 2 ao 9, apresentando-as passo a passo.
19. Elabore um algoritmo que simule o sistema SAC para aquisição de imóveis.
20. Elabore um algoritmo que calcule juro composto de um investimento.
21. Elabore um algoritmo que leia e converta números das bases numéricas binária, octal e hexadecimal para decimal.
22. Elabore um algoritmo que leia e converta números da base decimal para as bases binária, octal e hexadecimal.

## Exercícios - Sub-rotina

1. Elabore um algoritmo que simule uma calculadora, permitindo efetuar as quatro operações básicas - adição, subtração, multiplicação e divisão -, calcular o resto da divisão e calcular a potência. Para a multiplicação, efetue sucessivas somas. Para a divisão e o resto da divisão, efetue sucessivas subtrações. Para a potência, efetue sucessivas multiplicações (que efetuarão sucessivas somas). Dica: aproveite as rotinas implementadas em listas de exercícios anteriores.
2. Elabore um algoritmo que verifique se um CPF digitado é válido. Para os cálculos, utilize as sub-rotinas criadas no exercício 1.
3. Elabore um algoritmo que simule um caixa eletrônico para 3 contas diferentes, permitindo efetuar as operações de saque, depósito, transferência, apresentação de saldo e apresentação de extrato detalhado. O saldo inicial das contas é zero, e nenhuma pode ficar com saldo negativo.
4. Elabore um algoritmo para simular uma urna eletrônica que permita cadastrar de 2 a 3 candidatos por eleição, iniciar votação, votar, finalizar votação e apresentar o resultado da eleição, sendo que o eleitor pode votar em branco.
5. Elabore um algoritmo que leia e converta números entre as bases numéricas decimal, binária, octal e hexadecimal.
6. Elabore um algoritmo que receba o valor do salário-mínimo, o número de horas trabalhadas, o número de dependentes do funcionário e a quantidade de horas extras trabalhadas, calcule e apresente o salário a receber do funcionário de acordo com as regras a seguir:

    - O valor da hora trabalhada é igual a 1/5 do salário-mínimo;
    - O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
    - Para cada dependente, acrescentar R$ 32,00;
    - Para cada hora extra trabalhada, calcular o valor da hora trabalhada acrescida de 50%;
    - O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras;
    - Calcular o valor do imposto de renda retido na fonte de acordo com a tabela a seguir, usando `match`:

      | IRRF | Salário bruto |
      |---:|---|
      | Isento | Inferior a R$ 200 |
      | 10% | Entre R$ 200 e R$ 500 |
      | 20% | Acima de R$ 500 |

    - O salário líquido é igual ao salário bruto menos o IRRF.

7. Elabore um algoritmo que calcule juro composto de um investimento, com ou sem aporte periódico.
8. Elabore um algoritmo que simule o sistema SAC para aquisição de imóveis.
9. Elabore um algoritmo que simule o jogo da velha, armazenando o histórico com todas as jogadas efetuadas (reaproveite a rotina de armazenamento do histórico implementada no exercício 3).
10. Elabore um algoritmo que simule o jogo batalha naval em um mapa 5 x 5, onde seja possível posicionar 5 embarcações de tamanho 1 x 1 cada.
11. Elabore um algoritmo para controle de estoque de 1 produto, que permita informar o saldo inicial, fazer entradas, saídas, consultar o saldo atual e gerar um relatório do histórico, começando pelo saldo inicial, apresentando todas as entradas e saídas e, ao final, mostre o saldo atual (reaproveite a rotina de histórico do exercício 3).
12. Elabore um algoritmo para controlar o funcionamento de um carro automático:

    - Para ligar o carro, o pedal do freio precisa estar pressionado e o câmbio precisa estar na posição P. O carro liga com velocidade igual a zero;
    - Para colocar o câmbio na posição D ou R, o pedal do freio precisa estar pressionado e o carro precisa estar ligado e parado (velocidade igual a zero);
    - Para acelerar, o pedal do freio precisa estar pressionado, o carro precisa estar funcionando e o câmbio precisa ser colocado na posição D ou R. Ao acelerar, a velocidade sai de zero;
    - Para parar o carro, o pedal do freio precisa estar pressionado. Ao parar, a velocidade vai para zero;
    - Para colocar o câmbio na posição P, o carro precisa estar parado.

## Exercícios - Registro

1. Elabore um algoritmo que simule um caixa eletrônico, permitindo abrir conta (com saldo ou não), efetuar saque, depósito, transferência, apresentar saldo, apresentar extrato detalhado e encerrar conta (somente com saldo zero).
2. Elabore um algoritmo para simular uma urna eletrônica, permitindo cadastrar de 2 a 5 candidatos, iniciar votação, votar, finalizar votação e apresentar o resultado da eleição, sendo que o eleitor pode votar em branco.
3. Elabore um algoritmo que receba o valor do salário-mínimo, o número de horas trabalhadas, o número de dependentes e a quantidade de horas extras trabalhadas de 5 funcionários de uma empresa e, com base nesses dados, calcule, armazene e apresente o salário a receber de cada um, de acordo com as regras a seguir:

    - O valor da hora trabalhada é igual a 1/5 do salário-mínimo;
    - O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
    - Para cada dependente, acrescentar R$ 32,00;
    - Para cada hora extra trabalhada, calcular o valor da hora trabalhada acrescida de 50%;
    - O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras;
    - Calcular o valor do imposto de renda retido na fonte de acordo com a tabela a seguir, usando `match`:

      | IRRF | Salário bruto |
      |---:|---|
      | Isento | Inferior a R$ 200 |
      | 10% | Entre R$ 200 e R$ 500 |
      | 20% | Acima de R$ 500 |

    - O salário líquido é igual ao salário bruto menos o IRRF.

4. Elabore um algoritmo que calcule juro composto de um investimento, com ou sem aporte periódico, armazenando e apresentando os valores mensais de saldo inicial, rendimento e saldo final.
5. Elabore um algoritmo que simule o sistema SAC para aquisição de imóveis, apresentando uma tabela detalhada com todos os valores mensais.
6. Elabore um algoritmo para controle de estoque de produtos que permita informar o saldo inicial, fazer entradas, saídas, consultar o saldo atual e gerar um relatório do histórico, começando pelo saldo inicial, apresentando todas as entradas e saídas e, ao final, mostre o saldo atual.
7. Aprimore o controle de estoque de produtos implementado no exercício anterior, permitindo indicar o local em que cada produto está armazenado. Além disso, deve ser possível emitir um relatório de saldo de estoque dos produtos com base no local de armazenamento.
8. Elabore um algoritmo que simule uma agenda de telefones para até 10 contatos, com as seguintes opções:

    - **Cadastrar:** armazenar um nome e um telefone;
    - **Alterar:** buscar um nome e atualizar seu telefone;
    - **Consultar:** buscar um nome e exibir seu telefone;
    - **Excluir:** buscar um nome ou um telefone e apagar seu registro;
    - **Listar:** exibir todos os nomes e telefones registrados.

    Observação: mostrar uma mensagem caso o registro buscado não seja encontrado.

9. Elabore um algoritmo para controle de vendas que apresente o seguinte menu ao usuário:

    - **Cadastrar cliente:** armazenar o nome de um cliente;
    - **Alterar cliente:** localizar e alterar o nome de um cliente;
    - **Excluir cliente:** localizar e excluir um cliente pelo nome;
    - **Cadastrar produto:** armazenar o nome e o valor unitário de um produto;
    - **Alterar produto:** localizar e alterar o nome e o valor unitário de um produto;
    - **Excluir produto:** localizar e excluir um produto pelo nome;
    - **Realizar venda:** selecionar um cliente, um produto, informar a quantidade do produto e registrar a venda, atribuindo um código sequencial a ela;
    - **Cancelar venda:** excluir o registro de venda, buscando-a por meio de seu código sequencial;
    - **Emitir relatório de vendas:** apresentar todas as vendas efetuadas;
    - **Emitir relatório de vendas por cliente:** apresentar quanto um cliente já gastou;
    - **Emitir relatório de vendas por produto:** apresentar o estoque atual de um produto.

    Observação: mostrar uma mensagem caso o registro buscado não seja encontrado.

10. Junte os algoritmos dos exercícios 7 e 9, armazenando o estoque dos produtos e impedindo que seja vendida uma quantidade maior que a disponível.
11. Elabore um algoritmo para gerenciar ingressos em uma sala de cinema, que permita:

    - Apresentar a sala de cinema com todas as cadeiras disponíveis e ocupadas (10 fileiras com 20 cadeiras cada);
    - Adquirir um ingresso, armazenando o nome do cliente e da cadeira selecionada.
