# ==========================================
# IMPORTATION DE REQUESTS
# ==========================================

import requests


# ==========================================
# CLÉ API
# ==========================================

api_key = "f1df6f1173c649f0a05ec454132db1fa"


# ==========================================
# NOM DE LA VILLE
# ==========================================

ville = "Ouagadougou"


# ==========================================
# URL API
# ==========================================

url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric"


# ==========================================
# REQUÊTE API
# ==========================================

response = requests.get(url)


# ==========================================
# VÉRIFICATION
# ==========================================

if response.status_code == 200:

    print("Connexion réussie !")


    # JSON -> Python
    data = response.json()


    # Voir tout le JSON
    print(data)

    print("\n====================\n")


    # ==========================================
    # EXTRACTION DES DONNÉES
    # ==========================================

    temperature = data["main"]["temp"]

    humidite = data["main"]["humidity"]

    description = data["weather"][0]["description"]

    pays = data["sys"]["country"]


    # ==========================================
    # AFFICHAGE
    # ==========================================

    print("pays :", pays)

    print("Ville :", ville)

    print("Température :", temperature, "°C")

    print("Humidité :", humidite, "%")

    print("Description :", description)


else:

    print("Erreur :", response.status_code)
