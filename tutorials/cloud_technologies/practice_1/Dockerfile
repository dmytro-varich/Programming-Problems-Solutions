# Základný obraz z Docker Hub
# Fungujúca inštalácia Alpine Linux s nainštalovaným interpreterom Python
# Výhodou je malá veľkosť
FROM python:3.8-alpine

# Nastavenie pracovného adresára kontajnera
WORKDIR /app

# Inštalácia  závislostí aplikácie
RUN pip install flask

# Kopírovanie aplikácie súborov do obrazu
COPY ./app.py /app

# Nastavenie premennej prostredia
ENV FLASK_APP app.py

# Program na spustenie
ENTRYPOINT [ "flask" ]
# Argumenty 
CMD ["run", "--host", "0.0.0.0"]