
import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="FootPulse Matching", layout="centered")

st.title("🎯 Matching IA : Club ⇄ Joueur (démo FootPulse)")
st.markdown("**Tape un besoin de club pour trouver les meilleurs profils de joueurs.**")

# Exemple de base fictive
joueurs = {
    "Alex Dupont": "Milieu défensif, récupérateur agressif avec une excellente relance",
    "Sami Benali": "Ailier droit explosif, bon dribbleur, précis devant le but",
    "Hugo Moreau": "Défenseur central solide, bon jeu de tête, calme sous pression",
    "Rayan Belaïd": "Milieu créatif, forte vision de jeu, très technique",
    "Léo Giraud": "Avant-centre rapide, bonne finition, bon jeu sans ballon"
}

# Simuler des embeddings aléatoires
np.random.seed(42)
fake_embeddings = {name: np.random.rand(10) for name in joueurs.keys()}

input_text = st.text_area("🔎 Besoin du club :", placeholder="Ex : 'milieu défensif bon récupérateur avec relance'")

if st.button("🔍 Lancer le matching IA"):
    if input_text.strip() == "":
        st.warning("Merci d'entrer une description.")
    else:
        # Embedding simulé pour l'entrée
        input_embedding = np.random.rand(10)

        # Similarité cosinus
        scores = {}
        for name, emb in fake_embeddings.items():
            sim = cosine_similarity(input_embedding.reshape(1, -1), emb.reshape(1, -1))[0][0]
            scores[name] = round(float(sim), 3)

        # Afficher les meilleurs résultats
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        st.success("Top 3 correspondances IA :")
        for i, (name, score) in enumerate(sorted_scores[:3], 1):
            st.markdown(f"**{i}. {name}** — score : `{score}`")
