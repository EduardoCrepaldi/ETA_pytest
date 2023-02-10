from src.models.user import User
from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_usuario_nome_valido_profissao_valido_cpf_valido(self):
        # Setup
        service = ServiceUser()
        user = User(name="Eduardo", profession="TechLead QA", cpf="012.345.678-90")
        expected = "Usuário adicionado"

        # Chamada
        result = service.add_usuario(user)

        #Avaliação
        assert result == expected
        assert service.store.bd[0].name == user.name
        assert service.store.bd[0].profession == user.profession
        assert service.store.bd[0].cpf == user.cpf

    def test_add_usuario_nome_valido_profissao_valida_cpf_invalido(self):
        #SETUP
        service = ServiceUser()
        user = User(name="Eduardo CPF inválido",
                    profession="TechLead QA",
                    cpf=None)
        expected = "Usuário inválido"

        #CHAMADA
        result = service.add_usuario(user)

        #AVALIAÇÃO
        assert result == expected
        assert service.store.bd == []

    def test_add_usuario_nome_valido_cpf_valido_profissao_invalida(self):
        # Setup
        service = ServiceUser()
        user = User(name="Eduardo",
                    profession=None,
                    cpf="012.345.678-90")
        expected = "Usuário inválido"
        expected_store = []

        # Chamada
        result = service.add_usuario(user)

        # Avaliação
        assert result == expected
        assert service.store.bd == expected_store

    def test_add_usuario_profissao_valida_cpf_valido_nome_invalido(self):
        # Setup
        service = ServiceUser()
        user = User(name=None,
                    profession="Eng",
                    cpf="012.345.678-90")
        expected = "Usuário inválido"
        expected_store = []

        # Chamada
        result = service.add_usuario(user)

        # Avaliação
        assert result == expected
        assert service.store.bd == expected_store

    def test_add_usuario_nome_nao_string_profissao_valida_cpf_valido(self):
        # SETUP
        service = ServiceUser()
        user_number = User(name=153,
                    profession="Eng",
                    cpf="012.345.678-90")

        user_list = User(name=[],
                          profession="Eng",
                          cpf="012.345.678-90")
        expected = "Usuário inválido"
        expected_store = []

        # CHAMADA
        result = service.add_usuario(user_number)
        result2 = service.add_usuario(user_list)

        # AVALIAÇÃO
        assert result == expected
        assert result2 == expected
        assert service.store.bd == expected_store

    def test_add_usuario_cpf_existente(self):
        #SETUP
        service = ServiceUser()
        user1 = User(name="Eduardo",
                     profession="TechLead QA",
                     cpf="012.345.678-90")

        user2 = User(name="Eduardo",
                     profession="Analista QA",
                     cpf="098.765.432-10")
        expected = "Usuário já existe"

        #CHAMADAS
        service.add_usuario(user1)
        service.add_usuario(user2)
        result = service.add_usuario(user1) #Add novamente o Usuário 1

        #AVALIAÇÃO
        assert result == expected
        assert len(service.store.bd) == 2

    def test_remover_usuario_com_sucesso(self):
        #SETUP
        service = ServiceUser()
        user1 = User(name="Eduardo",
                     profession="TechLead QA",
                     cpf="012.345.678-90")

        user2 = User(name="Eduardo Remove",
                     profession="Analista QA",
                     cpf="098.765.432-10")
        user3 = User(name="Eduardo",
                     profession="Analista QA",
                     cpf="198.765.432-10")
        service.add_usuario(user1)
        service.add_usuario(user2)
        service.add_usuario(user3)
        expected = "Usuário removido com sucesso!"

        #CHAMADA
        result = service.remove_user(user2)

        #AVALIAÇÃO
        assert expected == result
        assert len(service.store.bd) == 2
        assert user2 not in service.store.bd

    def test_remover_usuario_sem_sucesso_user_none(self):
        #SETUP
        service = ServiceUser()
        user = None
        user_ok = User(name="Edu", profession="QA", cpf="012.345.678-90")
        service.add_usuario(user_ok)
        expected = "Usuário inválido"

        #CHAMADA
        result = service.remove_user(user)

        #AVALIAÇÃO
        assert expected == result
        assert user_ok in service.store.bd

    def test_remover_usuario_sem_sucesso_usuario_inexistente(self):
        # SETUP
        service = ServiceUser()
        user_not_exist = User(name="Usuario nao inserido", profession="Inexistente", cpf="333.444.111-90")
        user_ok = User(name="Edu", profession="QA", cpf="012.345.678-90")
        service.add_usuario(user_ok)
        expected = "Usuário não encontrado"

        # CHAMADA
        result = service.remove_user(user_not_exist)

        # AVALIAÇÃO
        assert expected == result
        assert user_ok in service.store.bd

    def test_remove_usuario_com_lista_vazia(self):
        #SETUP
        service = ServiceUser()
        user = User(name="Usuario nao cadastrado", profession="Teste", cpf="012.345.678-90")
        expected = "Usuário não encontrado"

        #CHAMADA
        result = service.remove_user(user)

        #AVALIAÇÃO
        assert expected == result

    def test_update_usuario_com_sucesso(self):
        # SETUP
        service = ServiceUser()
        user = User(name="Eduardo CPF inválido",
                    profession="TechLead QA",
                    cpf="ABC")
        service.add_usuario(user)

        service.update_user(user,"OLA", "ABC", "DR")

        assert service.store.bd[0].name == "OLA"
