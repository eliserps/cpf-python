FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt-get update && \
   apt-get install -y gcc netcat-openbsd libpq-dev build-essential ca-certificates && \
   pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh
CMD ["/wait-for-db.sh"]