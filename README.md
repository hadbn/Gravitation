# Gravitation
TP gravitation

Noms du binome : Théophane Prevost, Clément jauffret

Commentaires en plus : 
Lisibilité :
Il aurait sans doute était plus clair, d'utiliser un tableau des vitesses plutôt qu'un tableau du temps passé même si cela est équivalent.

Pertinence : 
Lors du lancement on remarque que pour des trops grands pas de temps, il y a divergence parfois du schéma .
Cela doit probablement être dû au fait que les schémas explicites (comme Euler) sont généralement plus instable que des méthodes implicites.
Les schémas implicites eux, sont plus lourds en mémoires et en complexité notamment de par le fait qu'il faut résoudre une équation à chaque pas de temps.
Enfin, on remarque qu'il y a divergence des planètes lorsqu'elles se rapprochent, cela est du au fait que l'on divise par les distances entre celles-ci qui se rapprochent ainsi de 0. 
Un modèle évitant cela serait de donner une valeur minimale au distance (cela parait incohérent mais permettrai de s'affranchir de la problématique précédente)