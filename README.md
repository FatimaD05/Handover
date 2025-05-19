# 🦾 Handover – Contrôle Gestuel 3D en Temps Réel avec Python, MediaPipe & Blender

> Comme Iron Man... mais sur budget étudiant.  
> Ce projet permet de contrôler un **bras robotique 3D dans Blender** avec les mouvements de la main, détectés par webcam — sans manette, sans capteurs physiques.

---

## 🎥 Démonstration Vidéo

▶️ [Regarder la démo sur YouTube](https://youtu.be/NQjh0z16frE)

---

## 🧠 Technologies utilisées

- **Python** – traitement en temps réel
- **MediaPipe** – détection de la main (21 points clés)
- **OpenCV** – gestion de la webcam
- **Blender** – application des mouvements à l’objet 3D

---

## 📁 Structure du projet

```bash
Handover/
├── main.py                # Capture et interprétation des gestes
├── HandTrackingModule.py # Détection de la main avec MediaPipe
├── scripting_blender.py  # À exécuter dans Blender pour animer l'objet
├── scale.txt              # Données de zoom
├── rotate.txt             # Données de rotation
├── pan.txt                # Données de translation
└── README.md              # Ce fichier ✨
```

---

## 🚀 Lancer le projet

### 1. Installer les dépendances

```bash
pip install mediapipe opencv-python
```

### 2. Lancer le script Python

```bash
python main.py
```

### 3. Dans Blender :

- Supprimer la caméra et la lumière
- Ajouter un objet (Cube, bras robotique…)
- Aller dans l’onglet **Scripting**
- Copier-coller le contenu de `scripting_blender.py`
- Cliquer sur ▶️ **Run Script**

---

## 🔧 Personnalisation

- Remplace `"Robotic Arm"` dans `scripting_blender.py` par le **nom exact** de ton objet dans Blender
- Les fichiers `.txt` servent d'échange entre Python et Blender (communication en temps réel)
- Tu peux modifier la vitesse, la sensibilité et les limites de mouvement

---

## 👩‍💻 À propos

Projet réalisé par **Fatoumata Diallo**  
Exploration de :
- L’intelligence artificielle appliquée
- L’interaction gestuelle
- L’intégration multi-outils (Python ↔ Blender)

---

## 🧾 Licence

[MIT License](LICENSE)

---

## ⭐ Tu as aimé ?

- Mets une ⭐️ au repo
- Partage-le avec d'autres curieux
- Reprends-le pour ton propre projet !
