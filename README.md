MÁQUINA NORMA
=============

Este projeto simula uma Máquina Norma com 8 registradores (de A até H), capaz de executar instruções simples a partir de um arquivo texto. 
É ideal para fins didáticos, como ensino de modelos computacionais e lógica de programação.

----------------------------------------
ESTRUTURA ESPERADA
----------------------------------------

- maquina_norma.py → Código principal da máquina
- programa.txt → Arquivo contendo as instruções do programa

----------------------------------------
COMO USAR
----------------------------------------

1. Execute o script no terminal com:

   python maquina_norma.py

2. Use o menu para interagir:

   [0] - Carregar Programa
   [1] - Inicializar e manipular registradores direto
   [2] - Executar Programa
   [9] - Sair

----------------------------------------
[0] CARREGAR PROGRAMA
----------------------------------------

O programa deve estar no arquivo "programa.txt", com cada linha no formato:

   <número da linha>:<INSTRUÇÃO>

Exemplos válidos:

   1:ADDA2       → Soma 1 ao registrador A e vai para a linha 2
   2:SUBB3       → Subtrai 1 de B (se B > 0) e vai para a linha 3
   3:ZERC4 5     → Se C == 0 vai para linha 4, senão vai para linha 5

Instruções válidas:
- ADD <registrador><destino>
- SUB <registrador><destino>
- ZER <registrador><destino_se_zero> <destino_se_nao_zero>

----------------------------------------
[1] INICIALIZAR REGISTRADORES
----------------------------------------

Você será solicitado a inserir um valor inteiro NÃO-NEGATIVO para cada registrador de A a H.

Esses valores são usados na execução do programa.

----------------------------------------
[2] EXECUTAR PROGRAMA
----------------------------------------

Depois de carregar o programa e inicializar os registradores, use esta opção para iniciar a execução.

Durante a execução:
- Cada passo será impresso no terminal
- Mostra o estado atual dos registradores
- Mostra qual instrução foi executada
- A execução termina quando não há mais linha válida para seguir

----------------------------------------
EXEMPLO DE ARQUIVO "programa.txt"
----------------------------------------

1:ZERA3 2
2:ADDA1
3:ZERB5 4
4:SUBB3
5:ADDC5

----------------------------------------
REQUISITOS
----------------------------------------

- Python 3.x
- Terminal/console

----------------------------------------
AUTOR
----------------------------------------

Este projeto foi desenvolvido como parte de estudos sobre Máquinas de Norma e modelos formais de computação.
Sinta-se à vontade para usar, modificar e compartilhar com seus colegas.
