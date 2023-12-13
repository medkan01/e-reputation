# E-Réputation

Projet de synthèse de Master 2 - SID à propos de l'E-Réputation des entreprises

---

Vous n’avez qu’à exécuter les commandes dans l’ordre normalement.

<aside>
💡 Il y a beaucoup de `git fetch` et de `git pull`, mais cela est très important pour éviter les conflits.
  
</aside>

<aside>
💡 Pour tous les `pull-request`, c’est Mehdi (moi) qui s’en chargera. Si vous souhaitez quand même savoir comment je fais la fusion avec un `pull-request`, je vous montrerai.
  
</aside>

<aside>
💡 Évitez au maximum de manipuler la branche `main`. Faites tout sur la branche `dev`.
  
</aside>

### Créer une nouvelle fonctionnalité

```bash
git checkout dev
git fetch
git pull
git branch nom-fonctionnalite
git checkout nom-fonctionnalite
git push -u nom-fonctionnalite
```

<aside>
💡 En faisant cela, la branche sera créée et directement mise en ligne. Vous n’aurez plus qu’à `git push` dans cette branche pour sauvegarder les modifications.
  
</aside>

### Récupérer les derniers changements de la branche `dev`

```bash
git stash
git checkout dev
git fetch
git pull
git checkout nom-fonctionnalite
git merge dev
git stash apply
```

### Commit un changement

```bash
git stash
git fetch
git pull
git stash apply
git add *
git commit -m "Message sur le changement effectué"
git push
```

### Récupéré les changements de la branche courante

<aside>
💡 Cette partie peut être utile si vous travaillez à plusieurs sur une même branche.
  
</aside>

```bash
git stash
git fetch
git pull
git stash apply
```
