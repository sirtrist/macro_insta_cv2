import pyautogui
import keyboard  # pip install keyboard
import time

positions = []

print("Place ta souris sur les points voulus, puis appuie sur ESPACE pour enregistrer la position.")
print("Appuie sur 'q' pour quitter et afficher les positions enregistrées.")

while True:
    try:
        if keyboard.is_pressed('space'):
            pos = pyautogui.position()
            positions.append(pos)
            print(f"Position enregistrée : {pos}")
            time.sleep(0.5)  # éviter plusieurs enregistrements accidentels

        if keyboard.is_pressed('q'):
            print("Fin de l'enregistrement.")
            break

    except:
        break

print("Positions enregistrées :", positions)

# Exemple d'écriture dans un fichier (optionnel)
with open("positions.txt", "w") as f:
    for p in positions:
        f.write(f"{p[0]},{p[1]}\n")
