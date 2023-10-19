class Gerador:
    def __init__(self, dados_lidos):
        self.dados_lidos = dados_lidos

    def gerar_xml(self):
        xmls_gerados = []

        for dados_nota in self.dados_lidos:
            empresa = dados_nota['Empresa']
            cnpj_cpf = dados_nota['CnpjCpf']
            inscricao_municipal = dados_nota['InscricaoMunicipal']
            numero_nota = dados_nota['NumeroNota']
            serie = dados_nota['Serie']
            data_emissao = dados_nota['DataEmissao']
            valor_total = dados_nota['ValorTotal']
            base_calculo_iss = dados_nota['BaseCalculoISS']
            aliquota_iss = dados_nota['AliquotaISS']
            codigo_servico = dados_nota['CodigoServico']
            valor_deducoes = dados_nota['ValorDeducoes']
            valor_iss = dados_nota['ValorISS']
            cnpj_prestador = dados_nota['CnpjPrestador']
            razao_social_prestador = dados_nota['RazaoSocialPrestador']
            descricao = dados_nota['Descricao']
            cep = dados_nota['CEP']
            bairro = dados_nota['Bairro']
            numero = dados_nota['Numero']
            endereco = dados_nota['Endereco']
            telefone = dados_nota['Telefone']

            xml_data = {
                'Empresa': empresa,
                'CnpjCpf': cnpj_cpf,
                'InscricaoMunicipal': inscricao_municipal,
                'NumeroNota': numero_nota,
                'Serie': serie,
                'DataEmissao': data_emissao,
                'ValorTotal': valor_total,
                'BaseCalculoISS': base_calculo_iss,
                'AliquotaISS': aliquota_iss,
                'CodigoServico': codigo_servico,
                'ValorDeducoes': valor_deducoes,
                'ValorISS': valor_iss,
                'CnpjPrestador': cnpj_prestador,
                'RazaoSocialPrestador': razao_social_prestador,
                'Descricao': descricao,
                'CEP': cep,
                'Bairro': bairro,
                'Numero': numero,
                'Endereco': endereco,
                'Telefone': telefone
            }

            xml = self.gerar_xml_individual(xml_data)

            print(xml)

            xmls_gerados.append(xml)

        return '\n'.join(xmls_gerados)

    def gerar_xml_individual(self, xml_data):

	# O XML abaixo consta incompleto, para uso do que possui todos os dados é necessário verificação junto a prefeitura do munícipio
	    
        xml = f"""
        <NotaFiscal>
            <CnpjCpf>{xml_data['CnpjCpf']}</CnpjCpf>
            <InscricaoMunicipal>{xml_data['InscricaoMunicipal']}</InscricaoMunicipal>
            <NumeroNota>{xml_data['NumeroNota']}</NumeroNota>
            <Serie>{xml_data['Serie']}</Serie>
            <DataEmissao>{xml_data['DataEmissao']}</DataEmissao>
            <ValorTotal>{xml_data['ValorTotal']}</ValorTotal>
            <BaseCalculoISS>{xml_data['BaseCalculoISS']}</BaseCalculoISS>
            <AliquotaISS>{xml_data['AliquotaISS']}</AliquotaISS>
            <CodigoServico>{xml_data['CodigoServico']}</CodigoServico>
            <ValorDeducoes>{xml_data['ValorDeducoes']}</ValorDeducoes>
            <ValorISS>{xml_data['ValorISS']}</ValorISS>
            <CnpjPrestador>{xml_data['CnpjPrestador']}</CnpjPrestador>
            <RazaoSocialPrestador>{xml_data['RazaoSocialPrestador']}</RazaoSocialPrestador>
            <Descricao>{xml_data['Descricao']}</Descricao>
            <CEP>{xml_data['CEP']}</CEP>
            <Bairro>{xml_data['Bairro']}</Bairro>
            <Numero>{xml_data['Numero']}</Numero>
            <Endereco>{xml_data['Endereco']}</Endereco>
            <Telefone>{xml_data['Telefone']}</Telefone>
            <ConstrucaoCivil>
	    <CodigoObra>_</CodigoObra>
	    <Art>_</Art>
	    </ConstrucaoCivil>
        </NotaFiscal>
        """
        return xml
