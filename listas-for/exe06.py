emails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]
senacEmails = []
for e in emails:
    if e.endswith("@senac.df"):
        senacEmails.append(e)


print(senacEmails)

