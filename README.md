# ExamenS1_S3

Para inicializar se debe crear el proyecto con 
```bash
uv init --package clasificador-paquetes
```
Después se instala: 

```bash
uv add pydantic scikit-learn joblib numpy scipy pytest
```

Luego se haría un

```bash
uv sync 
```

y finalmente 

```bash
uv run pytest
```