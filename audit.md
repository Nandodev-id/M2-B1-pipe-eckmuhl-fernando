# Audit Banque Eckmühl — Pipeline scoring crédit conso

> Document à rendre au DPO Klaus Eichmann. **Max 2 pages.**
> Public cible : DPO non-technicien — vocabulaire métier, pas de jargon
> scikit-learn.

## 1. Verdict qualité

> 3 à 5 problèmes principaux **chiffrés** + ce que tu as fait pour les
> traiter dans le pipeline.

Exemple de format attendu :

> 1. **18 % de manquants sur `purpose`** — imputés par la modalité la plus
>    fréquente (`radio/TV`). Recommandation : remonter la cause auprès
>    de l'équipe collecte (formulaire optionnel ?).
> 2. ...

## 2. Verdict éthique

> 2 à 3 alertes principales — variables sensibles, disparate impact
> chiffré, intersectionnalités si pertinentes.

Exemple :

> 1. **`personal_status_sex` est une variable composite** (genre + statut
>    civil dans la même colonne). Anti-pattern : impossible de surveiller
>    séparément le biais par genre vs par statut. Recommandation : **split
>    en 2 colonnes** côté collecte de données.
> 2. **Disparate impact sur `foreign_worker`** : DI = 0.67 (en dessous du
>    seuil 4/5 = 0.8). Les travailleurs étrangers sont 33 % moins susceptibles
>    d'être classés `good_credit`. Recommandation : audit complet en
>    consultation avec votre DPO.
> 3. ...

## 3. Recommandations

> Liste courte d'actions concrètes pour Eckmühl (3-5 items).

- ...
- ...
- ...

## 4. Limites de cet audit

> Ce que tu n'as **pas** fait, et qu'il faudrait faire plus tard.

- Pas de mitigation des biais à ce stade (cf. modules M7-M8 du parcours).
- Pas de test de robustesse sur dataset d'évaluation séparé (déjà discuté
  avec Karim).
- ...

---

*Audit produit par <prénom>, <date>, dans le cadre du brief M2-B1 ATOS.*