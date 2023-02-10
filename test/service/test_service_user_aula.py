from src.service.service_user_aula import ServiceUsuario


class TestServiceUsuario:

    def test_add_usuario_nome_valido_profissao_valido(self):
        # Setup
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = "TechLead QA"
        resultEsperado = "Usuario adicionado"

        # Chamada
        result = service.add_usuario(nome, profissao)

        #Avaliação
        assert result == resultEsperado
        assert service.store.bd[0].nome == nome
        assert service.store.bd[0].profissao == profissao

    def test_add_usuario_nome_valido_profissao_invalida(self):
        # Setup
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = None
        resultEsperado = "Usuario invalido"
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome, profissao)

        # Avaliação
        assert result == resultEsperado
        assert  service.store.bd == store_esperado

    def test_add_usuario_nome_invalido_profissao_valida(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = None
        profissao_valido = "Eng"
        result_esperado = "Usuario invalido"
        store_esperado = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao_valido)

        # Avaliação
        assert result == result_esperado
        assert service.store.bd == store_esperado

    def test_add_usuario_nome_nao_string_profissao_valida(self):
        # Setup
        service = ServiceUsuario()
        nome_valido = 153
        profissao_valido = "Eng"
        result_esperado = "Usuario invalido"
        store_esperado = []
        nome_lista = []

        # Chamada
        result = service.add_usuario(nome_valido, profissao_valido)
        result2 = service.add_usuario(nome_lista, profissao_valido)

        # Avaliação
        assert result == result_esperado
        assert result2 == result_esperado
        assert service.store.bd == store_esperado

    def test_add_usuario_ja_existente(self):
        # SETUP
        service = ServiceUsuario()
        name = "Eduardo"
        profession = "TechLead QA"
        profession2 = "OK"
        expected = "Usuario já existe"


        # CHAMADAS
        service.add_usuario(name, profession)
        result = service.add_usuario(name, profession2)  # Add novamente o Usuário 1

        # AVALIAÇÃO
        assert result == expected
        assert len(service.store.bd) == 1

    def test_remover_usuario_com_sucesso(self):
        # SETUP
        service = ServiceUsuario()
        name = "Eduardo"
        profession = "TechLead QA"
        name2 = "Eduardo Remove"
        profession2 = "Analista QA"
        name3="Eduardo OK"
        profession3="Analista QA"

        service.add_usuario(name,profession)
        service.add_usuario(name2, profession2)
        service.add_usuario(name3, profession3)
        expected = "Usuário removido com sucesso!"

        # CHAMADA
        result = service.remover_usuario(name2)

        # AVALIAÇÃO
        assert expected == result
        assert len(service.store.bd) == 2
        assert service.check_usuario(name2) == None

    def test_remover_usuario_sem_sucesso_usuario_inexistente(self):
        # SETUP
        service = ServiceUsuario()
        nomeInvalido = None
        nomeOk = "Edu"
        profissao = "QA"
        service.add_usuario(nomeOk, profissao)
        expected = "Usuário não encontrado"

        # CHAMADA
        result = service.remover_usuario(nomeInvalido)

        # AVALIAÇÃO
        assert expected == result
        assert len(service.store.bd) == 1

    def test_remove_usuario_com_lista_vazia(self):
        # SETUP
        service = ServiceUsuario()
        nome = "Usuario nao cadastrado"
        expected = "Usuário não encontrado"

        # CHAMADA
        result = service.remover_usuario(nome)

        # AVALIAÇÃO
        assert expected == result

    def test_update_usuario_com_sucesso(self):
        # SETUP
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = "Analista QA"
        nome_novo = "Crepaldi"
        profissao_nova = "TechLead QA"
        nome2 = "Marcos"
        profissao2 = "Dev"
        esperado = "Usuário atualizado com sucesso"

        #CHAMADA
        service.add_usuario(nome, profissao)
        service.add_usuario(nome2,profissao2)
        result = service.update_user(nome2, nome_novo, profissao_nova)

        assert result == esperado
        assert service.store.bd[1].nome == nome_novo
        assert service.store.bd[1].profissao == profissao_nova
        assert len(service.store.bd) == 2

    def test_update_usuario_com_ja_existente_com_mesmo_nome(self):
        # SETUP
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = "Analista QA"
        nome_novo = "Marco"
        profissao_nova = "TechLead QA"
        nome2 = "Marco"
        profissao2 = "Dev"
        esperado = "O nome que deseja atualizar já existe na base, tente outro."

        #CHAMADA
        service.add_usuario(nome, profissao)
        service.add_usuario(nome2,profissao2)
        result = service.update_user(nome, nome_novo, profissao_nova)

        assert result == esperado
        assert service.store.bd[0].nome == nome
        assert service.store.bd[0].profissao == profissao
        assert len(service.store.bd) == 2

    def test_update_usuario_sem_ter_cadastrado_antes(self):
        # SETUP
        service = ServiceUsuario()
        nome_nao_cadastrado = "Eduardo"
        nome = "Antonio"
        profissao = "Dev"
        nome_novo = "Marco"
        profissao_nova = "TechLead QA"
        esperado = "Usuário não encontrado"

        #CHAMADA
        service.add_usuario(nome,profissao)
        result = service.update_user(nome_nao_cadastrado, nome_novo, profissao_nova)

        assert result == esperado
        assert service.store.bd[0].nome == nome
        assert service.store.bd[0].profissao == profissao
        assert len(service.store.bd) == 1

    def test_update_usuario_com_novo_nome_none(self):
        # SETUP
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = "Techlead QA"
        nome_novo = None
        esperado = "Usuário não pode ser atualizado"

        #CHAMADA
        service.add_usuario(nome,profissao)
        result = service.update_user(nome, nome_novo, profissao)

        assert result == esperado
        assert service.store.bd[0].nome == nome
        assert service.store.bd[0].profissao == profissao
        assert len(service.store.bd) == 1

    def test_update_usuario_com_nova_profissao_none(self):
        # SETUP
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = "Techlead QA"
        nova_profissao = None
        esperado = "Usuário não pode ser atualizado"

        #CHAMADA
        service.add_usuario(nome,profissao)
        result = service.update_user(nome, nome, nova_profissao)

        assert result == esperado
        assert service.store.bd[0].nome == nome
        assert service.store.bd[0].profissao == profissao
        assert len(service.store.bd) == 1

    def test_update_usuario_com_atualizando_somente_profissao(self):
        # SETUP
        service = ServiceUsuario()
        nome = "Eduardo"
        profissao = "DESENVOLVEDOR"
        nova_profissao = "TechLead QA"
        esperado = "Profissão atualizada com sucesso"

        #CHAMADA
        service.add_usuario(nome,profissao)
        result = service.update_user(nome, nome, nova_profissao)

        assert result == esperado
        assert service.store.bd[0].nome == nome
        assert service.store.bd[0].profissao == nova_profissao
        assert len(service.store.bd) == 1