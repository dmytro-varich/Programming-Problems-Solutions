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

## 🚀 Čo sa deje po spustení kontajnera?

1. **Kontrola a stiahnutie image-u**  
   Ak image `nginx` nie je dostupný lokálne, Docker ho stiahne z Docker Hub (alebo iného registry).
2. **Vytvorenie kontajnera**  
   Na základe image-u Docker vytvorí kontajner s potrebnými nastaveniami.
3. **Alokácia súborového systému**  
   Docker vytvorí vrstvený súborový systém s read-write vrstvou navrchu.
4. **Pripojenie k sieti**  
   Vytvorí sa sieťový interface a kontajner sa pripojí do defaultnej siete (bridge).
5. **Spustenie kontajnera**  
   Ak je použitý `-it`, kontajner je interaktívny a prijíma vstupy z terminálu.
6. **Ukončenie a vymazanie**  
   Pri použití `--rm` sa kontajner automaticky vymaže po `exit`.

---

## 🌐 Virtuálna sieť v Dockeri

Docker využíva **software-defined networking**, čo znamená, že siete sú definované programovo, dynamicky.

### Typy sietí (drivers):
- **`bridge`** (default) – kontajnery komunikujú medzi sebou, ale sú izolované od hostiteľa.  
- **`host`** – zdieľa sieť s hostiteľom, žiadna izolácia.  
- **`none`** – žiadna sieťová funkcionalita.  

---

## 🗂 Virtuálny súborový systém

- Každý kontajner vidí **vlastný súborový systém**.
- Docker využíva mechanizmus **Copy-on-Write (CoW)**:
  - Ak súbor existuje v image, číta sa priamo.
  - Ak sa upravuje, je skopírovaný do read-write vrstvy kontajnera.
- `docker ps -s` zobrazí:
  - `SIZE`: veľkosť dát v read-write vrstve
  - `VIRTUAL SIZE`: veľkosť image + aktuálne dáta (môže byť zdieľaná inými kontajnermi)

---

## 💾 Oddelenie dát od aplikácie

Aplikácie v Dockeri sú štandardne **stateless**. Ak potrebujeme uložiť dáta, použijeme:

### 🔹 Data Volumes
- Ukladajú **perzistentné dáta** mimo samotného kontajnera
- Vysoký výkon, flexibilita (aj cez cloudové drivere)
- Odporúčaná forma ukladania dát

### 🔸 Alternatíva: Bind Mounts
- Mappovanie medzi adresárom na hoste a v kontajneri
- Menej flexibilné a bezpečné

📦 **Príklad:**
```bash
docker run -p 80:80 -v /var/www:/var/www nginx
```
→ Mapuje porty a pripojí lokálny adresár ako volume.

---

## 🕹 Docker Swarm – Orchestration Layer

- Umožňuje **škálovanie a manažment viacerých kontajnerov** v clustri.
- Vstavaný do Docker Engine (žiadna extra inštalácia).

### Základné komponenty:
- **Node** – inštancia Docker Engine (môže byť manager alebo worker)
- **Manager** – rozhoduje, čo a kde beží, rozdeľuje úlohy, zabezpečuje **load balancing**
- **Worker** – vykonáva pridelené úlohy

### Typy služieb:
- **Replicated Service** – definuješ počet inštancií, ktoré sa majú spustiť
- **Global Service** – služba beží na **každom** node

| ![image](https://github.com/user-attachments/assets/8e594634-2d80-4ae3-8218-416635240275) | 
|:------------------------------------------:|
| Docker Swarm                      | 

### ❗️ Možné problémy
- Závislosť na Docker Hub.
- Časté využívanie neoverených obrazov.
- Docker daemon beží ako "root".

### 📍 Docker sumár
- Je virtualizačná vrstva medzi jadrom a aplikáciou.
- Umožňuje ľahko spustiť aplikáciu v cloude.
- Zjednodušie inštaláciu.
