#3. Crie uma função que percorre e imprime todos os elementos da fila.


from queue import Queue    #Importei o queue para manipular as filas

fila = Queue()
fila.put(print(1," - Primeiro da fila"))           #.put é usado pra inserir elemento na fila, quando falamos de queue.
fila.put(print(2," - Segundo da fila")) 
fila.put(print(3," - Terceiro da fila")) 
fila.put(print(4," - Quarto da fila")) 
fila.put(print(5," - Quinto da fila")) 
fila.put(print(6," - Sexto da fila")) 
fila.put(print(7," - Septimo da fila")) 





def percorrer_fila(fila):
    while not fila.empty():          
        elemento = fila.get()
        print(elemento)
       
percorrer_fila(fila,)