from pathlib import Path
import pandas as pd
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

        print(f"Se cargo exitosamente el archivo: {ruta_archivo.stem}{ruta_archivo.suffix}")

        return df

    except Exception as error:
        print(f"A ocurrido un error, revisar función 'abrir_csv': {error}")
        sys.exit(1)