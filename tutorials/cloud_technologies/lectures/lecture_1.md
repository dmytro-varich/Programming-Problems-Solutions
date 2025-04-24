# 📕 Lecture 1

⚫️ **Cloud computing** — je model poskytovania IT zdrojov (výpočtového výkonu, úložísk, databáz, sietí, softvéru, analytických služieb a služieb umelej inteligencie) na požiadanie cez internet s platbou podľa potreby. Namiesto kapitálových investícií do nákupu, vlastníctva a údržby vlastných dátových centier získate pružnú, škálovateľnú a spravovanú platformu od poskytovateľa ([AWS](https://aws.amazon.com/), [Azure](https://portal.azure.com/), [Google Cloud](https://cloud.google.com/), atď.), ktorá vám umožní rýchlejšie inovovať, flexibilne rozširovať alebo znižovať zdroje a optimalizovať náklady.

⚫️ **Cloud computing** — is a model for delivering IT resources (computing power, storage, databases, networking, software, analytics, and AI services) on demand over the Internet with pay-as-you-go pricing. Instead of capital investments in buying, owning, and maintaining your own data centers, you get an elastic, scalable, and managed platform from a provider ([AWS](https://aws.amazon.com/), [Azure](https://portal.azure.com/), [Google Cloud](https://cloud.google.com/), etc.), which allows you to innovate faster, flexibly expand or reduce resources and optimize costs.

⚫️ **Хмарні обчислення** — це модель надання IT-ресурсів (обчислювальної потужності, сховищ, баз даних, мережевих можливостей, програмного забезпечення, аналітики та сервісів ШІ) на вимогу через Інтернет з оплатою "за фактом" використання. Замість капітальних вкладень у купівлю, володіння та обслуговування власних дат-центрів ви отримуєте платформу від провайдера ([AWS](https://aws.amazon.com/), [Azure](https://portal.azure.com/), [Google Cloud](https://cloud.google.com/), тощо.), що дає змогу швидше впроваджувати інновації, гнучко нарощувати або скорочувати ресурси та оптимізувати витрати.

## ☁️ 5 charakteristík cloudu:

1. **On-demand self-service**.
2. **Broad network access**.
3. **Resource pooling**.
4. **Rapid elasticity**.
5. **Measured service**.

### 1️⃣ **On-demand self-service**
- Zákazníci získavajú prístup k ďalším zdrojom na požiadanie.
- Prístup k zdrojom by mal byť okamžitý, resp. **veľmi rýchly**.
- Zákazník sa rozhoduje koľko zdrojov potrebuje.
- **Príklad**: Na portáli providera cloudu si vypýtam ďalšiu virtuálnu mašinu, ktorú aktuálne potrebujem, a tá je mi okamžite pridelená. Po ukončení výpočtov mašinu odstránim.

### 2️⃣ **Broad network access**
- Zdroje sú dostupné po sieti.
- Zdroje sú prístupné pomocou štandardných mechanizmov-protokolov (HTTP(S), TCP/IP) a je možné ich používať z rôznych platforiem (Windows, iOS, Android, atď.).
- **Príklad**: Máte server API v cloude (napr. AWS) na adrese `api.myapp.com`. Používateľ z akéhokoľvek zariadenia — smartfónu so systémom iOS alebo Android, notebooku — prostredníctvom štandardnej požiadavky HTTPS okamžite získa prístup na túto adresu bez ďalších nastavení VPN alebo presmerovania portov.

### 3️⃣ **Resource pooling**
- Poskytovateľ cloudových služieb má **pool** (množinu) zdrojov, ktoré dynamicky poskytuje rôznym zákazníkom podľa potreby.
- Na lokalite týchto zdrojov nezáleží a zákazník často ich presnú polohu nepozná.

| ![image](https://github.com/user-attachments/assets/d0f256b7-34fb-48ea-b41e-263dd67b27c8) | ![image](https://github.com/user-attachments/assets/b306c192-6d82-4388-9796-8a315dcab565) |
|:------------------------------------------:|:------------------------------------------:|
| **Data Center (Outside)**                   | **Data Center (Inside)**                   |

### 4️⃣ **Rapid elasticity**
- Schopnosť pridávať alebo odoberať zdroje (škálovať), keď to je potrebné, niekedy automaticky.
- Zákazníkovi sa zdá, že zdroje sú **nekonečné** a môže si vypýtať ľubovoľné množstvo v ľubovoľný čas.
- **Elasticita** == škálovateľnosť.
  - **Vertikálna škálovateľnosť** (scaling up/down): Pridanie alebo zníženie kapacity jednej inštancie (zvýšenie CPU, pamäte, miesta na disku vo virtuálnom počítači alebo kontajneri).
  - **Horizontálna škálovateľnosť** (scaling out/in): Dynamicky pridávajte nové inštancie (virtuálne stroje, kontajnery alebo mikroslužby) podľa rastúceho zaťaženia a automaticky ich odstraňujte, keď už nie sú potrebné.

### 5️⃣ **Measured service**
- Používanie cloudových zdrojov je **sledované**/monitorované.
- Zdroje sú **ovládané** a optimalizované.
- **Pay as you go** == platíme za to, čo použijeme.

| ![image](https://github.com/user-attachments/assets/59f5cb9a-4945-4340-a2cd-806cefadef2d) | 
|:------------------------------------------:|
| **Cloud Monitoring Tools**                      |

## 🧬 Evolution of cloud computing
1. **1963 - DARPA Challenge**: Počítač musia používať dvaja alebo viacerí ľudia súčasne.
2. **1990 - Utility Computing**: Model poskytovania služieb, v ktorom poskytovateľ ponúka zákazníkom výpočtové zdroje a spravuje infraštruktúru. Zákazníci platia len za skutočne spotrebované zdroje (žiadne fixné predplatné).
3. **2000 - Grid Computing**: Distribuovaný systém výpočtových zdrojov spojených na vykonávanie spoločnej úlohy (vedecké výpočty, vykresľovanie, analýza veľkého množstva údajov).
4. **2006 - Vznik pojmu 'Cloud Computing'**: Amazon Web Services uvádza na trh služby EC2 a S3, čím stanovuje moderný štandard cloudu so zdrojmi na požiadanie a platbou za používanie.
5. **2010 - Vznik PaaS a bezserverového vývoja**: Off-the-shelf platformy (Google App Engine, Azure App Service) a feature-a-as-service (AWS Lambda), ktoré zjednodušujú vývoj a nasadenie bez starostí o servery.
6. **2020 - Mikroslužby a multi-cloud**: Rozšírené zavádzanie architektúry mikroslužieb a stratégií multi-cloudu s cieľom zlepšiť odolnosť a flexibilitu.

## 🗄 **Modely cloudových služieb**

| ![image](https://github.com/user-attachments/assets/fb9b53cd-5ba9-4465-b98e-bf59f6c1ae97) | 
|:------------------------------------------:|
| Types of cloud models                      | 

1. **Software as a Service (SaaS)**  
   **SaaS** poskytuje aplikácie priamo ako službu. Používateľ priamo používa aplikáciu, ktorú poskytovateľ spravuje v cloude, a nemusí sa starať o infraštruktúru, servery ani ukladanie dát. Aplikácie sú prístupné cez webový prehliadač alebo API.  
   **Príklady:** Office 365, Gmail, Google Docs, OneDrive.

2. **Platform as a Service (PaaS)**  
   **PaaS** poskytuje platformu na vývoj a nasadenie aplikácií. Používateľ nahráva vlastné aplikácie na cloudovú platformu, pričom poskytovateľ spravuje infraštruktúru a sieť. Používateľ má plnú kontrolu nad aplikáciou, konfiguráciou a dátami.  
   **Príklady:** Google App Engine, Microsoft Azure App Services, Heroku.

3. **Infrastructure as a Service (IaaS)**  
   **IaaS** poskytuje virtuálne stroje a ďalšie infraštruktúrne zdroje, ktoré si používateľ môže prispôsobiť podľa vlastných potrieb. Používateľ má kontrolu nad operačným systémom, aplikáciami a sieťovými nastaveniami, zatiaľ čo fyzická infraštruktúra je spravovaná poskytovateľom.  
   **Príklady:** Google Compute Engine, Microsoft Azure Virtual Machines, AWS EC2.

4. **Anything as a Service (XaaS)**  
   **XaaS** je širší koncept, ktorý pokrýva rôzne IT služby poskytované cez internet. Ide o rozšírenie modelov SaaS, PaaS a IaaS, kde je každý aspekt IT infraštruktúry, riešení alebo služieb poskytovaný ako služba na požiadanie. Tento model umožňuje prístup k rôznym technológiam a funkciám bez nutnosti vlastniť alebo spravovať infraštruktúru.  
   **Príklady:** AI-as-a-Service, Database-as-a-Service, Security-as-a-Service.

## 🌥 **Cloud Deployment Models**
1. **Private Cloud**  
   Používaný iba jednou organizáciou. Môže byť vlastnený a spravovaný samotnou organizáciou alebo tretími stranami.

2. **Community Cloud**  
   Určený pre komunitu organizácií, ktoré majú spoločné záujmy. Môže ho spravovať komunita, tretia strana alebo kombinácia oboch.

3. **Public Cloud**  
   Prístupný širokej verejnosti. Správu zabezpečujú rôzne organizácie, ako napríklad firmy, univerzity alebo vláda.

4. **Hybrid Cloud**  
   Kombinácia dvoch alebo viacerých rôznych cloudových infraštruktúr, ktoré sú prepojené proprietárnou alebo štandardnou technológiou, umožňujúcou prenos dát a aplikácií medzi nimi.

---

## 💼 **Výhody Cloudu pre Firmy**
- **Nižšie náklady na infraštruktúru**
- **Zvýšená bezpečnosť**
- **Škálovateľnosť** podľa potrieb
- **Univerzálny prístup** k dátam a aplikáciám
- **Ochrana pred stratou dát**
- **Automatické aktualizácie** a správa

---

## 🖥 **Virtualizácia**
Virtualizácia je proces vytvárania virtuálnych (abstraktných) verzií fyzických IT zdrojov ako sú servery, úložiská, siete alebo operačné systémy pomocou softvérovej vrstvy (hypervisoru alebo kontajnerizačnej platformy).  
Umožňuje efektívnejšie využívať fyzický hardvér, spúšťať viac virtuálnych strojov alebo kontajnerov na jednom zariadení, a poskytuje flexibilitu pri škálovaní a migrácii pracovného zaťaženia.

### **Charakteristiky Virtualizácie:**
- Delenie zdrojov jedného stroja medzi viacerých užívateľov.
- Poskytovanie požadovanej úrovne abstrakcie užívateľom.
- Umožňuje prevádzku požadovaných aplikácií na rôznom hardvéri.
- Virtuálny stroj je virtuálnou reprezentáciou fyzického počítača, s vlastným operačným systémom a zdrojmi.

---

## 🖥 **Hypervisor**
Hypervisor (alebo Virtual Machine Monitor - VMM) je softvérová vrstva, ktorá spravuje virtuálne stroje a prideľuje im hardvérové zdroje. Existujú dva typy hypervisorov:

- **Bare-metal Hypervisor**  
   Beží priamo na hardvéri, čo prináša vyšší výkon a bezpečnosť.  
   **Príklad:** Microsoft Hyper-V.

- **Hosted Hypervisor**  
   Funguje na úrovni hostiteľského operačného systému, čo umožňuje jednoduchšiu inštaláciu a správu.  
   **Príklad:** Oracle VirtualBox.

| ![image](https://github.com/user-attachments/assets/75de45ea-c410-4402-a308-10c39bdb597d) | 
|:------------------------------------------:|
| **Types of Hypervisor**                    |

---

## 🔧 **Druhy Virtualizácie**
1. **Full/Native Virtualizácia**  
   Simuluje všetok potrebný hardvér na beh operačného systému bez úprav. Hostovaný OS vidí skutočný hardvér, ale výkonom je to náročnejšie kvôli emulácii.  
   **Príklady:** Oracle VM VirtualBox, VMware Workstation.

2. **Para-virtualizácia**  
   Zlepšuje výkon tým, že zakáže emuláciu hardvéru a upraví hostiteľské jadro OS. Hostovaný systém je „uvedomelý“ o virtualizácii a komunikuje s hypervisorom cez špeciálne API.  
   **Príklad:** VMware VMI.

3. **Hardware Assisted Virtualization**  
   Využíva vstavané funkcie CPU pre virtualizáciu, čo zabezpečuje takmer natívny výkon bez potreby emulácie.  
   **Príklady:** AMD‑V, Intel VT‑x.

4. **OS-level Virtualization**  
   Beží niekoľko izolovaných kontajnerov na jednom spoločnom jadre operačného systému bez simulácie hardvéru. Každý kontajner zdieľa rovnaký kernel, čo minimalizuje výkonové straty.  
   **Príklady:** Docker, Solaris Zones.

| ![image](https://github.com/user-attachments/assets/c28b1a96-7b0d-4725-b378-6a1517ab59fe) | 
|:------------------------------------------:|
| **Types of Virtualization**                    |
