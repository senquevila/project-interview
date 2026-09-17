# Data Visualization: FastAPI + Svelte + eCharts

App que sirve `data.json` desde un backend FastAPI y lo visualiza en el
frontend (Svelte) con dos gráficos eCharts: un pie chart y un bar plot.

## Estructura

```
├── data.json           # datos servidos por el backend
├── backend/
│   ├── main.py          # FastAPI: endpoint /api/data + estáticos del frontend
│   └── requirements.txt
├── frontend/
│   ├── src/App.svelte   # fetch a /api/data + render de los gráficos
│   └── package.json
├── Dockerfile            # build multi-stage (frontend -> backend)
└── docker-compose.yml
```

## Ejecutar con Docker (recomendado)

```bash
docker-compose up --build
```

Levanta la app en http://localhost:8000. `data.json` se monta como volumen
(`./data.json:/data.json:ro`), así que se puede editar sin reconstruir la
imagen — solo hay que reiniciar el contenedor.

## Ejecutar en local (sin Docker)

**Backend:**

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
DATA_FILE=../data.json uvicorn main:app --reload --port 8000
```

**Frontend** (en otra terminal):

```bash
cd frontend
npm install
npm run dev
```

El dev server de Vite corre en http://localhost:5173 con proxy a
`localhost:8000` para las llamadas a `/api`.

## Dependencias

- **Backend:** FastAPI, Uvicorn
- **Frontend:** Svelte, Vite, ECharts

## Variables de entorno

| Variable     | Default              | Descripción                              |
|--------------|-----------------------|-------------------------------------------|
| `DATA_FILE`  | `data.json`           | Ruta al archivo JSON que sirve `/api/data` |
| `STATIC_DIR` | `frontend/dist`       | Directorio con el build estático de Svelte |
