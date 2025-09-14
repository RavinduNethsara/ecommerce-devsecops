
FROM python:3.11-slim
WORKDIR /app
COPY ecommerce/ ./ecommerce/
COPY README.md ./
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip &&     if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
CMD ["python", "-m", "ecommerce.demo"]
