pessoa = {
    "nome":"iago",
    "idade":22,
    "cidade":"brasilia"
}

pessoa["idade"] = 21
pessoa.setdefault("profissao", "cachorro")
print(pessoa)