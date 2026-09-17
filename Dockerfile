FROM node:20-slim AS builder
WORKDIR /frontend
COPY ./frontend .
RUN npm install
RUN npm run build

# multi stage build
# just copy the compiled frontend into the backend
FROM python:3.12-slim-bookworm
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
RUN python -m pip install --upgrade pip
COPY ./backend/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./backend .
COPY --from=builder /frontend/dist /frontend/dist
ENTRYPOINT ["python", "main.py"]
