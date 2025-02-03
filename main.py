from metodos import *
from rutas import *

if __name__ == "__main__":
    rutas = [ruta_users, ruta_profiles, ruta_resumenes, ruta_challenges]
    nombres_tablas = ['users', 'profiles', 'resumenes', 'challenges']
    for ruta, nombre_tabla in zip(rutas, nombres_tablas):
        df_carga = abrir_csv(ruta)
        df_carga = cambiar_tipos_datos(df_carga, ruta)
        carga_datos(df_carga, nombre_tabla)