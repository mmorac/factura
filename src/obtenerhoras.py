import pandas as pd
from datetime import datetime

def obtenerhoras(archivo):
    #Esta función leerá un archivo de Excel y obtendrá la información para retornarla como Dataframe
    df = pd.read_excel(archivo, "Hours")
    df = df.set_index(df["Resource Name"])
    df = df.fillna(0)

    cols = []
    for i in df.columns:
        if("20" in str(i)):
            cols.append(str(i).split()[0])
        else:
            cols.append(i)

    df.columns = cols

    return df
