import pandas as pd

COLUMNS = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root",
    "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate", "label", "difficulty",
]

CATEGORIQUES = ["protocol_type", "service", "flag"]


def load_and_prepare():
    train = pd.read_csv("data/KDDTrain+.txt", names=COLUMNS)
    test = pd.read_csv("data/KDDTest+.txt", names=COLUMNS)

    y_train = (train["label"] != "normal").astype(int)
    y_test = (test["label"] != "normal").astype(int)

    X_train = train.drop(columns=["label", "difficulty"])
    X_test = test.drop(columns=["label", "difficulty"])

    X_train = pd.get_dummies(X_train, columns=CATEGORIQUES)
    X_test = pd.get_dummies(X_test, columns=CATEGORIQUES)

    X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

    return X_train, y_train, X_test, y_test


if __name__ == "__main__":
    X_train, y_train, X_test, y_test = load_and_prepare()
    print(f"X_train : {X_train.shape[0]} lignes x {X_train.shape[1]} colonnes")
    print(f"X_test  : {X_test.shape[0]} lignes x {X_test.shape[1]} colonnes")
    print(f"Cible : {y_train.value_counts().to_dict()}")
