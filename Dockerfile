FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY visitors.py .
ENV PORT=8000
EXPOSE 8000
RUN useradd --create-home appuser
USER appuser
CMD ["python", "visitors.py"]
