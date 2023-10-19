import pandas as pd


class Leitura:
    def __init__(self, caminho_arquivo_excel, dados_filiais, mapeamento_codigos):
        self.caminho_arquivo_excel = caminho_arquivo_excel
        self.dados_filiais = dados_filiais
        self.mapeamento_codigos = mapeamento_codigos
        self.dados_lidos = []

    def calcular_valor_deducoes(self, base_iss, valor_total):
        return base_iss - valor_total

    def ler_dados(self):
        try:
            colunas_desejadas = [] #Filtro para as colunas necessárias para leitura do Excel

            dados = pd.read_excel(
                self.caminho_arquivo_excel, usecols=colunas_desejadas)

            filiais_alvo = [] #Filtro para coleta somente das filais desejadas do Excel

            dados_filtrados = dados[(dados['EMPRESA'].isin(
                filiais_alvo)) & (dados['CITY'] == 'PONTA GROSSA') & (dados['VALOR_ISS'] > 0)]

            for indice, linha in dados_filtrados.iterrows():
                empresa = linha['EMPRESA']
                cnpj_tomador = self.dados_filiais.get(empresa, {'CNPJ_CPF'})
                inscricao_tomador = self.dados_filiais.get(
                    empresa, {'CNPJ_CPF'})
                num_nota = linha['NUM_NOTA']
                serie = linha['SERIE']
                data_emissao = linha['DATA_EMISSAO']
                valor_total = linha['VALOR_TOTAL']
                base_iss = linha['BASE_ISS2']
                alicota_iss = linha['ALICOTA_ISS']
                valor_iss = linha['VALOR_ISS']
                descricao = linha['DESCRICAO2']
                cnpj_prestador = linha['CNPJ']
                razao_prestador = linha['RAZAO']

                valor_deducoes = self.calcular_valor_deducoes(
                    base_iss, valor_total)

                codigo_servico = descricao[:5]
                if codigo_servico in self.mapeamento_codigos:
                    codigo_servico = self.mapeamento_codigos[codigo_servico]

                dados_nota = {
                    'Empresa': empresa,
                    'CnpjCpf': cnpj_tomador['CNPJ_CPF'],
                    'InscricaoMunicipal': inscricao_tomador['InscMunicipal'],
                    'NumeroNota': num_nota,
                    'Serie': serie,
                    'DataEmissao': data_emissao,
                    'ValorTotal': valor_total,
                    'BaseCalculoISS': base_iss,
                    'AliquotaISS': alicota_iss,
                    'CodigoServico': codigo_servico,
                    'ValorDeducoes': valor_deducoes,
                    'ValorISS': valor_iss,
                    'CnpjPrestador': cnpj_prestador,
                    'RazaoSocialPrestador': razao_prestador,
                    'Descricao': descricao,
                    'CEP': self.dados_filiais[empresa]['CEP'],
                    'Bairro': self.dados_filiais[empresa]['Bairro'],
                    'Numero': self.dados_filiais[empresa]['Numero'],
                    'Endereco': self.dados_filiais[empresa]['Endereco'],
                    'Telefone': self.dados_filiais[empresa]['Telefone'],
                }

                self.dados_lidos.append(dados_nota)

            print("Os dados foram lidos e armazenados com sucesso.")

            print("Dados Lidos:")
            for dados_nota in self.dados_lidos:
                print(dados_nota)

        except Exception as e:
            print(f"Erro ao ler planilha: {e}")

    def obter_dados_lidos(self):
        return self.dados_lidos

# Dicionário dos dados necessários das filiais para geração do XML
dados_filiais = {}
}

# Dicionário de mapeamento de códigos LCP para códigos PG
mapeamento = {
    '3.02': '3.01',
    '3.03': '3.02',
    '3.04': '3.03',
    '3.05': '3.04',
    '7.16': '7.14',
    '7.17': '7.15',
    '7.18': '7.16',
    '7.19': '7.17',
    '7.20': '7.18',
    '7.21': '7.19',
    '7.22': '7.20',
    '13.02': '13.01',
    '13.03': '13.02',
    '13.04': '13.03',
    '13.05': '13.04',
    '16.01': '16.02',
    '16.02': '16.01',
    '17.08': '17.07',
    '17.09': '17.08',
    '17.10': '17.09',
    '17.11': '17.10',
    '17.12': '17.11',
    '17.13': '17.12',
    '17.14': '17.13',
    '17.15': '17.14',
    '17.16': '17.15',
    '17.17': '17.16',
    '17.18': '17.17',
    '17.19': '17.18',
    '17.20': '17.19',
    '17.21': '17.20',
    '17.22': '17.21',
    '17.23': '17.22',
    '17.24': '17.23',
}
