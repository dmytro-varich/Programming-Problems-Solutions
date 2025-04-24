# 📕 Lecture 2

## ⚙️ **OCI (Open Container Initiative)**
- **Štandardy** sú v IT mimoriadne dôležité  
- Založená pôvodnou dohodou **Docker**, **CoreOS** a ďalších industry leaderov  
- Obsahuje tri kľúčové špecifikácie:  
  1. **Runtime Specification**  
  2. **Image Specification**  
  3. **Distribution Specification**  
- Umožňuje **kompatibilitu kontajnerov** medzi rôznymi runtime-ami  
- **Príklady** kompatibilných runtime-ov:  
  - `Podman`  
  - `CRI-O`  
  - `runc` / `crun`  
  - `containerd`  
  - `Docker`  
- **Dôležité**: Štandardy fungujú naprieč ekosystémom!

---

## 🐳 **Docker**
**Docker** je open‑source platforma pre developerov na **balenie**, **distribúciu** a **spúšťanie** aplikácií v kontajneroch. Umožňuje:
- **Rýchle nasadenie** aplikácie na akomkoľvek hardware bez zložitej inštalácie či správy závislostí  
- **Izoláciu** prostredia aplikácie od hostiteľského systému  

### 🔍 Charakteristiky Dockeru
- **Virtualizačná vrstva** medzi aplikáciou a OS  
- Aplikácia používa **jadro hostiteľského OS**  
- Napísaný v **Go**  
- Využíva Linux kernel funkcie:
  - **Namespaces**  
  - **Control Groups (cgroups)**  
  - **Union file systems**  

### ✨ Výhody Dockeru
1. **Jednoduchosť** a skvelý **user experience**  
2. Konzistentné, vysoko‑úrovňové koncepty zhodné s OCI  
3. **Prenositeľnosť**: kontajnery vytvorené v Dockeri bežia aj v iných OCI‑kompatibilných enginoch  
4. Bohatá komunita a množstvo hotových image‑ov na Docker Hub

### 🛠 **Docker Komponenty**
1. **Docker Client**  
   - Príkaz `docker` v termináli (CLI).  
   - Beží na ľubovoľnom OS (Linux, macOS, Windows).  
   - Pomocou **REST API** komunikuje s Docker daemonom.

2. **Docker Daemon** (Docker Engine)  
   - **Väčšinou** beží na Linux OS alebo v Docker Machine.  
   - Spravuje objekty: **images**, **containers**, **networks**, **volumes**.  
   - Komunikuje s container runtime-ami: `containerd`, `runc`.  
   - Môže sa spojiť s ďalšími daemons (napr. pri swarm/clustering).

3. **Image Registry**  
   - Ukladá a distribuuje Docker images.  
   - **Docker Hub**: predvolený **public** registry s možnosťou **private** repozitárov.  
   - Príkazy:
     - `docker pull <image>` — stiahne image z registry  
     - `docker push <image>` — nahrá image do registry  

```
+----------+
| registry | Docker Hub
+----------+
| | (image)   
+----------+
| daemon | Host machine
+----------+
| | (REST API) 
+----------+
| client | Host machine
+----------+
```

| ![image](https://github.com/user-attachments/assets/95060ddf-fc07-4253-b1e2-649db91f3ff8) | 
|:------------------------------------------:|
| Docker Components                      | 


## 🧱 Docker Objects

Docker používa rôzne objekty na zabezpečenie svojej funkcionality. Medzi hlavné patria:

- **Images**  
- **Containers**  
- **Networks**  
- **Volumes**  
- **Plugins**  

---

### 📦 **Image**  
- **Read‑only vzor** pre spustenie kontajnera  
- Tvorba definovaná pomocou **Dockerfile**  
- Skladá sa z vrstiev (každý príkaz v Dockerfile = nová vrstva)  
- Umožňujú **odvodzovanie** (inheritance) – z jedného obrazu sa vytvorí ďalší s pridanými zmenami  

<details>
<summary>📝 Príklad Dockerfile-u</summary>

```dockerfile
# 1. Základné prostredie – Python 3.11 slim
FROM python:3.11-slim AS base

# 2. Pridáme curl pre healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# 3. Nastavíme pracovný adresár
WORKDIR /usr/local/app

# 4. Inštalujeme závislosti
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 5. Vývojová fáza (watchdog, debug)
FROM base AS dev
RUN pip install watchdog
ENV FLASK_ENV=development
CMD ["python", "app.py"]

# 6. Produkčná fáza
FROM base AS final
COPY . .
EXPOSE 80
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", \
     "--log-file", "-", "--access-logfile", "-", \
     "--workers", "4", "--keep-alive", "0"]
```

</details>

---

### 🏃 **Container**  
- **Bežiaca inštancia** image-u  
- Definovaný obrazom a jeho konfiguráciou  
- **Read‑write vrstva** na vrchu, kde sa zapisujú zmeny  
- Po zmazaní kontajnera táto vrstva zmizne, základný image zostáva nezmenený  
- Kontajner môže byť pripojený k rôznym sieťam a volumes; izolácia zabezpečená namespaces a cgroups  

#### Príkazy na spustenie  
- **Základné spustenie**:  
  ```bash
  docker run nginx
  ```  
- **Interaktívne s odstránením po ukončení**:  
  ```bash
  docker run -it --rm nginx
  ```  

### Čo sa deje po spustení?
