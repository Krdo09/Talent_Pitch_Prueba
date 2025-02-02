from metodos import *
from rutas import *

if __name__ == "__main__":
    df_prueba = abrir_csv(ruta_challenges)
    df_prueba = cambiar_tipos_datos(df_prueba, ruta_challenges)
    #print(df_prueba)
    print(anonimizacion_datos(df_prueba, df_prueba.columns[0:2])[0])