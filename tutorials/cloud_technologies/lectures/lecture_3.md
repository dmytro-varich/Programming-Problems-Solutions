# 📕 Lecture 3

## 🌐 Príklady firiem a ich PaaS riešení

### 🔧 **Siemens – MindSphere**
- 🛠 *"Operačný systém"* pre **IoT aplikácie a priemyselné riešenia**
- ☁️ Hostované na: **AWS (Amazon Web Services)**

---

### ⚙️ **GE – Predix**
- 🌍 Prvá **IoT industriálna cloudová platforma**
- 🎯 Zameraná na **analýzu dát zo senzorov a strojov**
- ☁️ Hostované na: **Azure**

---

### 🚀 **Heroku**
- 👩‍💻 Platforma pre vývojárov – umožňuje:
  - Buildovanie aplikácií
  - Nasadzovanie
  - Škálovanie
  - Manažovanie
- 💼 Vlastník: **Salesforce**
- ☁️ Hostované na: **AWS**

---

### 👥 **Workday**
- 📊 Riešenia pre:
  - **HR (ľudské zdroje)**
  - **Finančný manažment**
  - **Plánovanie**
- 🔄 Pôvodne **SaaS**, rozšírené o **PaaS**:
  - Prístup k API
  - Možnosť rozšíriť funkcionalitu
  - Práca nad dátami zo SaaS systému

## 🤝 Podľa čoho sa firmy najčastejšie rozhodujú? 
| 🧩 Kritérium                        | 📝 Popis                                                                                                                                           |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Konkrétna služba**              | - Môže byť „gamechanger“ pre danú aplikáciu<br>- Exkluzívna dohoda s 3. stranou                                                                  |
| **Dostupnosť služieb**            | - Regionálna dostupnosť<br>- Uptime / downtime                                                                                                   |
| **Dostupnosť ľudí**               | - Požiadavky na certifikovaných špecialistov<br>- Dôvera zo strany zákazníkov                                                                     |
| **Disaster recovery**             | - Ako rýchlo je možné obnoviť služby?<br>- Záloha a istota prístupu k dátam                                                                        |
| **Podmienky používania**          | - Malé firmy = štandardné podmienky<br>- Veľké firmy = vyjednané zmluvy<br>- Zákaznícka podpora                                                  |
| **Cena**                          | - Priamy vplyv na rozhodovanie<br>- Potreba transparentného modelu                                                                                |
| **Migrácia a vendor lock-in**     | - Dostupnosť nástrojov na migráciu<br>- Riziko uzamknutia na jedného providera                                                                   |
| **Ochrana súkromia**              | - GDPR a právna zodpovednosť za prenos dát mimo EÚ                                                                                                |
| **Bezpečnosť**                    | - Certifikácie (napr. ISO 27001)<br>- Audity, monitoring<br>- Šifrovanie dát                                                                      |

## 🏠 Self-hosting

**Self-hosting** označuje prax nasadzovania a prevádzkovania softvérových riešení (aplikácií, služieb, platforiem) **na vlastnej infraštruktúre**, namiesto využitia cloudu od externých providerov (napr. AWS, Azure, GCP).

