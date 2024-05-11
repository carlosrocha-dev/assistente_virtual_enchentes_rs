FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV GOOGLE_API_KEY=YOUR_API_KEY_HERE

CMD ["flask", "run"]
