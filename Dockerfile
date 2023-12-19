# Docker imajını temel olarak Python 3.9 kullan
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Çalışma dizinini belirle
WORKDIR /app

# Gerekli dosyaları kopyala
COPY main.py .
COPY XGB_model.pkl .
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı çalıştır
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
