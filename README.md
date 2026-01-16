# 🎮 VideoGame-Market-Intelligence

**Analyse stratégique & Business Plan pour *GameQuest Productions***  
*Projet réalisé par le cabinet fictif **Level Up Analytics***

*Durée maximum du projet : 1 journée et demi*

- 📊 **[Lien vers le fichier Power BI (.pbix)](https://drive.google.com/file/d/1Bs6fcx3ul4Tu5dbvL5CJnRT3MSnGOVOc/view?usp=sharing)**
   Dashboard interactif complet (hébergé sur Google Drive)  
---

## Présentation du projet

Ce dépôt contient une **analyse du marché mondial du jeu vidéo** basée sur des données couvrant la période **2021–2025**.

Nous n'avons pas pu exploiter toutes les KPI dans ce projet, car le projet devait être effectué en 1 journée et demi maximum.

L’objectif est d’accompagner **Édouard**, représentant d’un éditeur *Mid-Tier*, dans la **sécurisation de son prochain investissement majeur**, en s’appuyant sur des **données factuelles** plutôt que sur l’intuition.

---

## Storytelling – La Mission d’Édouard

Édouard dirige un studio ambitieux, capable d’investir, mais évoluant dans un marché **extrêmement concurrentiel** de plus de **83 000 jeux**.

Dans cet environnement :
- L’intuition ne suffit plus  
- Les échecs coûtent cher  
- La différenciation est critique  

🎯 **Son besoin :**  
> Des preuves chiffrées pour choisir **le bon genre**, **le bon prix** et **le bon calendrier de sortie**.

---

## Architecture technique

Le projet repose sur un **pipeline de données en deux étapes** :

### 1️⃣ Extraction & traitement des données
- Script Python : `extraction.py`
- Nettoyage et normalisation des données
- Gestion des types
- Optimisation de la structure pour l’analyse BI

### 2️⃣ Business Intelligence
- Modélisation des données dans **Power BI**
- Création d’indicateurs stratégiques (**KPIs**)
- Construction d’un dashboard décisionnel orienté **Business Plan**

---

## 📊 Analyse du dashboard

### 📍 Page 1 – Diagnostic du marché

![Santé du Marché Mondial](https://github.com/BYRic-F/VideoGame-Market/raw/b1aa6f5a38a1b57326d9e20c93a192e90d15f28f/images/Sant%C3%A9%20du%20march%C3%A9.png)

**Saturation du marché**
- Les **10 plus grands éditeurs** captent près de **50 % de la valeur totale**

**Guerre des prix**
- Prix moyen constaté : **6,53 $**
- Forte pression sur la rentabilité pour les studios de taille intermédiaire
- Nécessité d’une stratégie **volume** ou **premium de niche**

---

### 📍 Page 2 – Leviers de performance

![Leviers de Rentabilité](https://github.com/BYRic-F/VideoGame-Market/raw/b1aa6f5a38a1b57326d9e20c93a192e90d15f28f/images/Leviers%20de%20rentabilit%C3%A9.png)

**Qualité & Satisfaction**
- Seuils critiques de succès identifiés :
  - 🎯 **Metacritic ≥ 79 / 100**
  - 👍 **Avis positifs ≥ 82 %**

**Saisonnalité**
- Pics de revenus observés :
  - 📈 **Mars**
  - 📈 **Septembre**
- Ces périodes orientent le **calendrier de lancement recommandé**

---

### 📍 Page 3 – Business Plan (Recommandation)

![Business Plan - Choix Stratégique](https://github.com/BYRic-F/VideoGame-Market/raw/37eec831cbd4dfcd32e536d4438d92f1b4f2e202/images/Choix%20strat%C3%A9gique.png)

🔎 **Recommandation stratégique du cabinet Level Up Analytics**

**Genre recommandé**
- 🎮 **MMORPG (Massively Multiplayer Online RPG)**

**Positionnement**
- 💰 **Prix cible : 50 €**
- Positionnement **Premium**

**Modèle de revenus**
- Stratégie basée sur la **rétention et la persistance**
- Moyenne observée : **Entre 2 et 3 DLC par titre**
- Objectif : maximisation de la **LTV (Lifetime Value)**

**Indice de Risque**
- ⚠️ Score : **24,5**
- Complexité technique élevée
- Risque compensé par :
  - 🌍 Localisation multilingue (5+ langues)
  - Marché international adressable

---

## 📁 Contenu du dépôt

- `extraction.py`  
  Script Python de préparation et transformation des données

- `/images/`  
  Captures d’écran du dashboard :
  - Santé du marché
  - Leviers de performance
  - Business Plan

- 📊 **[Lien vers le fichier Power BI (.pbix)](https://drive.google.com/file/d/1Bs6fcx3ul4Tu5dbvL5CJnRT3MSnGOVOc/view?usp=sharing)**
  Dashboard interactif complet (hébergé sur Google Drive)  
  > ⚠️ Taille du fichier > 25 Mo  
  > Identité visuelle personnalisée & mesures DAX avancées

---

## Comment utiliser ce projet

1. 📂 Consulter le dossier `/images/` pour une lecture rapide des conclusions  
2. 🐍 Lancer `extraction.py` pour comprendre la logique de préparation des données  
3. 📈 Ouvrir le lien Google Drive pour explorer :
   - Le dashboard interactif
   - Les KPIs
   - Les mesures DAX
   - Les filtres avancés

---

## Objectif final

Permettre à un éditeur **Mid-Tier** de :
- Réduire le risque d’investissement
- Choisir un positionnement rentable
- Appuyer ses décisions sur des **données concrètes**

---

