from src.models.store import Store
from src.models.user_aula import Usuario


class ServiceUsuario:
    def __init__(self):
        self.store = Store()

    def add_usuario(self, nome, profissao):
        if nome != None and profissao != None:
            if type(nome) == str and type(profissao) == str:
                if self.check_usuario(nome) == None:
                    usuario = Usuario(nome, profissao)
                    self.store.bd.append(usuario)
                    return "Usuario adicionado"
                else:
                    return "Usuario já existe"
            else:
                return "Usuario invalido"
        else:
            return "Usuario invalido"

    def remover_usuario(self, nome):
        user = self.check_usuario(nome)
        if user != None:
            self.store.bd.remove(user)
            return "Usuário removido com sucesso!"
        return "Usuário não encontrado"

    def update_user(self, nome, nome_novo, profissao_nova):
        user_update = self.check_usuario(nome)
        usuario_existente = self.check_usuario(nome_novo)
        if user_update != None:
            if usuario_existente == None:
                if nome_novo != None and profissao_nova != None:
                    user_update.nome = nome_novo
                    user_update.profissao = profissao_nova
                    return "Usuário atualizado com sucesso"
                else:
                    return "Usuário não pode ser atualizado"
            elif nome == nome_novo:
                if profissao_nova != None:
                    user_update.profissao = profissao_nova
                    return "Profissão atualizada com sucesso"
                else:
                    return "Usuário não pode ser atualizado"
            else:
                return "O nome que deseja atualizar já existe na base, tente outro."
        return "Usuário não encontrado"


    def check_usuario(self, nome):
        for user in self.store.bd:
            if user.nome == nome:
                return user
        return None

