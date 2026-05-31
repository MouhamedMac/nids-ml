import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import (classification_report, confusion_matrix,
                             ConfusionMatrixDisplay)

from preprocessing import load_and_prepare

X_train, y_train, X_test, y_test = load_and_prepare()
modele = joblib.load("modele_nids.joblib")
y_pred = modele.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
print(f"Vrais negatifs  (normal -> normal)   : {tn:>6}")
print(f"Faux positifs   (normal -> attaque)  : {fp:>6}")
print(f"Faux negatifs   (attaque -> normal)  : {fn:>6}")
print(f"Vrais positifs  (attaque -> attaque) : {tp:>6}")

recall_attaque = tp / (tp + fn)
precision_attaque = tp / (tp + fp)
print(f"Detection des attaques (recall)  : {recall_attaque * 100:.1f} %")
print(f"Fiabilite des alertes (precision): {precision_attaque * 100:.1f} %")

print(classification_report(y_test, y_pred,
                            target_names=["normal", "attaque"]))

disp = ConfusionMatrixDisplay(cm, display_labels=["normal", "attaque"])
disp.plot(cmap="Blues", values_format="d")
plt.title("Matrice de confusion - Detecteur d'intrusions")
plt.tight_layout()
plt.savefig("matrice_confusion.png", dpi=120)
print("Image sauvegardee : matrice_confusion.png")
