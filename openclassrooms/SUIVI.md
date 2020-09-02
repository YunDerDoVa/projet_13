# Suivi

## Retour de la soutenance

J'ai bien réglé la majorité des erreurs retourné par l'évaluateur, il ne me
reste plus qu'à boucher les failles XSS avant de terminer d'écrire les tests
et faire le ménage dans les packages comme 'digitaltesttools'
(qui doit être dans le répertoire des tests) et color_tool (qui doit être soit
intégré au site dans la librairie, soit supprimé ou soit devenir autre-chose).

## Résolution des failles XSS

Le problème principale vient des failles XSS. L'idée pour les boucher serait
d'interdire les mots comme 'document', 'getElementById' ou 'getParent' et de proposer une
classe appelée 'DigitalTable' (par exemple) qui proposerait des fonctions
de remplacement afin d'éviter aux utilisateurs de sortir de leur div.
J'ai donc supprimé virustotal car il ne servira plus à grand-chose.

## Tests

J'ai changé l'emplacement des tests pour les mettre dans la racine.

## Compréhension des packages

Le README devrait servir à mieux appréhender l'architecture et surtout le
nomage de chaque package.
