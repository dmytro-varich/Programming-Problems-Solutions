## 🐳 **Základné príkazy Dockeru**

| Príkaz | Popis |
|-------|-------|
| `docker --version` | Zistíš verziu Dockeru |
| `docker info` | Zobrazí detaily o Docker inštancii |
| `docker help` | Zobrazí nápovedu ku všetkým príkazom |

---

## 📦 **Práca s kontajnermi**

| Príkaz | Popis |
|-------|-------|
| `docker run <image>` | Spustí nový kontajner z image |
| `docker run -it <image> bash` | Spustí interaktívny shell v kontajneri |
| `docker ps` | Zoznam bežiacich kontajnerov |
| `docker ps -a` | Zoznam všetkých kontajnerov (aj zastavených) |
| `docker stop <container>` | Zastaví kontajner |
| `docker start <container>` | Spustí už existujúci kontajner |
| `docker rm <container>` | Odstráni kontajner |
| `docker logs <container>` | Výpis logov z kontajnera |
| `docker exec -it <container> bash` | Otvorí shell v bežiacom kontajneri |

---

## 🛠️ **Práca s images**

| Príkaz | Popis |
|-------|-------|
| `docker images` | Zoznam dostupných Docker images |
| `docker build -t <meno>:<tag> .` | Vytvorí image z Dockerfile |
| `docker pull <image>` | Stiahne image z Docker Hubu |
| `docker push <image>` | Nahraje image na Docker Hub |
| `docker rmi <image>` | Odstráni image |
| `docker tag <lokálny_image> <repo/image:tag>` | Premenuje alebo označí image |

---

## 🔗 **Siete a objemy**

| Príkaz | Popis |
|-------|-------|
| `docker network ls` | Zoznam Docker sietí |
| `docker volume ls` | Zoznam objemov (volumes) |
| `docker network create <meno>` | Vytvorí vlastnú sieť |
| `docker volume create <meno>` | Vytvorí objem pre ukladanie dát |

---

## 🔁 **Docker Compose (ak používaš docker-compose.yml)**

| Príkaz | Popis |
|-------|-------|
| `docker-compose up` | Spustí všetky služby |
| `docker-compose up -d` | Spustí služby na pozadí |
| `docker-compose down` | Zastaví a odstráni služby |
| `docker-compose build` | Vybuduje images zo súboru |
| `docker-compose logs` | Zobrazí logy všetkých služieb |
