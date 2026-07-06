def cria_aluno(nome, idade, curso):
    return {"nome": nome, "idade": idade, "curso": curso}


def soma_notas(notas):
    return sum(notas.values())


def atualiza_dicionario(dicionario, **novos_valores):
    dicionario.update(novos_valores)
    return dicionario
