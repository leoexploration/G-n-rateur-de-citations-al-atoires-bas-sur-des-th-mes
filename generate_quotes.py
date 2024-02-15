import random

# Dictionnaire de citations par thème
citations_par_theme = {
    "inspiration": [
        "La seule façon de faire du bon travail est d'aimer ce que vous faites. - Steve Jobs",
        "La vie est soit une grande aventure ou rien du tout. - Helen Keller",
        "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme. - Winston Churchill"
    ],
    "motivation": [
        "Le succès n'est pas final, l'échec n'est pas fatal : c'est le courage de continuer qui compte. - Winston Churchill",
        "Tout ce que vous pouvez imaginer, vous pouvez le réaliser. Tout ce que vous pouvez rêver, vous pouvez le devenir. - William Arthur Ward",
        "Ne rêvez pas votre vie, vivez vos rêves. - Mark Twain"
    ],
    "humour": [
        "Le seul moyen de se débarrasser d'une tentation, c'est d'y céder. - Oscar Wilde",
        "La vie n'est pas un problème à résoudre, mais une réalité à expérimenter. - Soren Kierkegaard",
        "Je ne suis pas paresseux, je suis juste très motivé à ne rien faire. - Garfield"
    ]
}

def generer_citation(theme="aleatoire"):
    """Génère une citation aléatoire basée sur un thème donné."""
    if theme == "aleatoire":
        theme = random.choice(list(citations_par_theme.keys()))
    citations = citations_par_theme.get(theme)
    if citations:
        return random.choice(citations)
    else:
        return "Thème non trouvé. Veuillez choisir un thème parmi : " + ", ".join(citations_par_theme.keys())

if __name__ == "__main__":
    # Demander à l'utilisateur de choisir un thème
    print("Bienvenue dans le générateur de citations !")
    print("Thèmes disponibles : inspiration, motivation, humour")
    theme = input("Entrez un thème ou appuyez sur Entrée pour un thème aléatoire : ")

    # Générer et afficher la citation
    citation = generer_citation(theme.lower())
    print("Citation générée :", citation)
