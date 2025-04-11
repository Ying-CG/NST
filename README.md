# NST

INSTRUCTIONS POUR ROULER LE CODE (sur Windows):

Initialisation:

1. Installer les librairies nécessaires avec la commande suivante:
pip install torch torchvision matplotlib numpy opencv-python

2. Télécharger et installer CUDA sous le lien suivant (choisir Windows):
https://developer.nvidia.com/cuda-downloads
*Il est aussi possible de rouler l'algorithme sans CUDA. Celui-ci utilisera alors le CPU et prendra un temps beaucoup plus long.


Roulement du code:

1. Aller dans le répertoire ./pytorch-neural-style-transfer
2. Ouvrir une ligne de commande, lancer la commande suivante:
   python neural_style_transfer.py --content_img_name <content-img-name> --style_img_name <style-img-name>
   par exemple:
   python neural_style_transfer.py --content_img_name mona.jpg --style_img_name graffiti2.jpg
3. Attendre la fin de l'exécution de l'algorithme (environ 1000 itérations par défaut, environ 4 minutes). Le résultat sera dans un répertoire ./data/output-images/combined_<content-img-name>_<style-img-name> (ex: ./data/output-images/combined_mona_graffiti2).

Alternativement:

2-3. Lancer la commande suivante:
    python execute_all.py
    Cette commande exécutera l'algorithme une fois pour chaque image de contenu dans le répertoire ./data/content-images en attribuant à chacun une image de style choisie aléatoirement dans le répertoire ./data/style-images.

4. OPTIONNEL: Modifier les paramètres (alpha, beta, init_method, etc.) dans neural_style_transfer.py et relancer l'algorithme pour voir les différences.
