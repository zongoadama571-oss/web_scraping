# =========================
# IMPORTATION DES MODULES
# =========================

# Permet d'envoyer des requêtes HTTP vers un site web
import requests

# Permet de lire et analyser le HTML
from bs4 import BeautifulSoup

# Permet de créer des tableaux de données
import pandas as pd


# =========================
# URL DU SITE
# =========================

# Adresse du site qu'on veut scraper
url = "https://books.toscrape.com"


# =========================
# ENVOI DE LA REQUÊTE
# =========================

# Envoie une requête GET au serveur
# Comme lorsqu'on ouvre un site dans Chrome
response = requests.get(url)


# =========================
# VÉRIFICATION DE LA RÉPONSE
# =========================

# Vérifie si le site a répondu correctement
# 200 = succès
if response.status_code == 200:

    print("Connexion réussie")


    # =========================
    # ANALYSE DU HTML
    # =========================

    # Transforme le HTML en objet analysable
    soup = BeautifulSoup(response.text, "html.parser")


    # =========================
    # RECHERCHE DES LIVRES
    # =========================

    # Cherche tous les articles contenant les livres
    books = soup.find_all("article", class_="product_pod")


    # =========================
    # LISTE QUI VA STOCKER LES DONNÉES
    # =========================

    # Liste vide
    # Chaque livre sera ajouté ici
    data = []


    # =========================
    # BOUCLE SUR CHAQUE LIVRE
    # =========================

    # Parcourt tous les livres trouvés
    for book in books:


        # =========================
        # EXTRACTION DU TITRE
        # =========================

        # Récupère l'attribut "title"
        # Exemple HTML :
        # <a title="Nom du livre">
        Title = book.h3.a["title"]


        # =========================
        # EXTRACTION DU PRIX
        # =========================

        # Cherche la balise :
        # <p class="price_color">
        Prix = book.find("p", class_="price_color").text


        # =========================
        # EXTRACTION DISPONIBILITÉ
        # =========================

        # Cherche :
        # <p class="instock availability">
        Disponibilité = book.find(
            "p",
            class_="instock availability"
        ).text.strip()


        # =========================
        # AJOUT DANS LA LISTE
        # =========================

        # Ajoute les informations du livre
        # sous forme de dictionnaire
        data.append({

            "Titre": Title,
            "Prix": Prix,
            "Disponibilité": Disponibilité

        })


    # =========================
    # CRÉATION DU DATAFRAME
    # =========================

    # Transforme la liste en tableau
    df = pd.DataFrame(data)


    # =========================
    # AFFICHAGE DU TABLEAU
    # =========================

    print(df)


    # =========================
    # EXPORT CSV
    # =========================

    # Crée un fichier CSV
    df.to_csv("livres.csv", index=False)


    # =========================
    # MESSAGE FINAL
    # =========================

    print("Fichier CSV créé avec succès")


# =========================
# SI ERREUR
# =========================

else:

    print("Erreur lors de la récupération du site")