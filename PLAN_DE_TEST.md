# Plan de test

Ce plan de test devrait nous donner une idée des méthodes mises en places afin de tester
notre application django.

## Périmètre

Nous allons tester les principales fonctionnalités de l'applications. Vérifier que chaque template hérite bien de la template de base afin que le site soit cohérent. Nous allons aussi tester que les modèles soient bien implémentés ainsi que le système d'authentification. Nous avons donc un mélange de tests unitaires et de tests d'intégrations avec une majorité de tests d'intégrations.

## Limites

Nous ne faisons pas de tests de performance pour le moment. Nous ne faisons pas non-plus de tests de charge ni de sécurité bien que ceux-ci (les tests de sécurité) devraient être ajoutés dans la deuxième ou troisième version de l'application.

## Outils utilisés

Nous utilisons django.test (qui hérite de unittest) pour réaliser nos tests. Aucun mock n'est utilisé car nous privilégions les tests d'intégrations aux tests unitaires.

*Le package coverage est aussi utilisé dans la mesure du tux de couverture.*

## Organisation des tests

**Dans le dossier racine**
- tests
  - test_door
  - test_hall
  - test_house
  - test_library
  - test_table
  - test_virustotal

## Exécution des tests

Les tests sont écrits avant ou juste après l'écriture des fonctions.
Il en va des préférences de chaque développeur tant que le taux de couverture ne passe pas en-dessous des 80%.

De préférence, écrire la docstring de la fonction avant l'écriture des tests. Ensuite, écrire les tests puis écrire la fonction.
