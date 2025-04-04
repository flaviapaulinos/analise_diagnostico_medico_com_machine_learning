from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"


DADOS_ORIGINAIS = PASTA_DADOS / "breast-cancer.csv"
DADOS_LIMPOS = PASTA_DADOS / "breast-cancer-clean.parquet"


PASTA_MODELOS = PASTA_PROJETO / "modelos"

PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
RELATORIO = PASTA_RELATORIOS / "00-fbps-eda.html"
MODELO_LINEAR_REGRESSION = PASTA_MODELOS / "lr.pkl"
MODELO_LINEAR_REGRESSION_REDUCAO_FEATURES = PASTA_MODELOS / "lr_red_feat.pkl"
MODELO_DECISION_TREE = PASTA_MODELOS / "decision_tree.pkl"
MODELO_SVC = PASTA_MODELOS / "svc.pkl"