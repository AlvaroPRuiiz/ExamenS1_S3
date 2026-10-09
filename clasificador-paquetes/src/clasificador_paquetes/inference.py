
import csv
from pathlib import Path
import joblib
from clasificador_paquetes.contracts import Entrada, Salida

path = Path("data/raw/paquetes.csv")

def leer_csv(ruta: Path) -> list[Entrada]:
    # TODO:
    entrada = []
    with open(ruta, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                entrada.append(Entrada(**row))
            except ValueError:
                raise ValueError("Fila inválida en el CSV")
    if not entrada:
        raise ValueError("El CSV no contiene filas de datos")
    return entrada

def preprocesar(entrada: Entrada) -> list[float]:
    return [round(entrada.peso_kg, 1), entrada.distancia_km]

def cargar_modelo(ruta: Path):
    # TODO:cargar el modelo
    modelo = joblib.load(ruta)
    return modelo

def predecir(entrada: Entrada, modelo) -> Salida:
    #TODO
    matriz = [preprocesar(entrada)]
    categoria = modelo.predict(matriz)[0]
    probabilidades = modelo.predict_proba(matriz)[0]
    indice = probabilidades.argmax()

    return Salida(
        id_paquete=entrada.id_paquete,
        categoria=categoria,
        confianza=float(probabilidades[indice]),
    )

def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO:
    columnas_salida = ['id_paquete', 'categoria', 'confianza']
    with open(ruta, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columnas_salida)
        writer.writeheader()
        for resultado in resultados:
            fila_dict = resultado.model_dump(include=set(columnas_salida))
            writer.writerow(fila_dict)

def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO:
    modelo_cargado = cargar_modelo(modelo)

    resultados = []

    for fila in leer_csv(entrada):
        prediccion = predecir(fila, modelo_cargado)
        resultados.append(prediccion)

    guardar_csv(resultados, salida)

if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
