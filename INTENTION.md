# Note d'Intention

## I. Commencement du projet

Ce projet trouve son inspiration dans le projet que j'ai appelé
"crazyscript"
(lien [ici](https://github.com/GoswaTech/crazyscript)). Son but
était simplement de créer plusieurs background animés en
JavaScript afin de laisser ces backgrounds à disposition des
développeurs.

## II. Inspirations

J'ai beaucoup pris exemple sur les réseaux sociaux pour concevoir
ce projet. Dans l'idée, j'ai remplacé les images de l'application
instagram par la demo des scripts en action. J'ai ajouté un
button 'dislike' afin de mieux trier la qualité des posts dans la
vue d'accueil.

## III. Projet_13

### 1. Le Post

Chaque post sera, dans un premier temps, un script rattaché au
code html `<div id="background"></div>`. Il y aura donc une
seule catégorie de posts nommée **"DigitalBackground"**. Mais nous
pouvons imaginer un développement afin de proposer des squelettes
différents avec des rendus différents.

#### 1. a. Quelques idées de catégories
- DigitalAnimation
    - `<div id="text_box">Animated long text</div>`
- DigitalButton
    - `<button id="my_button">Crazy Button</button>`
- DigitalCarousel
    - `<div id="my_carousel"></carousel_images></div>`

#### 1. b. Librairie pour développeurs

Les développeurs pourront ensuite prendre les scripts gratuits
et libres de droits pour les intégrer à leur site. La
documentation étant très simple car commune à tous les posts
de chaque catégorie. Cela nécessite donc de créer une api.

---

### 2. Les Principales Fonctionnalités

#### 2. a. Côté Web

- [x] **Poster**/**Editer** Script
- [ ] **Aimer**/**Ne pas aimer** Post
- [x] **Visiter** Profile/Post
- [x] **Découvrir** Posts
- [x] **Editer** Compte

#### 2. b. Côté API

- **Importer** les librairies publiques
- **Lister** les librairies publiques
- **Rechercher** une librairie publique