| 💡 Kategória                     | 📝 Popis |
|----------------------------------|---------|
| **Definícia**                    | Prevádzka softvéru na vlastných serveroch alebo dátových centrách – v plnej réžii firmy alebo jednotlivca. |
| **Rozdiel oproti on-premise**    | - **On-premise**: tradičné nasadenie softvéru v rámci internej IT infraštruktúry firmy.<br>- **Self-hosting**: širší pojem, môže zahŕňať aj nasadenie v cloude, ktorý firma sama kontroluje (napr. vlastné servery v dátovom centre). |
| **Kedy dáva zmysel?**            | - Firma už má infraštruktúru alebo vlastné výpočtové zdroje.<br>- Chce **plnú kontrolu nad dátami** (napr. kvôli bezpečnosti, GDPR).<br>- Potrebuje špecifickú konfiguráciu alebo integrácie. |
| **Požiadavky**                   | - Softvér musí podporovať self-hosting (nie každá SaaS aplikácia to umožňuje).<br>- V prípade PaaS/IaaS treba aj orchestráciu, monitoring, škálovanie a ďalšie DevOps nástroje. |
| **Typický software pre self-hosting** | - **OSS/FOSS** (napr. Nextcloud, GitLab CE, Mattermost, Jitsi)<br>- **Komerčný software s možnosťou self-hosting**: Atlassian Jira, Confluence, DeepL, GitLab EE. |
| **Príklad: Jira**               | - Atlassian ponúka **Jira Software Data Center** – self-hostingovú verziu Jira.<br>- Firmy môžu prevádzkovať Jiru interne bez potreby cloudovej služby Atlassian Cloud.<br>- Vhodné pre enterprise, ktoré chcú zachovať kontrolu nad projektovým manažmentom a integrovať s vlastnými systémami. |
| **Výhody**                    | - Kontrola.<br>- Prispôsobenie.<br>- Súkromie. |
| **Nevýhody**                    | - Vyššie náklady na údržbu a správu.<br>- Potreba interného know-how (napr. administrátori, bezpečnostné tímy).<br>- Zodpovednosť za zálohovanie, aktualizácie, dostupnosť. |

> Každá väčšia firma používa kombináciu rôznych poskytovateľov a self-hostingu

--- 

## ☁️ Ovládanie cloudov

Aby bolo možné efektívne pracovať s cloudovými službami, poskytovatelia cloudu ponúkajú **viacero rozhraní** pre ovládanie a správu infraštruktúry, služieb a aplikácií. Každé má svoje výhody a vhodné použitie v rôznych scenároch.

---

### 🛠️ Štyri hlavné typy rozhraní:

| Rozhranie     | Popis |
|---------------|-------|
| **CLI (Command Line Interface)** | Ovládanie cloudu pomocou príkazového riadku. Rýchle, skriptovateľné. Príklad: `az` pre Azure, `aws` pre AWS, `gcloud` pre GCP. |
| **REST API** | Programatický prístup cez HTTP požiadavky. Vhodné na integrácie s inými systémami. Každý provider má vlastnú štruktúru API. |
| **Webový portál (GUI)** | Grafické rozhranie v prehliadači. Intuitívne, vhodné pre rýchle nastavenia alebo monitoring. |
| **SDK (Software Development Kit)** | Knižnice pre rôzne programovacie jazyky (napr. Python, Java, Go), ktoré uľahčujú prácu s cloudovým API. Príklad: Boto3 pre AWS (Python). |

---

### 📚 Nevyhnutné predpoklady

| Potreba | Popis |
|--------|-------|
| **Dokumentácia** | Každé rozhranie má svoje špecifiká. Kvalitná dokumentácia je kľúčová (napr. referencie API, príklady použitia). |
| **Príklady použitia** | Príklady a návody zjednodušujú učenie a implementáciu (cookbook štýl, GitHub repozitáre, code snippets). |
| **Podpora** | Rôzne úrovne podpory: bezplatná, platená, komunitná, podniková. |

---

### 📞 Príklad podpory: **Microsoft Azure**

Azure definuje **maximálne časy odozvy** podľa úrovne podpory a závažnosti problému:

| Úroveň problému | Enterprise podpora | Štandardná podpora |
|------------------|---------------------|---------------------|
| **Závažnosť A** – kritické | 15 minút | 1 hodina |
| **Závažnosť B** – významné | 1 hodina | 4 hodiny |
| **Závažnosť C** – malé | 2 hodiny | 8 hodín (iba počas pracovnej doby) |

> ⏳ *Poznámka: Tieto časy sú reakčné, nie garancia vyriešenia problému!*

---

## 🌐 REST API

