class No:
    def __init__(self, timestamp, preco):
        self.timestamp = timestamp  
        self.preco     = preco      
        self.esq       = None
        self.dir       = None


class ABB:
    def __init__(self):
        self._raiz = None

    # método para inserir adpatado para esse exercício
    def inserir(self, timestamp, preco):        
        self._raiz = self._inserir(self._raiz, timestamp, preco)

    def _inserir(self, no, timestamp, preco):
        if no is None:
            return No(timestamp, preco)
        
        if timestamp < no.timestamp:
            no.esq = self._inserir(no.esq, timestamp, preco)
        elif timestamp > no.timestamp:
            no.dir = self._inserir(no.dir, timestamp, preco)
        else:
            no.preco = preco   # valor já existe, portanto apenas atualiza o nó
        return no

    # método para buscar um timestamp na árvore binária de busca
    def buscar(self, timestamp):        
        no = self._raiz
        
        while no:
            if timestamp == no.timestamp:
                return no.preco
            elif timestamp < no.timestamp:
                no = no.esq
            else:
                no = no.dir
        
        return None # se não encontrar retorna None

    # método para retornar uma lista de timestamp
    def range_query(self, inicio, fim):        
        resultado = []
        self._range_query(self._raiz, inicio, fim, resultado)
        return resultado

    def _range_query(self, no, inicio, fim, resultado):
        if no is None:
            return

        # busca os elementos a esquerda
        if no.timestamp > inicio:
            self._range_query(no.esq, inicio, fim, resultado)

        # visita o nó atual (in-order garante ordem crescente, sempre)
        if inicio <= no.timestamp <= fim:
            resultado.append((no.timestamp, no.preco))

        # busca os elementos a direita
        if no.timestamp < fim:
            self._range_query(no.dir, inicio, fim, resultado)

    # método para implementar o desafio
    def maximo_em_intervalo(self, inicio, fim):
        cotacoes = self.range_query(inicio, fim)
        if not cotacoes:
            return None
        return max(cotacoes, key=lambda par: par[1])[0]


# simulação do programa
if __name__ == "__main__":
    bst = ABB()

    cotacoes = [
        (1000, 62400.0),
        (1100, 63100.5),
        (1200, 61800.0),
        (1300, 64500.0),
        (1400, 65200.0),
        (1500, 63900.0),
    ]
    
    for ts, preco in cotacoes:
        bst.inserir(ts, preco)

    print("=" * 55)
    print("BUSCA EXATA")
    print("=" * 55)
    for ts in [1200, 9999]:
        print(f"  buscar({ts}) → {bst.buscar(ts)}")

    print()
    print("=" * 55)
    print("RANGE QUERY")
    print("=" * 55)
    for inicio, fim in [(1100, 1300), (1400, 1500)]:
        resultado = bst.range_query(inicio, fim)
        print(f"  range_query({inicio}, {fim}) → {resultado}")

    print()
    print("=" * 55)
    print("MÁXIMO EM INTERVALO")
    print("=" * 55)
    for inicio, fim in [(1100, 1400), (1000, 1500)]:
        ts_max = bst.maximo_em_intervalo(inicio, fim)
        preco_max = bst.buscar(ts_max)
        print(f"  maximo_em_intervalo({inicio}, {fim}) → timestamp {ts_max} | preço {preco_max}")
    print("=" * 55)