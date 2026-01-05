# docker file

# image ufficiale di python 3.10 slim
FROM python:3.10-slim

# copiamo tutto il contenuto della cartella CD nella cartella /app del container
COPY ./6_CI_CD/CD /app

# impostiamo la working directory
WORKDIR /app

# comando di default OK
RUN ls
CMD ["python", "app.py"]