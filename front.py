import streamlit as st # type: ignore
import random
from back import gen_password

# En-tête
col_image, col_title = st.columns([1, 4])
with col_image:
    st.image("lock.png", width=100)
with col_title:
    st.markdown(
        "<h1 style='margin: 0px; padding-top: 15px;'>Générateur de mot de passe</h1>",
        unsafe_allow_html=True
    )

st.markdown("---")

# Entrée de l'utilisateur
name = st.text_input("Nom de l'application", placeholder="ex: Gmail...")
level = st.selectbox("Choisissez le niveau de sécurité :", ["Faible", "Moyen", "Élevé"])

st.markdown("---")

# Options de compositions
col1, col2, col3 = st.columns(3)
with col1:
    maj = st.checkbox("Majuscules", value=True)
with col2:
    nbre = st.checkbox("Chiffres", value=False)
with col3:
    symboles = st.checkbox("Symboles", value=False)


# Nombre de caracteres du mot de passe selon le niveau
if level == "Faible":
    length = st.slider("Nombre de caractères", 8, 12)
elif level == "Moyen":
    length = st.slider("Nombre de caractères", 12, 16)
else:
    length = st.slider("Nombre de caractères", 16, 20)

st.markdown("---")

#Bouton de génération du mot de passe
passButton = st.button("Générer le mot de passe", use_container_width=True)

password = ""
if passButton:
    selected_types = ["lettres"]  
    if nbre:
        selected_types.append("nombres")
    if symboles:
        selected_types.append("symboles")

# Répartitons des différents types de caracteres 
    parts = [1] * len(selected_types)
    for _ in range(length - len(parts)):
        idx = random.randint(0, len(parts) - 1)
        parts[idx] += 1

    n_lettres = parts[selected_types.index("lettres")]
    n_chiffres = parts[selected_types.index("nombres")] if "nombres" in selected_types else 0
    n_symboles = parts[selected_types.index("symboles")] if "symboles" in selected_types else 0

    password = gen_password(n_lettres, n_symboles, n_chiffres)

    if not maj:
        password = password.lower()
    
# zone d'affichage finale
st.text_area(
    f"Le mot de passe de votre compte {name if name else ''} est :",
    value=password,
    disabled=True,
    height=100
)

