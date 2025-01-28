# Monitor-PI

Ce projet est une interface web en temps réel permettant de surveiller les statistiques système (température, utilisation CPU/GPU, RAM, réseau) et d'analyser les paquets réseau.

## Fonctionnalités

- Suivi des températures du CPU et du GPU.
- Surveillance de l'utilisation des ressources système : CPU, GPU, RAM.
- Affichage des débits réseau (upload/download).
- Analyse des paquets réseau capturés.
- Interface utilisateur dynamique basée sur **Chart.js** pour des graphiques en temps réel.

## Technologies utilisées

- **Backend** : Python (Flask, psutil, subprocess).
- **Frontend** : HTML, CSS, JavaScript (Chart.js).
- **Outils système** : `tshark` pour la capture de paquets réseau.

---

## Installation

### Prérequis

- Python 3
- Les bibliothèques Python : Flask, psutil
- Chart.js (inclus via un CDN)
- `tshark` (Wireshark) installé pour la capture réseau
- Accès root ou sudo pour capturer des statistiques système avancées

### Étapes d'installation

1. Clonez le dépôt :
   ```bash
   git clone <url-du-repo>
   cd Monitor-PI

### /!\ Les captures réseaux ne sont pas au points et peuvent DDOS votre box internet.... /!\
- WORK-IN-PROGRESS
