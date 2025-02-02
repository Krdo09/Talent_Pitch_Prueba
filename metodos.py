from pathlib import Path
from rutas import *
from datetime import date
import pandas as pd
import numpy as np
import sys


def abrir_csv(ruta_archivo: Path) -> pd.DataFrame:
    """
    Convierte los archivos .csv a un DataFrame de pandas

    Parameters:
    ruta_archivo: ruta del archo tranformado en un objeto tipo pathlib | type pathlib.PATH

    Returns:
    df: .csv cargado en pandas | type pd.DateFrame
    """
    try:
        # Abrir csv
        df = pd.read_csv(ruta_archivo.as_posix())
        # Mensaje de carga exitosa
        print(f"Se cargo exitosamente el archivo: {ruta_archivo.stem}{ruta_archivo.suffix}")

        return df

    except Exception as error:
        # Se capturan errores 
        print(f"A ocurrido un error, revisar función 'abrir_csv': {error}")
        sys.exit(1)

def cambiar_tipos_datos(df: pd.DataFrame, ruta_archivo: Path) -> pd.DataFrame:
    """
    Dado un df cambia las columnas al tipo de dato adecuado para su carga en la DB

    Parameters:
    df: DataFrame que se desea cargar en la DB | type pd.DataFrame

    Return:
    df: DataFrame con el cambio de tipo de dato correcto
    """
    try:
        # Validar nombre de cada archivo
        
        if ruta_archivo.stem == ruta_users.stem:
            # Se asignan tipos de datos para cada columna
            tipos_columnas = {'id': int,
                              'name': str,
                              'identification_number': str,
                              'slug': str,
                              'video': str,
                              'email': str,
                              'gender': str,
                              'created_at': 'datetime64[ns]',
                              'updated_at': 'datetime64[ns]'}
            # Se realiza cambio de datos
            df = df.astype(tipos_columnas)
        
        elif ruta_archivo.stem == ruta_profiles.stem:
            # Se asignan tipos de datos para cada columna
            tipos_columnas = {'id': int,
                              'user_id': int,
                              'onboarding_goal': str,
                              'created_at': 'datetime64[ns]',
                              'updated_at': 'datetime64[ns]',
                              'views': int}            
            # Se realiza cambio de datos
            df = df.astype(tipos_columnas)

        elif ruta_archivo.stem == ruta_resumenes.stem:
            # Se asignan tipos de datos para cada columna
            tipos_columnas = {'id': int,
                              'user_id': int,
                              'name': str,
                              'type': str,
                              'video': str,
                              'views': int,
                              'created_at': 'datetime64[ns]'}
            # Se realiza cambio de datos
            df = df.astype(tipos_columnas)
        
        elif ruta_archivo.stem == ruta_challenges.stem:
            # Se asignan tipos de datos para cada columna
            tipos_columnas = {'id': int,
                              'name': str,
                              'description': str,
                              'status':str,
                              'opencall_objective': str,
                              'created_at': 'datetime64[ns]'}
            # Se realiza cambio de datos
            df = df.astype(tipos_columnas)
           
        # Cambiar datos tipo np.NaN por None, dado que la DB solo acepta tipos NULL que son equivalentes a None 
        df = df.replace({'nan': None})


        return df

    except Exception as error:
        print(f"Error en la transformación de datos, revisar función 'cambiar tipos_datos' {error}")
        # Cerrar el programa
        sys.exit(1)