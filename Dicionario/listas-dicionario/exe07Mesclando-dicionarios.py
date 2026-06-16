dados_pessoais = {
    "nome": "Iago Estevao Escobar",
    "idade": 22,
    "cpf": "123.456.789-00",
    "cidade": "Brasilia",
    "telefone": "(61) 99238-3860"
}

dados_profissionais = {
    "cargo": "Desenvolvedor Python",
    "empresa": "Senac",
    "salario": 10000000000,
    "experiencia": "69",
    "linguagens": "Python"
}
perfil_completo = dados_pessoais|dados_profissionais
for c,v in perfil_completo.items():
    print(c,v)