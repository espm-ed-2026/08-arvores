class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
class ABB:
    def __init__(self):
        self.raiz = None
        
    # método para inserir um dado na árvore binária de busca
    def inserir(self, dado):
        dado = dado.lower()
        self.raiz = self._inserir(self.raiz, dado)
        
    # método recursivo para inserir um dado na árvore
    def _inserir(self, no, dado):
        if no is None:
            return No(dado)
        
        if dado < no.dado:
            no.esq = self._inserir(no.esq, dado)
        elif dado > no.dado:
            no.dir = self._inserir(no.dir, dado)
            
        return no
    
    # método para buscar os nomes que começam com um determinado prefixo
    def buscar(self, prefixo):
        prefixo = prefixo.lower()
        resultado = []
        self._buscar(self.raiz, prefixo, resultado)
        return resultado
        
    # método recursivo para busca 
    def _buscar(self, no, prefixo, resultado):    
        if no is None:
            return
        
        if prefixo < no.dado:
            self._buscar(no.esq, prefixo, resultado)
            
        if no.dado.startswith(prefixo):
            resultado.append(no.dado)
            
        if (prefixo + chr(256)) > no.dado:
            self._buscar(no.dir, prefixo, resultado)
    
            
#------------------------------------------------------------------------------
# programa principal
if __name__ == '__main__':
    abb = ABB()
    usuarios = ["mariana", "marcos", "mario", "ana", "marina", "bruna", "marcelo"]
    
    for u in usuarios:
        abb.inserir(u)
        
    print(abb.buscar('mar'))