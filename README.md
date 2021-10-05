# <h1>Avaliacao-Tecnica
  >Status: Developed
  
Como utilizar os códigos
  
  

1-Escolha um diretório no qual deseja baixar os códigos, abra um CMD e digite: git clone https://github.com/VictorFujiyama/Avaliacao-Tecnica
  
2-Instale as bibliotecas necessárias para o funcionamento do programa da seguinte forma. Abra o CMD como adiministrador e em seguida digite o seguinte comando "python -m pip install requests"
  
3-Para rodar os códigos basta entrar na pasta "main program" onde estão localizados os arquivos py, portanto em algum editor python execute o arquivo desejado.

  Sobre a primeira questão( Arquivo Fibonacci.py)
  
  
  
  
Este arquivo .py tem como função principal a construção da sequência de Fibonacci:
  
  
  
  É uma sequência de números inteiros, começando por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.
  
  Neste programa o usuário insere um número N de entrada e o programa responde com o N-ésimo termo da sequência de fibonacci
  
  O termo em questão é calculado a partir da base onde temos que o primeiro e o segundo termo da sequência, sendo eles respectivamente zero e um. A partir deles é         efetuada um calculo basico mostrado no código onde obtemos o resultado do termo desejado.
  
  
  
  
  Sobre a segunda questão: Explique o problema que poderia acontecer com o programa desenvolvido na questão 1 ao passar como
entrada n = 50.
  
  
  Devido ao comportamento das funções recursivas, principalmente em linguagem python onde todas as funções são jogadas na memória do call stack. Elas podem acabar consumindo muita memória, ou seja, o programa não suportaria fazer operações onde necessitam de muitas recursões pois o python permite somente mil delas, isto é o que acontece no caso de pedir o quinquagésimo termo da sequência de fibonnaci, por exemplo.
  O que resolveria esse problema seria a programação em loops, que em python acabam sendo bem mais performáticas do que as funções recursivas(Demonstrado no arquivo fiboSolved.py).
  
    
