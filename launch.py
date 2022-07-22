from server import db

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

def check_trend(source, dataframe):
    encoder = preprocessing.LabelEncoder()
    
    states = range(1, 100, 2)
    estimators = range(1, 100)
    features = range(1, 3)
    best_model = None
    highest_score = 0

    # On crée ici nos jeux de données
    X_alltrain = dataframe.loc[:, ['nb_places_totales', 'prix_horaire']]
    y_alltrain = dataframe['rate']

    for state in states:
        X_train, X_dev, y_train, y_dev = train_test_split(X_alltrain, y_alltrain, train_size=0.6, random_state=state)

        # On va ensuite pouvoir créer notre modèle de prédiction
        for feature in features:
            nb_error = 0

            for estimator in estimators:
                model = RandomForestClassifier(n_estimators=estimator, max_features=feature, n_jobs=-1, random_state=42)
                model.fit(X_train, encoder.fit_transform(y_train))
                score = accuracy_score(encoder.fit_transform(y_dev), model.predict(X_dev))

                if nb_error > 5:
                    break

                elif score >= 1.0:
                    break

                if score > highest_score:
                    highest_score = score
                    loop_score = score
                    best_model = model
                    nb_error = 0
                    continue
                
                # Ceci nous permet de mettre en place le early-stopping et limiter le temps de calcul    
                nb_error += 1
    
    if highest_score >= 0.6:
        print("Score de prédiction: " + str(highest_score))
        return best_model
    
    return None


def start():
    source = db.MySQL()

    for city in source.get_cities():
        df = source.get_data_of_city(city)

        if len(df.index) < 4:
            continue

        df['rate'] = ((df['nb_places_totales'] - df['nb_places_libres']) / df['nb_places_totales'])

        model = check_trend(source, df)
        if model == None:
            continue

        print("La ville traitée est: " + city)

        # ici on va pouvoir définir le potentiel taux de remplissage d'un parking d'une ville
        data = pd.DataFrame(
            np.array([[100, 0], [500, 2], [1000, 1]]),
            columns=['nb_places_totales', 'prix_horaire']
        )
        
        print(model.predict(data))

if __name__ == "__main__":
    start()
