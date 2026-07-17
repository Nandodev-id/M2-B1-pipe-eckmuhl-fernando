# Audit Banque Eckmühl — Pipeline de scoring crédit conso

## 1. Verdict qualité

Le dataset principal contient **1 000 dossiers**, **20 variables explicatives** et une cible binaire. Le complément ajoute une variable, `customer_segment`, portant le total à **21 variables d'entrée**.

1. **Modalités métier ambiguës** — `savings_account` contient **183 dossiers (18,3 %)** classés `unknown / no savings`, et `property` contient **154 dossiers (15,4 %)** classés `unknown / no property`. Ces catégories mélangent une donnée inconnue et une absence réelle d'épargne ou de patrimoine. Elles sont conservées comme modalités distinctes dans le pipeline, sans leur attribuer un ordre artificiel.
   **Recommandation :** séparer à la collecte les valeurs « inconnue » et « aucune ».

2. **37 valeurs manquantes sur `customer_segment`** — soit **3,7 %** des dossiers. Elles sont remplacées par la modalité la plus fréquente afin que tous les dossiers puissent être transformés.
   **Recommandation :** rendre ce champ obligatoire ou tracer explicitement la cause de son absence.

3. **Variable composite `personal_status_sex`** — **310 dossiers** appartiennent à une catégorie féminine unique, tandis que **690 dossiers** sont répartis entre plusieurs catégories masculines. Cette structure asymétrique mélange sexe et situation matrimoniale. La variable est conservée comme catégorie non ordonnée afin de ne pas créer de hiérarchie artificielle.
   **Recommandation :** la remplacer par deux colonnes indépendantes.

4. **Forte sous-représentation d'un groupe** — `foreign_worker = no` ne représente que **37 dossiers (3,7 %)**, contre **963 dossiers (96,3 %)** pour `yes`. Cette faible taille rend les comparaisons statistiques plus instables.
   **Recommandation :** contrôler les résultats sur un échantillon plus large et plus représentatif.

Le pipeline final transforme les **21 variables d'entrée en 58 variables préparées**, conserve les **1 000 lignes**, ne laisse aucun `NaN` et produit un résultat déterministe.

## 2. Verdict éthique

1. **`personal_status_sex` est une variable composite** — elle combine sexe et situation matrimoniale et ne permet pas de surveiller correctement ces deux dimensions séparément. La représentation des femmes et des hommes est également asymétrique.
   **Alerte :** cette variable doit être revue avant tout déploiement.

2. **Disparate impact sur `foreign_worker`** — le taux de résultat `good_credit` est de **69,26 %** pour `foreign_worker = yes`, contre **89,19 %** pour le groupe de référence `no`. Le disparate impact est de **0,7766**. Il est inférieur au seuil de **0,8** fixé par la règle des quatre cinquièmes et constitue donc un signal d'alerte.
   Cette conclusion doit rester prudente, car le groupe de référence ne contient que **37 dossiers**.

3. **Écart selon le sexe dérivé** — le taux de résultat positif est de **64,84 %** pour les femmes et de **72,32 %** pour les hommes. Le disparate impact est de **0,8966**. Il reste entre **0,8 et 1,25** et ne déclenche donc pas d'alerte forte selon la règle des quatre cinquièmes. Un écart demeure néanmoins observable. Cette analyse est limitée par la mauvaise structure de la variable d'origine.

La nouvelle variable `customer_segment` suit l'ordre `basic < plus < premium < private`. Elle peut être corrélée au revenu, au patrimoine ou à la rentabilité du client et agir comme indicateur indirect du niveau socioéconomique.

Ces résultats signalent des écarts statistiques. Ils ne prouvent pas à eux seuls une discrimination intentionnelle.

## 3. Recommandations

* Séparer `personal_status_sex` en deux variables : sexe et situation matrimoniale.
* Séparer les modalités « inconnue » des situations réelles d'absence d'épargne ou de patrimoine.
* Réexaminer la pertinence de `customer_segment` dans une décision de crédit.
* Surveiller le disparate impact de `foreign_worker` sur davantage de données.
* Rejouer le test de conformité du pipeline avant chaque livraison ou modification.

## 4. Limites de cet audit

* Aucune mitigation des biais n'a été appliquée : l'objectif était uniquement de détecter, mesurer et documenter les écarts.
* Aucun modèle de scoring n'a été entraîné dans ce brief.
* Aucun test de performance n'a été réalisé sur un dataset d'évaluation séparé.
* Aucune analyse intersectionnelle complète n'a été conduite.
* Le disparate impact sur `foreign_worker` est sensible à la faible taille du groupe `no`.

---

*Audit produit par Fernando, le 17 juillet 2026, dans le cadre du brief M2-B1 FastIA.*
