FROM python:3-slim
WORKDIR /programas/cloudbase64
RUN pip3 install fastapi pydantic uvicorn
COPY . .
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
