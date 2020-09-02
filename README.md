# Digital Art
*Développez votre créativité digitale avec Digital Art !*

## Note d'Intention
*click here : https://github.com/GoswaTech/projet_13/blob/master/openclassrooms/INTENTION.md*

## Short History of Packages' Names

We are in a giant high-tech tree and only JavaScript exists. To live, you need to code
beautiful backgrounds. You are in a tree, don't forget it.

To understand packages names, follow this instructions :

- You enter by the **door**, who give you all *static files* to decode the
environment
- You can open you house's door in the *login* view or create you own in the
*register* view. So, after a *settings* review, you can go in your **house**
to see your *living room* (public area), your *likes*, your *posts* or
your *dashboard*.
- Leave your house and go in the **hall** to *discover* the others tables
(posts).
- The **table** is like a painting as if devs are painting their *posts*. These
tables are digital so they decides how to *render*, how to trigger a *like*
or a *comment*.
- You can also go in the **library** to learn how to use the website with
*documentations* and *examples*.

## Django Apps Universe

- [door](https://github.com/GoswaTech/projet_13/blob/master/door/README.md)
This package is the 'auth' part of the tree. We can find :
  - User Model
  - Register View
  - Auth URLs (login, logout, register)
  - User Settings
- [hall](https://github.com/GoswaTech/projet_13/blob/master/hall/README.md)
This package is the exposition room of the tree. We can find :
  - Website's Index
  - Discover view
  - Posts Tools (useful backend functions)
- [house](https://github.com/GoswaTech/projet_13/blob/master/house/README.md)
This package is the core of the social part. You can find :
  - The Users' Dashboard
  - The Users' Likes
  - The Users' Posts
  - The Users' Living Room
- [table](https://github.com/GoswaTech/projet_13/blob/master/table/README.md)
This package contain the tables of Digital Art. You can find :
  - The TablePost Model
  - The TableLike Model
  - The TableComment Model
- [library](https://github.com/GoswaTech/projet_13/blob/master/library/README.md)
This package is the learning room of the tree. You can find :
  - Documentation with examples
  - Legacy Mentions

### Door

The door is where we enter in the house. It's in this app where we can
find the auth part of the project.

Functionnalities :
- **view** User authentification
- **view** User settings *(auth required)*
- **model** Create New User

**Static Files are written in this app.**

### Hall

The hall is the public part of our project. It is a commune space with
all users.

Functionnalities :
- **view** Website Index
- **view** Discover Posts

### House

The house is specific to the user experience. We can find scripts,
likes, profile. Their are a living room in the house to expose
tables to the public.

Functionnalities :
- **view** Dashboard *(auth required)*
- **view** Likes List *(auth required)*
- **view** Owned Posts List *(auth required)*
- **view** Account's Public Page *(auth required)*

### Library

It's at this app we will develop the documentation's part of
the project.

Functionnalities :
- **view** Documentation Page

### Table

It's a table where painters draws in the metaphoric way. This app
manage all posts, likes or comments created by users.

Functionnalities :
- **view** Create and Edit Post *(auth required)*
- **view** View Post
- **model** Like / Dislike Post *(auth reqiured)*

## TeamWork

### Dev
- Space [*(contact me)*](mailto:arthur.neyer@muggum.fr)
    - Checklists
    - Mirror
- GitHub [*(repo)*](https://github.com/GoswaTech/projet_13/)
    - Issues
    - Pull Requests
    - Merge Requests
    - Discuss

### Maintainer
- Sentry [*(contact me)*](mailto:arthur.neyer@muggum.fr)
    - Errors

### Analytics
*no analytics*

### SysAdmin
- DigitalOcean [*(contact me)*](mailto:arthur.neyer@muggum.fr)
    - Server [*(contact me)*](mailto:arthur.neyer@muggum.fr)

## Liens externes
- Trello : https://trello.com/b/2nEbNZqw/projet-13
- Space : https://muggum.jetbrains.space/p/projet-13

## Repositories
- GitHub : https://github.com/GoswaTech/projet_13/
- Space : https://git.jetbrains.space/muggum/projet-13/projet_13.git
