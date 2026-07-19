# Stage 1
FROM python:3.11-alpine AS builder
WORKDIR /0day_diary
COPY . /0day_diary
RUN pip install --no-cache-dir -r requirements.txt

# Stage2
FROM python:3.11-alpine AS final
COPY --from=builder /0day_diary /0day_diary
WORKDIR /0day_diary
ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4500
CMD ["python", "app.py"]