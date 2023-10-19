from Leitura import Leitura, mapeamento, dados_filiais
from Gerador import Gerador
import os
import time


class App:
    def __init__(self, leitura, gerador):
        self.leitura = leitura
        self.gerador = gerador

    def iniciar(self):
        try:
            if self.leitura:
                xml = self.gerador.gerar_xml()

                if xml:
                    projeto_diretorio = os.getcwd()
                    caminho_xml = os.path.join(projeto_diretorio, "output.xml")

                    with open(caminho_xml, "w", encoding="utf-8") as file:
                        file.write(xml)  # Escreve a string XML no arquivo

                    print("XML gerado e salvo com sucesso na pasta do projeto.")
                else:
                    print("Erro ao gerar XML.")
            else:
                print("Erro ao ler dados.")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    caminho_arquivo_excel = #Caminho para o arquivo do Excel a ser lido

    leitor = Leitura(caminho_arquivo_excel, dados_filiais, mapeamento)

    leitor.ler_dados()

    dados_lidos = leitor.obter_dados_lidos()

    if leitor:
        gerador = Gerador(dados_lidos)

        app = App(leitor, gerador)
        app.iniciar()
