import pandas as pd

from imblearn.pipeline import Pipeline

from sklearn.metrics import fbeta_score, make_scorer
from sklearn.model_selection import KFold, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline

RANDOM_STATE = 42

def construir_pipeline_modelo_classificacao(classificador, preprocessor=None):
    if preprocessor is not None:
        pipeline = Pipeline([("preprocessor", preprocessor), ("clf", classificador)])
    else:
        pipeline = Pipeline([("clf", classificador)])

    model = pipeline

    return model

def treinar_e_validar_modelo_classificacao(
    X,
    y,
    cv,
    classificador,
    preprocessor=None,
    multi_class=False,
    beta=2  # Parâmetro beta para o fbeta_score
):
    model = construir_pipeline_modelo_classificacao(
        classificador,
        preprocessor,
    )

    # Definindo as métricas como um dicionário
    scoring = {
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
        "f1": "f1_weighted" if multi_class else "f1",
        "precision": "precision_weighted" if multi_class else "precision",
        "recall": "recall_weighted" if multi_class else "recall",
        "roc_auc": "roc_auc_ovr" if multi_class else "roc_auc",
        "average_precision": "average_precision",
        "f2_score": make_scorer(fbeta_score, beta=beta, average='weighted' if multi_class else 'binary')
    }

    scores = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=scoring,  # Passando o dicionário de métricas
    )

    return scores


def grid_search_cv_classificador(
    classificador,
    param_grid,
    cv,
    preprocessor=None,
    return_train_score=False,
    refit_metric="roc_auc",
    multi_class=False,
    beta=2  # Parâmetro beta para o fbeta_score
):
    model = construir_pipeline_modelo_classificacao(classificador, preprocessor)

    # Criando o scorer para fbeta_score
    fbeta_scorer = make_scorer(fbeta_score, beta=beta, average='weighted' if multi_class else 'binary')

     # Definindo as métricas como um dicionário
    scoring = {
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
        "f1": "f1_weighted" if multi_class else "f1",
        "precision": "precision_weighted" if multi_class else "precision",
        "recall": "recall_weighted" if multi_class else "recall",
        "roc_auc": "roc_auc_ovr" if multi_class else "roc_auc",
        "average_precision": "average_precision",
        "f2_score": make_scorer(fbeta_score, beta=beta, average='weighted' if multi_class else 'binary')
    }
    grid_search = GridSearchCV(
        model,
        cv=cv,
        param_grid=param_grid,
        scoring=scoring,
        refit=refit_metric,
        n_jobs=-1,
        return_train_score=return_train_score,
        verbose=1,
    )
       

    return grid_search

def organiza_resultados(resultados):

    for chave, valor in resultados.items():
        resultados[chave]["time_seconds"] = (
            resultados[chave]["fit_time"] + resultados[chave]["score_time"]
        )

    df_resultados = (
        pd.DataFrame(resultados).T.reset_index().rename(columns={"index": "model"})
    )

    df_resultados_expandido = df_resultados.explode(
        df_resultados.columns[1:].to_list()
    ).reset_index(drop=True)

    try:
        df_resultados_expandido = df_resultados_expandido.apply(pd.to_numeric)
    except ValueError:
        pass

    return df_resultados_expandido