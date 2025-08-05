# Détection d'Image - Guide d'utilisation

## Installation
Les packages nécessaires sont déjà installés :
- `opencv-python` : Pour la détection d'image
- `pillow` : Pour la capture d'écran
- `numpy` : Pour le traitement d'image

## Comment utiliser la détection d'image

### 1. Préparer vos images
Placez vos images de référence dans le dossier `images/` :
```
images/
├── button.png
├── link.png
├── icon.png
└── ...
```

### 2. Capturer une image de référence
Pour capturer une image à détecter :
1. Utilisez un outil de capture d'écran (Snipping Tool, etc.)
2. Capturez l'élément que vous voulez détecter (bouton, icône, etc.)
3. Sauvegardez l'image dans le dossier `images/`

### 3. Modifier le script
Remplacez les clics fixes par la détection d'image :

**Avant (clic fixe) :**
```python
click_at_position(950, 743)
```

**Après (avec détection d'image) :**
```python
click_if_image_found('images/button.png', 950, 743)
```

### 4. Paramètres de la fonction
```python
click_if_image_found(image_path, x_fallback, y_fallback, confidence=0.8, max_attempts=3)
```

- `image_path` : Chemin vers l'image à détecter
- `x_fallback, y_fallback` : Coordonnées de secours si l'image n'est pas trouvée
- `confidence` : Niveau de confiance (0.0 à 1.0, défaut: 0.8)
- `max_attempts` : Nombre de tentatives de détection (défaut: 3)

### 5. Exemples d'utilisation

**Détection d'un bouton :**
```python
click_if_image_found('images/send_button.png', 950, 743)
```

**Détection avec confiance élevée :**
```python
click_if_image_found('images/important_button.png', 687, 972, confidence=0.9)
```

**Détection avec plus de tentatives :**
```python
click_if_image_found('images/rare_element.png', 600, 129, max_attempts=5)
```

## Avantages
- ✅ Plus robuste : Le script s'adapte si l'interface change
- ✅ Fallback : Utilise les coordonnées de secours si l'image n'est pas trouvée
- ✅ Configurable : Ajustez la confiance et le nombre de tentatives
- ✅ Logs détaillés : Voir si l'image est trouvée ou non

## Conseils pour de meilleures détections
1. **Images nettes** : Utilisez des captures d'écran de bonne qualité
2. **Taille appropriée** : Pas trop grandes, pas trop petites
3. **Contraste** : Choisissez des éléments avec un bon contraste
4. **Testez** : Vérifiez que la détection fonctionne dans différentes conditions 