import time
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from preprocessing import load_and_prepare

X_train, y_train, X_test, y_test = load_and_prepare()

modele = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)

t0 = time.time()
modele.fit(X_train, y_train)
print(f"Entraine en {time.time() - t0:.1f}s")

acc_train = accuracy_score(y_train, modele.predict(X_train))
acc_test = accuracy_score(y_test, modele.predict(X_test))
print(f"Precision entrainement : {acc_train * 100:.2f} %")
print(f"Precision test         : {acc_test * 100:.2f} %")

joblib.dump(modele, "modele_nids.joblib")
print("Modele sauvegarde dans modele_nids.joblib")
