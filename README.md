
<br />
<div align="center">
  <a href="https://github.com/Paulchrr/project-paulcharrier">
    <img src="https://studl.com/assets/uploads/logo_ecoles/420/photo58d909424ebfa1.57301377.png" alt="Logo" width="150" height="150">
  </a>

 
  
  <h3 align="center">Auto Playbook</h3>

  <p align="center">
    Un playbook d'automatisation RED TEAM
    <br />

  </p>
</div>





# Auto Playbook

![App Screenshot](https://user-images.githubusercontent.com/100359031/227722134-cdb78a34-8be4-45b3-b5f2-df3671d0249f.png)

Auto Playbook est un script qui à pour but d'automatiser un maximum de tâches dans un contexte orienté Red Team.

L'outils comporte trois modules ;
- Auto
- Osint - Reconnaissance passive
- Obtenir les dernières CVE

Nous allons revenir plus en détails sur chacun des modules pour expliquer plus en détails les actions qui seront réalisés dans chacun d'entre eux.

### Mode Auto

Le mode Auto est destiné à un usage plutôt offensif.
Il est composé de plusieurs fonctions telles que :

- WhoIS
- NMAP
- Un WordPress scanner qui va vérifier sur le nom de domaine cible utilise WordPress, et si va lancer un scan avancés afin de lister les utilisateurs, les plugins, la page du panel d'administration ect ...

### Mode OSINT

Le mode OSINT à pour volonté de recupérer un maximum d'information sur un un domaine tout en restant au maximum dans une reconaissance passive.
Ce module utilise plusieurs fonctions codés par mes soins qui sont :
- Whois
- Un chercheur de sous domaines. Le scanner de sous-domaines fonctionne à l'aide d'une API https://Securitytrails.com
- Un scrapper de mail via search engine tels que Google, Bing, et Baidu
- Un module qui va vérifier sur le nom de domaine cible utilise WordPress, et si oui peut lancer un scan avancés afin de lister les utilisateurs, les plugins, la page du panel d'administration ect ...
- Un module de DORKS qui va passer par le moteur de recherche DuckDuckGo pour vérifier la présence de fichier intéressants appartenant au site ciblé



### Mode CVE

Le mode CVE affichera en console les 30 dernières CVE.
Ces CVE sont scrapper(récuperer) grâce à l'API https://cve.circl.lu/api/last/.

Le résultat de cette API est traité afin de récuperer les infos importants tels que l'ID et la date de publication de la CVE

![App Screenshot](https://user-images.githubusercontent.com/100359031/227724013-f67377ef-24bd-47a4-9d7a-1c8ef2e73a6c.png)
## Installation

Pour déployer "Auto Playbook"

```bash
# Télécharger le git
$ git clone https://github.com/Paulchrr/project-paulcharrier

# Accéder au répertoire
$ cd project-paulcharrier

# Rendre éxecutable l'installer
$ chmod +x installer.sh

# Executer le script d'installation
$ ./installer.sh
```

## Utilisation

Pour utiliser "Auto Playbook"

```bash
$ ./main.py
```

Les résultats de l'outils seront stockés dans le repertoire "/result" qui sera créé avec un fichier texte qui sera conformément nommé "nom_de_domaine.txt"
## Fichier utilisés

| Fichier           | Description                                                              |
| ----------------- | ------------------------------------------------------------------ |
| main.py | Script qui initialise l'outils |
| functions.py| Script qui stock toutes les fonctions utilisées par l'outils|
| installer.sh| Script bash qui installe les pré-recquis pour le bon fonctionnement de l'application |
| README.MD | Fichier à but informatif sur l'utilisation et les usages de l'outils |
| /result | Dossier qui contient les résultats des analyses |



## Auteur

- Paul Charrier - [@paulchrr](https://www.github.com/paulchrr)


