A heurística escolhida pra a resolução do Problema do Caixeiro Viajante foi a
"nearest neighbor", NN. Nesse algortítmo, é selecionado uma localidade como ponto de partida
e, a cada iteração, a "próxima localidade" a ser visitada é selecionada a partir da distância
entre a posição "atual" e a posição da próxima localidade. A localidade selecionada é
aquela que possui a menor distância em relação a localidade original E ainda não foi visitada.
Após visitar todas as localidades, a distância (custo) da última localidade até a primeira é
somada ao resultado, representando o regresso ao ponto de partida.