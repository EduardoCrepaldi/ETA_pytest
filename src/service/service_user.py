from src.models.store import Store


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_usuario(self, user):
        if user.name != None and user.profession != None and user.cpf != None:
            if self.exist_user(user.cpf) != None:
                return "Usuário já existe"
            elif type(user.name) == str and type(user.profession) == str:
                self.store.bd.append(user)
                return "Usuário adicionado"
            else:
                return "Usuário inválido"
        else:
            return "Usuário inválido"

    def remove_user(self, user):
        if user != None:
            if user in self.store.bd:
                self.store.bd.remove(user)
                return "Usuário removido com sucesso!"
            else:
                return "Usuário não encontrado"
        return "Usuário inválido"

    def update_user(self, user, name, cpf, profession):
        user_bd = self.exist_user(user.cpf)

        if user != None and user_bd != None:
            if user_bd.cpf == cpf:
                user_bd.name = name
                user_bd.profession = profession
                return "Usuário atualizado com sucesso"
            return "CPF já cadastrado para outro usuário"

        return "Usuário não encontrado"




    def exist_user(self, cpf):
        for user in self.store.bd:
            if user.cpf == cpf:
                return user
        return None


