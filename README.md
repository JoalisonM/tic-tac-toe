# **Jogo da velha :hash:** 

## Dependências :computer:
* Sockets com TCP;
* Linguagem python.

## Regras :page_with_curl:
* Apenas dois players podem se conectar ao server;
* Quem conectar primeiro é o player 1 e o segundo o player 2;
* Se toda matriz estiver preenchida é empate;
* Se uma linha do tabuleiro estiver preenchida com X ou O, haverá um ganhador;
* Se uma coluna da tabuleiro estiver preenchida com X ou O, haverá um ganhador;
* Se uma das diagonais do tabuleiro estiver preenchida com X ou O, haverá um ganhador.

## Conexões :electric_plug:

#### START_GAME (player -> server) :pushpin:
* O player manda um pacote com o nome dele para reconhecimento;
     

#### RECOGNIZE_PLAYER (server -> player) :pushpin:
* O server manda um pacote que diz ao jogador qual player ele é (1 ou 2);

#### MAKE_PLAY (player -> server) :pushpin:
* O player manda um pacote com as informações da jogada dele;

#### REDIRECT (server -> player) :pushpin:
* O server manda um pacote um jogador com as informações da jogada de outro
	jogador;

#### RESULT (server -> player) :pushpin:
* O server manda um pacote com qual foi o jogador que ganhou a partida;

## Jogar :arrow_forward:
* Primeiro é necessário executar o arquivo `python3 main.py` no terminal para ligar o servidor;
* Os jogadores se conectam no servidor ao executar o arquivo `python3 client.py` no terminal;
* Apos se conectar, o jogador se identifica através do nome;
* Fica aguardando até o outro jogador entrar;
* O player 1 sempre vai ser o `X` e o player 2 sempre vai ser o `O`;
* Player 1 começa jogando e o player 2 espera a jogada do 1;
* Ambos os jogadores fazem suas jogadas, indicando a posição no tabuleiro;
* Quando houver um vencedor ou der empate, o jogo acaba.




