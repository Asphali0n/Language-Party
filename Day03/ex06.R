Nom = c("Alice", "Bob", "Clara", "David", "Emma", "Fred", "Gina")
Age = c(22, 25, 20, 23, 24, 26, 21)
Note = c(15, 18, 14, 16, 17, 19, 20)

etudiants = data.frame(Nom, Age, Note)

Nom_et_Note = etudiants[,c("Nom","Note")]
Nom_et_Note = subset(Nom_et_Note, Note >= 15)
print(Nom_et_Note)