**REST (Representational State Transfer)** je architektonický štýl pre návrh webových API. REST API (nazývané aj RESTful API) sa stalo **de facto štandardom** pre modernú komunikáciu medzi aplikáciami a mikroslužbami.

### 🔧 Kľúčové vlastnosti:

| Vlastnosť | Popis |
|-----------|-------|
| **Nie je to štandard ani protokol** | REST definuje odporúčané princípy, nie presné pravidlá ako SOAP. |
| **Použitie** | Primárne na integráciu aplikácií, mikroslužieb a klient-server komunikáciu. |
| **Protokol** | Najčastejšie sa využíva nad HTTP. |
| **Metódy** | `GET`, `POST`, `PUT`, `DELETE` – zodpovedajú čítaniu, vytváraniu, úpravám a mazaniu zdrojov. |
| **Reprezentácia dát** | Môže byť ľubovoľná, ale najčastejšie sa používa **JSON** (ľahko čitateľný pre ľudí aj stroje). |

### ✅ Výhody REST API

- **Flexibilita** – voľba dátovej reprezentácie, možnosť práce s rôznymi klientmi.
- **Škálovateľnosť** – jednoduchá horizontálna distribúcia služby.
- **Efektivita** – nízka režijná záťaž (žiadne zbytočné XML ako v SOAP).
- **Jednoduchosť implementácie** – ľahko sa testuje a ladí (napr. pomocou Postman, curl).

### 🧪 Príklad REST požiadavky

```http
GET /api/users/123 HTTP/1.1
Host: example.com
Accept: application/json
```

**Odozva (200 OK):**
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```
---

### 🧩 JSON – JavaScript Object Notation
**JSON** je **ľahký dátový formát**, ktorý sa používa na výmenu dát medzi systémami (najmä medzi klientom a serverom). Je nezávislý na jazyku, ale **ľahko čitateľný pre ľudí aj stroje**.

**Výhody:**
- **Jazykovo nezávislý** – rovnaký JSON vieš vytvoriť v Pythone, JavaScripte, Go, atď.
- **Jednoducho serializovateľný** – väčšina jazykov má natívnu podporu pre konverziu objektov do JSON a späť.
- **Štandard v API komunikácii** – REST API najčastejšie vracajú odpovede práve vo formáte JSON.

---

### 📚 CLI a SDK 
| 🔧 Vlastnosť              | 💻 CLI (Command Line Interface)                                              | 📦 SDK (Software Development Kit)                                    |
|---------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| 🎯 Účel                   | Ovládanie cez príkazový riadok                                              | Integrácia priamo do aplikácie                                        |
| 🧠 Abstrakcia             | Skrýva REST API, prekladá požadované príkazy a argumenty                    | To isté – skrýva REST API                                              |
| ⚙️ Funkcionalita          | Zväčša rovnako schopné ako REST API, niekedy aj viac                        | Môže mať obmedzenia                                                    |
| 🖥️ Podpora OS             | Väčšinou dostupné pre všetky operačné systémy                              | Zvyčajne len pre vybrané jazyky (najčastejšie Python)                 |
| 🔁 Použitie               | Vhodné pre skripty, automatizáciu, opakované manipulácie                    | Ideálne pre priame použitie v kóde aplikácie                          |
| 🧩 Integrácia             | Vyžaduje spúšťanie externých skriptov alebo procesov                        | Priama integrácia do kódu                                              |
| 🛠️ Príklad použitia       | CI/CD pipeline, cron job, ručné ovládanie                                   | Backend webovej aplikácie, ktorá komunikuje s cloud službou           |

---

### 📺 Webový portál (GUI)
**Najjednoduchší formát** pre používateľa a spôsob ako sa **ozvať podpore**, pretože **vhodný na vizualizáciu výsledkov či informácií** (napr. `AI` či `dátové
služby`). Často **obmedzený** v niektorých druhoch **funkcionality**. Takže, podlieha **častejším zmenám** ako ostatné spôsoby.
