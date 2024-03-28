#Defina as funções inserção, remoção e busca como métodos da Classe Lista. (Vide apostila)

class Lista:
    
   
    
    def __init__(self, elementosLista):                #Construtor da lista
        self.elementosLista = elementosLista
        
    def inserir(self, elementosLista):
        self.elementosLista.append(elementosLista)     #Adicionar um elemento na lista
        
    def remover(self, elementosLista):
        if elementosLista in  self.elementosLista:
            self.elementosLista.remove(elementosLista)  #Remove um elemento na lista
        else:
            print("Não encontrei um elemento em sua lista")
            
    def buscar(self,elementosLista):
        if elementosLista in self.elementosLista:
            print("Achei o seu elemento na lista")
        else:
            print("Não achei o seu elemento na lista")
            
            
elementosLista = Lista([0,1,2,3,4,5])

elementosLista.inserir(6)
elementosLista.inserir(7)

elementosLista.remover(2)

elementosLista.buscar(8)

print(elementosLista.elementosLista)