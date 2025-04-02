from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"


DADOS_ORIGINAIS = PASTA_DADOS / "breast-cancer.csv"
DADOS_LIMPOS = PASTA_DADOS / "breast-cancer-clean.parquet"


PASTA_MODELOS = PASTA_PROJETO / "modelos"

PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
RELATORIO = PASTA_RELATORIOS / "00-fbps-eda.html"