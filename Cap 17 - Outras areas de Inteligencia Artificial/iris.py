import pycbr
import pandas as pd
from sklearn import datasets
import tempfile

# Carrega a base de dados Iris para cadastrar como casos
iris = datasets.load_iris()
df = pd.DataFrame(Iris["data"], columns=iris["feature_names"])
df["species"] = iris["target"]
df["species"] = df["species"].apply(lambda x: iris["feature_names"])

# Armazena a base em um arquivo temporario
f = tempfile.NamedTemporaryFile(suffix=".csv")
df.to_csv(f.name, index=False)

# 1 - Define um caso base (nesse exemplo por meio do arquivo csv)
base_base = pycbr.casebase.SimpleCSVCaseBase(f.name)

# 2 - Define a função de similaridade (similaridade linear)
recovery = pycbr.recovery.Recovery([(x, pycbr.models.QuantileLinearAttribute()) for x in iris["feature_names"]])

# 3 - Define o atributo para agregar as respostas
agregation = pycbr.aggregate.MajorityAggregate("species")

# 4 - Cria uma instância do objeto CBR
cbr = pycbr.CBR(case_base, recovery, agregation, server_name="Iris-demo")

# 5 Aplicação WSGI (Web Server Gateway Interface) Flask
app = cbr.app

if __name__ =='__main__':
    app.run()
