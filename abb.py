
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
        
    # método para fazer o percurso em ordem
    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado
    
    # método auxiliar recursivo para fazer o percurso em ordem
    def _em_ordem(self, no, resultado):
        if no is None:
            return
        
        self._em_ordem(no.esq, resultado)
        resultado.append(no.dado)
        self._em_ordem(no.dir, resultado)
    
    # método para remover um elemento da árvore
    def remover(self, dado):
        self.raiz = self._remover(self.raiz, dado) 
        
    # método auxiliar (recursivo) para remover um elemento 
    def _remover(self, no, dado):
        if no is None:
            return None
        
        if dado < no.dado:
            no.esq = self._remover(no.esq, dado)
        elif dado > no.dado:
            no.dir = self._remover(no.dir, dado)
        else:
            # caso 1 -> o nó não tem filhos (é uma folha)
            if no.esq is None and no.dir is None:
                return None
            
            # caso 2 -> o nó só tem um filho
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            
            # caso 3 -> o nó tem dois filhos
            sucessor = self.buscar_menor(no.dir)
            no.dado = sucessor.dado
            no.dir = self._remover(no.dir, sucessor.dado)
            
        return no

    def buscar_menor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual
        
################################################################
if __name__ == '__main__':
    print('*' * 85)
    arvore = ABB()
    
    arvore.inserir(15)
    arvore.inserir(7)
    arvore.inserir(10)
    arvore.inserir(25)
    arvore.inserir(20)
    arvore.inserir(35)
    
    print(arvore.em_ordem())
    
    arvore.remover(20)    
    print(arvore.em_ordem())
    
    arvore.remover(7)
    print(arvore.em_ordem())
    
    arvore.remover(15)
    print(arvore.em_ordem())