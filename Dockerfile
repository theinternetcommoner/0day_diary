FROM python:3.11-alpine
WORKDIR /0day_diary
COPY requirements.txt .
ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 4500
ENTRYPOINT ["waitress-serve"]
CMD ["--listen=0.0.0.0:4500", "app:app"]