
FROM python:3.11-slim
WORKDIR /work
COPY . /work
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "/work/src/run.py"]
