# Suivi

## Résolution des failles XSS

Le problème principale vient des failles XSS. L'idée pour les boucher serait
d'interdire les mots comme 'document', 'getElementById' ou 'getParent' et de proposer une
classe appelée 'DigitalTable' (par exemple) qui proposerait des fonctions
de remplacement afin d'éviter aux utilisateurs de sortir de leur <div>.
J'ai donc supprimé virustotal car il ne servira plus à grand-chose.

## Tests

J'ai changé l'emplacement des tests pour les mettre dans la racine.
