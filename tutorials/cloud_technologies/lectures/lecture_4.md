# 📕 Lecture 4 - Tvorba cloud riešenia

## 🗳 Microservices

Dnešné moderné aplikácie sú čoraz častejšie tvorené ako kolekcia **mikroslužieb**. Ide o prístup, ktorý nadväzuje na service-oriented architecture (SOA), no ide ešte ďalej – do modularity, nezávislosti a flexibility.

| ![image](https://github.com/user-attachments/assets/756480d3-6750-4699-a1bb-e225e3e533fd) | 
|:------------------------------------------:|
| Difference between Microservices and Monolithic Architecture                    | 

### Čo sú Microservices?

Mikroslužby sú malé, samostatne vyvíjané a nasadzované komponenty aplikácie. Každá z nich má:

- **Vlastnú funkcionalitu**, ktorú implementuje – napríklad autentifikácia, správa používateľov, platby atď.
- **Vlastný vývojový cyklus** – môže byť nasadzovaná, aktualizovaná či testovaná nezávisle od ostatných.
- **Vlastné úložiská a závislosti** – každá služba má svoju databázu, konfigurácie a knižnice.
- **Vlastný proces** – beží samostatne a komunikuje s ostatnými službami pomocou API (často REST, gRPC).
- Spolu tieto služby **tvoria aplikáciu ako celok**, kde každá robí svoju časť a dohromady vytvárajú komplexný systém.

### Prečo používať Microservices?

- **Lepšia škálovateľnosť** – možno škálovať len tú službu, ktorú potrebujeme.
- **Flexibilnejší vývoj** – tímy môžu pracovať paralelne na rôznych častiach systému.
- **Jednoduchšia údržba** – menšie kódy znamenajú menej chýb a rýchlejšie opravy.

---

### Výzvy pri práci s mikroslužbami

Aj keď sú mikroslužby silným architektonickým riešením, prinášajú aj svoje výzvy:

- **Komunikácia** – Ako zabezpečiť, aby služby vedeli, kedy a s kým majú komunikovať? Potrebujeme dobre definované API a protokoly.
- **Odolnosť systému** – Čo ak niektorá služba vypadne? Potreba riešiť fallbacky, retry mechanizmy, circuit breakery.
- **Distribuované dáta** – Každá služba má vlastné dáta, ale niekedy potrebujeme ich zdieľať. Riešime konzistenciu a synchronizáciu.
- **Bezpečné uchovávanie tajomstiev** – Konfigurácie, heslá, API kľúče… Musia byť bezpečne uložené a dostupné len oprávneným službám.

---

## ▶️ CI/CD
`Continuous integrations` is DevOps software development practice where developers regularly merge their code changes into a central 
repository, after which automated builds and tests are run.

`Continuous delivery` is a software development practice where code changes are automatically build. 
tested, and prepared for a release to production.

> Infrastructure as a code - umožňuje definovať infraštruktúru pomocou kódu.

## 🔁 DevOps
Software development (Dev) + Operations (Ops). Set praktík, pre automatizáciu a optimalizáciu dodávania Software,
snažíme sa optimalizovať kvalitu a čas dodania. `Planning`, `Coding`, `Building`, `Testing`, `Packaging`, `Releading`, `Configuring`, `Monitoring`.

| ![image](https://github.com/user-attachments/assets/64f39add-09ce-4c53-8fab-f252f841e1d4) | 
|:------------------------------------------:|
| DevOps                    | 

**Fázy DevOps:**
- **Pred depoyom:** Plan, Test, Code, Build, Test, Release.
- **Po deployi:** Deploy, Operate, Monitor, Test.

| ![image](https://github.com/user-attachments/assets/c96984c2-f966-4c3c-9006-30d24d03f620) | 
|:------------------------------------------:|
| Phases of DevOps                    | 


## 💻 Cloud aplikácie
- **Cloud-native:** design je od začiatku navrhnutý pre cloud.
- **Cloud-based:** používa niektoré schopnosti cloudu, napr. škálovateľnosť.
- **Cloud-enabled:** zväčša klasická aplikácia premigrovaná do cloudu.

### Cloud Native 
Cloudové technolóhie umožňujú organizáciám vytvárať a prevádzkovať škálovateľné aplikácie v moderných
dynamických prostrediach, ako sú verejné, súkromné a hybridné cloudy. Príkladom tohto prístupu sú
kontajnery, siete služieb, mikroslužby, nemenná infraštruktúra a deklaratívne API. 

Tieto techniky umožňujú voľne viazané systémy, ktoré sú odolné, spravovateľne a pozorovateľné. 
V kombinácii s robustnou automatizáciou umožňujú inžinierom vykonávať zmeny s veľkým vplyvom často 
a predvídateľne s minimálnou námahou.

| **Company** | **Number of Services in Production** | **Deployment Frequency**                   |
|-------------|--------------------------------------|---------------------------------------------|
| **Netflix** | 600+                                 | 100 raz na deň                              |
| **Uber**    | 1,000+                               | Niekoľko raz na tyždeň                |
| **WeChat**  | 3,000+                               | 1,000 krát na deň                            |

**Výhody Cloudu Native:**
- Efektívnejšie
- Lacnejšie
- Rýchlejšie na trhu
- Dostupnejšie
- Škálovateľnejšie a flexibilnejšie

### ☁️ **Microsoft – Piliery Cloud-Native**
- **Cloud-first prístup**
- **PaaS (Platform as a Service)**
- **Princíp "Pets vs Cattle"** – namiesto správy konkrétnych serverov pracujeme s abstrakciami
- **Moderný návrh aplikácií** (napr. 12-Factor App)
- **Mikroslužby**
- **Kontajnery**
- **Externé služby (Backing services)** – databázy, messaging, monitoring, identita...
- **Automatizácia**
  - IaC – Infrastructure as Code
  - CI/CD – automatizované nasadzovanie

---

### 🔧 **Google – Princípy Cloud-Native**
- **Dizajn pre automatizáciu** – infra, škálovanie, monitoring, recovery
- **Chytré narábanie so stavom** – stav aplikácie je najťažšia časť
- **Preferuj managed služby** – úspora nákladov, menej komplexity
- **Defense in Depth** – minimálna dôvera medzi komponentmi, silná autentifikácia
- **Neustále architektuj** – cloud-native systémy sa stále vyvíjajú

---

### 🛠 **AWS – Cloud-Native Prístup**

#### Architektúra:
- **Immutable infraštruktúra**
- **Mikroslužby + API-first**
- **Service Mesh** – vrstva komunikácie medzi službami
- **Kontajnery**

#### Vývoj:
- **CI/CD**
- **DevOps kultúra**
- **Serverless** – bez správy serverov, výpočty a škálovanie rieši poskytovateľ


| ![image](https://github.com/user-attachments/assets/fd2bdbc7-b7b7-4520-b647-d84888bb1e56) | 
|:------------------------------------------:|
| Most popular cloud technoogiess 2017                    | 

## ☁️ Edge, Fog Cloud Computing

1. `Edge computing` znamená spracovanie dát **priamo** na okraji siete, teda čo najbližšie k 
zariadeniam, ktoré tieto dáta generujú (senzory, kamery, IoT zariadenia...).

> Cieľom je **minimalizovať latecniu**, znížiť záťaž siete a zabezpečiť **rýchlu reakciu**.

 **Príklad:**
 - Samojazdiace auto analyzuje obraz z kamier a rozhofuje v reálnom čase lokálne, bez potreby odosielania dát do cloudu.
 - Smart kamera v továrni detekuje poruchu stroja a okamžite reaguje.

2. `Fog computing` je **medzivrstva medzi edge zariadeniami a centrálnym cloudom**. Spracováva časť
dát bližšie k zdroju ako cloud, ale nie priamo na zariadení ako edge.

> Slúži ako **lokálny dátový uzol** - vykonáva predspracovanie, filtrovanie alebo agregáciu dát.

 **Príklad:**
 - Výrobný závod má **lokálnu server**, ktorý zbiera a spracováva dáta zo všetkých IoT senzorov v hale,
predtým než sa dáta odošlú do cloudu.
- Smart mesto používa fog uzly na riadenie dopravy - každý uzol spracuje dáta z okolitých kamier a semaforov.

### Rýchle porovnanie:

| Vlastnosť            | Edge                       | Fog                              |
|----------------------|----------------------------|----------------------------------|
| Kde sa spracúva?     | Priamo na zariadení        | Na miestnom uzle / gateway       |
| Latencia             | Veľmi nízka                | Nízka                            |
| Výpočtová sila       | Limitovaná                 | Vyššia ako edge, nižšia ako cloud |
| Príklad použitia     | Samojazdiace auto          | Továreň so senzorovou sieťou     |

| ![image](https://github.com/user-attachments/assets/bb5c6caa-0b17-4e7a-a19c-f3607cb21853) | 
|:------------------------------------------:|
| Edge, Fog, Cloud Computing                   | 
