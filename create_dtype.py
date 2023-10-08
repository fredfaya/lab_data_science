import arff
import pandas as pd
import json
from sklearn.model_selection import train_test_split

# Remplacez 'test_file.arff' par le chemin complet de votre fichier ARFF
file_path = 'dataset.arff'

# Creation du dtype avec python
"""with open(file_path, 'r') as f:
    data = arff.load(f)

attributes = data['attributes']
attribute_dict = {}
for attribute in attributes:
    name, attr_type = attribute
    attribute_dict[name] = attr_type


print(attribute_dict)
"""

# Chargement des donnees sans dtype
"""
print('Chargement des donnees sans dtype')
with open(file_path, 'r') as f:
    data = arff.load(f)
    # On va juste travailler avec les 5000 premieres lignes
df = pd.DataFrame(data['data'][:5000])
df.to_csv('dataset_5000.csv', index=False)
"""
# Chargement des donnees avec dtype
"""
print('Chargement des donnees avec dtype')
# lecture du fichier faite dans la partie 1
data = pd.read_csv("dataset_5000.csv")
with open("dtype_using_linux", 'r') as f:
    cols_with_types = f.read()
cols_with_types = cols_with_types.replace("'", '"')
cols_with_types = json.loads(cols_with_types)
for col, dtype in cols_with_types.items():
    if dtype == "INTEGER":
        cols_with_types[col] = "int"
    elif dtype == "REAL":
        cols_with_types[col] = "float"
    elif dtype == "STRING":
        cols_with_types[col] = "str"

cols_with_types['upselling'] = "int"

cols = [col for col, _ in cols_with_types.items()]
dtypes = {col: dtype for col, dtype in cols_with_types.items()}

# On ajoute les colonnes et le dtype
data.columns = cols
data = data.astype(dtypes)

data.to_csv('dataset_5000_with_dtype.csv', index=False)
"""
# Suppression des colonnes avec 10% de valeurs manquantes
"""
data = pd.read_csv("dataset_5000_with_dtype.csv")
missing_percentage = (data.isnull().sum() / len(data)) * 100
data = data.drop(columns=missing_percentage[missing_percentage > 10].index)
data.to_csv('dataset_5000_without_10_percents_missing_values_cols.csv', index=False)
"""
# Remplacement des valeurs manquantes par une constante avec fillna
"""
data = pd.read_csv("dataset_5000_without_10_percents_missing_values_cols.csv")
for col in data.columns:
    if data[col].dtype == 'object':
        data[col].fillna("Inconnu", inplace=True)
    else:
        data[col].fillna(-1, inplace=True)

data.to_csv('dataset_5000_without_missing_values.csv', index=False)
"""
# suppression de toutes les lignes ayant une valeure manquante
"""
data = pd.read_csv("dataset_5000_without_10_percents_missing_values_cols.csv")
nb_lignes_before = len(data)
data = data.dropna()
nb_lignes_after = len(data)
print("Nombre de lignes avant suppression : ", nb_lignes_before)
print("Nombre de lignes apres suppression : ", nb_lignes_after)
pourcentage_suppression = ((nb_lignes_before - nb_lignes_after) * 100 / nb_lignes_before)
print(f"Pourcentage de lignes supprimees : {pourcentage_suppression:.2f}%")
data.to_csv('dataset_clean_without_fill.csv', index=False)
# Division des donnees en train et test
"""
# division des donnees en train et test
"""
data = pd.read_csv("dataset_clean_without_fill.csv")
X = data.drop(columns=['upselling'])
y = data['upselling']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)
# Sauvegarde sous format csv
# train.to_csv('train.csv', index=False)
# test.to_csv('test.csv', index=False)

# Sauvegarde sous format parquet
# train.to_parquet('train.parquet', index=False)
# test.to_parquet('test.parquet', index=False)

# Sauvegarde sous format h5
# train.to_hdf('train.h5', key='train', index=False)
# test.to_hdf('test.h5', key='test', index=False)
"""