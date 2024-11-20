import pandas as pd

class ProcesasdorCSV:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None
    
    def ler_csv(self):
        self.df = pd.read_csv(self.arquivo_csv)

    def remover_celulas_vazias(self):
        self.df.dropna(inplace=True)

    def filtrar_por_calculista(self, calculista):
        self.df = self.df[self.df['Calculista'] == calculista]

    def processar(self, calculista):
        self.ler_csv()
        self.filtrar_por_calculista(calculista)

        return self.df
    

# testando a classe
if __name__ == "__main__":
    processador = ProcesasdorCSV('liquidacao.csv')
    df = processador.processar('Rodrigo Falcao Lopes De Lima')
    print(df)


