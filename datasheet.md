# Datasheet — German Credit (version Eckmühl, clean)

> **Modèle Gebru et al. (2018), version simplifiée 7 sections, 1 page max.**
> À transmettre avec le dataset Parquet livré à Eckmühl.
> Public cible : DPO + équipe métier — lisible par un non-data-scientist.

## 1. Motivation

> Pourquoi ce dataset existe-t-il ? Qui l'a créé et pour quel objectif initial ?

- ...

## 2. Composition

> Combien d'observations, quelles colonnes, quels types, distribution de la
> cible, **variables sensibles signalées explicitement**.

| Aspect | Valeur |
|---|---|
| Nombre de lignes | ... |
| Nombre de colonnes | ... |
| Cible | `credit_risk` : `good_credit` / `bad_credit` |
| Distribution cible | `good_credit` ... % / `bad_credit` ... % |
| Variables sensibles | `age`, `personal_status_sex` ⚠️ composite, `foreign_worker` |

**Schéma des colonnes** (types + modalités pour les catégorielles) :

| Colonne | Type | Modalités / range | Note |
|---|---|---|---|
| `duration_months` | int | 4 — 72 | |
| ... | ... | ... | ... |

## 3. Processus de collecte

> Connu / inconnu ? Période de collecte ? Quelles personnes sont
> représentées ? Quel biais de sélection probable ?

- ...

## 4. Préprocessing appliqué (TOI)

> Ce que tu as fait dans ton pipeline. Concis, listé.

- Imputation des manquants : ...
- Encodage des catégorielles : ...
- Normalisation des numériques : ...
- Variables exclues : ... (et pourquoi)

## 5. Usages prévus / à éviter

> Pour quoi ce dataset doit-il être utilisé (et pour quoi il ne **doit pas**
> l'être).

**Usages prévus** :
- ...

**Usages à éviter** :
- ...

## 6. Distribution

> À qui ce dataset est-il transmis ? Sous quelle forme ?

- Transmis à : ...
- Format : Parquet (compressé)
- Conditions : ...

## 7. Maintenance

> Qui maintient ce dataset ? Comment signaler un problème ? Quelle version ?

- Mainteneur·euse : ...
- Version : v1.0.0 — <date>
- Contact issue : ...

---

*Datasheet produite par <prénom>, <date>, dans le cadre du brief M2-B1 ATOS.*