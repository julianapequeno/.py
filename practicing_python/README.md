# Praticando o Python! :)

Este repositório contém alguns projetos de prática em python.  Segue 
um pequeno resumo sobre cada um deles:

**numeros_divisíveis.py** é um programa que imprime os números entre 1 e 100 que dividem 
o número que foi recebido. Para poder ampliar o leque de divisores, é só aumentar o valor da variável N. 
Acabo de incrementar ao programa uma pequena alteração que permite avisar ao usuário se o número
é primo. Se o número for divisível por 2 números tais que sejam 1 e ele mesmo, o número é primo.
Lembrando que como o N vai até 100 (neste código), não aparecerá que o número 233, por exemplo, é primo. Pois 
só está contabilizando os divisores de 1 a 100.


**numeros_escritos.py** é um programa que recebe um número entre 0 e 999, e devolve o mesmo número escrito por extenso.

**figura_qualquer.py** é um programa desenvolvido a partir de uma questão desenvolvida em C da disciplina de ITP - Introdução às Técnicas de Programação do curso de BTI/UFRN. 
Tem por objetivo identificar se o clique do mouse foi feito dentro da figura 'qualquer', ou seja convexa etc.
A entrada teste é a seguinte:

3 2\
0 0\
0 10\
10 0\
A 3 3\
B 8 8

O 3 e 2 representam respectivamente N, a quantidade de pontos, e M, a quantidade de cliques. Após
a inserção dessas duas quantidades, o usuário entra com o x e o y dos pontos (N vezes), e depois o identificador (ex: A) mais o x e o y dos cliques (M vezes).

A saída resultante será a do identificador do clique que foi dado dentro da figura.

