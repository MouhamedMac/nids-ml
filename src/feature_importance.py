import joblib
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from preprocessing import load_and_prepare

X_train, _, _, _ = load_and_prepare()
modele = joblib.load("modele_nids.joblib")

importances = pd.Series(modele.feature_importances_, index=X_train.columns)
top15 = importances.sort_values(ascending=False).head(15)

for rang, (nom, score) in enumerate(top15.items(), start=1):
    print(f"{rang:>2}. {nom:<32} {score * 100:5.2f} %")

plt.figure(figsize=(9, 6))
top15.sort_values().plot(kind="barh", color="#c0392b")
plt.title("Top 15 des signaux d'alerte d'une intrusion")
plt.xlabel("Importance (poids dans les decisions du modele)")
plt.tight_layout()
plt.savefig("importance_features.png", dpi=120)
print("Image sauvegardee : importance_features.png")
