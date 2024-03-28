#Remova duplicatas de uma lista ordenada. Suponha que lhe seja fornecida uma lista encadeada armazenando números inteiros em ordem crescente. Sua tarefa é remover todos os elementos duplicados da lista. Por exemplo, dada a lista [0 → 1 → 1 → 5 → 7 → 10 → 10 → None], seu programa deve retornar a lista [0 → 1 → 5 → 7 → 10 → None].

exemploLista = [0,1,1,5,7,10,10]
remocaoDasDuplicadas = list(set(exemploLista))  #Set: Elementos únicos, removendo todos os duplicados.
                                                # list: Não bagunça a ordem da lista.
print(remocaoDasDuplicadas)