import random
import time
import pyautogui
import pyperclip
import cv2
import numpy as np
from PIL import ImageGrab

def get_random_message():
    
    messages = [
        """Hello

        I have an excellent broker for international market investing - Interactive Brokers, a well-established and reliable platform.

        Interested in investing in emerging markets like India with strong demographics? Use my affiliate link for zero account minimum and start building your international portfolio today

        https://ibkr.com/referral/tristan696

        Have a great day 😊""",
                            
        """Hello

        Want to access global markets? I use Interactive Brokers - a trusted platform for international investing.

        Perfect for investing in high-growth emerging markets like India Zero minimum deposit with my affiliate link.

        https://ibkr.com/referral/tristan696

        Cheers 🚀""",
                            
        """Hello

        Looking for a reliable broker to invest internationally? Interactive Brokers is my go-to platform.

        Great opportunity to invest in emerging markets with strong demographics. No minimum deposit required with my link

        https://ibkr.com/referral/tristan696

        Best regards 💼""",
                            
        """Hello

        I found an amazing broker for global investing - Interactive Brokers. Very reliable and established.

        Interested in emerging markets like India? Start with zero minimum using my affiliate link

        https://ibkr.com/referral/tristan696

        Take care 📈""",
                            
        """Hello

        Interactive Brokers is my trusted platform for international market access. Highly recommended

        Want to invest in high-growth emerging markets? Use my affiliate link for zero account minimum.

        https://ibkr.com/referral/tristan696

        Happy investing 🎯"""
    ]
    
    return random.choice(messages)


def get_random_hashtag():
    """
    Lit le fichier de hashtags et retourne un hashtag aléatoire
    """
    try:
        with open('hastags_finance.txt', 'r', encoding='utf-8') as file:
            hashtags = [line.strip() for line in file if line.strip()]
        
        if hashtags:
            selected_hashtag = random.choice(hashtags)
            print(f"Hashtag sélectionné aléatoirement: {selected_hashtag}")
            return selected_hashtag
        else:
            print("Aucun hashtag trouvé dans le fichier, utilisation du hashtag par défaut")
            return '#webdevelopment'
    except FileNotFoundError:
        print("Fichier hastags_finance.txt non trouvé, utilisation du hashtag par défaut")
        return '#webdevelopment'
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier de hashtags: {e}")
        return '#webdevelopment'

def hash_search(hash: str = None):
    """
    Effectue une recherche de hashtag. Si aucun hashtag n'est fourni, en choisit un aléatoirement
    """
    if hash is None:
        hash = get_random_hashtag()
    
    print(f"Recherche du hashtag: {hash}")
    
    main_search_coords = if_image_found('images/main_search.png', 0.8, 1, True)
    click_at_position(main_search_coords[0], main_search_coords[1])
    time.sleep(3)
    write_text_with_clipboard(hash)
    time.sleep(3)
    click_at_position(224, 364)
    # time.sleep(3)
    # click_at_position(681, 249)
    time.sleep(3)
    click_at_position(713, 373)
    time.sleep(3)
    h_follow_coords = if_image_found('images/h_follow.png', 0.8, 1, True)
    if h_follow_coords:
        click_at_position(h_follow_coords[0]-70, h_follow_coords[1])
        time.sleep(2)
    else:
        print("h_follow non trouvé")

# Configuration de sécurité pour pyautogui
pyautogui.FAILSAFE = True  # Arrêt d'urgence en déplaçant la souris dans le coin supérieur gauche
pyautogui.PAUSE = 0.5  # Pause entre les actions

def click_at_position(x=1303, y=160):
    """
    Clique sur la position spécifiée
    """
    try:
        print(f"Clique sur la position: ({x}, {y})")
        pyautogui.click(x, y)
        print("Clic effectué avec succès!")
        return True
    except Exception as e:
        print(f"Erreur lors du clic: {e}")
        return False

def write_text_with_clipboard(text):
    """
    Écrit du texte en utilisant le presse-papiers pour éviter les problèmes de caractères
    """
    try:
        # Copier le texte dans le presse-papiers
        pyperclip.copy(text)
        # Coller le texte
        pyautogui.hotkey('ctrl', 'v')
        print("Message écrit avec succès!")
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture du message: {e}")
        return False

def write_text_with_typing(text):
    """
    Écrit du texte caractère par caractère pour préserver les sauts de ligne
    """
    try:
        # Effacer le contenu existant
        pyautogui.hotkey('ctrl', 'a')  # Sélectionner tout
        pyautogui.press('delete')      # Supprimer le contenu
        
        # Écrire le texte caractère par caractère
        pyautogui.write(text, interval=0.01)  # interval de 0.01 seconde entre chaque caractère
        print("Message écrit avec succès!")
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture du message: {e}")
        return False

def find_image_on_screen(image_path, confidence=0.8, max_attempts=3):
    """
    Trouve une image à l'écran et retourne ses coordonnées
    """
    for attempt in range(max_attempts):
        try:
            # Capturer l'écran
            screenshot = ImageGrab.grab()
            screenshot_np = np.array(screenshot)
            screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
            
            # Charger l'image à rechercher
            template = cv2.imread(image_path)
            if template is None:
                print(f"Impossible de charger l'image: {image_path}")
                return None
            
            # Rechercher l'image
            result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= confidence:
                # Calculer le centre de l'image trouvée
                h, w = template.shape[:2]
                center_x = max_loc[0] + w // 2
                center_y = max_loc[1] + h // 2
                print(f"Image trouvée à ({center_x}, {center_y}) avec confiance: {max_val:.2f}")
                return (center_x, center_y)
            else:
                print(f"Tentative {attempt + 1}: Image non trouvée (confiance: {max_val:.2f})")
                time.sleep(1)
                
        except Exception as e:
            print(f"Erreur lors de la recherche d'image (tentative {attempt + 1}): {e}")
            time.sleep(1)
    
    print(f"Image non trouvée après {max_attempts} tentatives")
    return None

def click_if_image_found(image_path, x_fallback, y_fallback, confidence=0.8, max_attempts=3):
    """
    Clique sur une image si elle est trouvée, sinon utilise les coordonnées de fallback
    """
    print(f"Recherche de l'image: {image_path}")
    coords = find_image_on_screen(image_path, confidence, max_attempts)
    
    if coords:
        print(f"Clic sur l'image trouvée: {coords}")
        return click_at_position(coords[0], coords[1])
    else:
        print(f"Image non trouvée, clic sur position de fallback: ({x_fallback}, {y_fallback})")
        return click_at_position(x_fallback, y_fallback)

def if_image_found(image_path, confidence=0.8, max_attempts=1, return_coords=False):
    """
    Vérifie si une image est présente à l'écran et renvoie True ou False
    Si return_coords=True, renvoie les coordonnées de l'image trouvée
    """
    try:
        # Capturer l'écran
        screenshot = ImageGrab.grab()
        screenshot_np = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        
        # Charger l'image à rechercher
        template = cv2.imread(image_path)
        if template is None:
            print(f"Impossible de charger l'image: {image_path}")
            return False if not return_coords else None
        
        # Rechercher l'image
        result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= confidence:
            if return_coords:
                # Calculer le centre de l'image trouvée
                h, w = template.shape[:2]
                center_x = max_loc[0] + w // 2
                center_y = max_loc[1] + h // 2
                coords = (center_x, center_y)
                print(f"Image trouvée: {image_path} à {coords} (confiance: {max_val:.2f})")
                return coords
            else:
                print(f"Image trouvée: {image_path} (confiance: {max_val:.2f})")
                return True
        else:
            print(f"Image non trouvée: {image_path} (confiance: {max_val:.2f})")
            return False if not return_coords else None
            
    except Exception as e:
        print(f"Erreur lors de la recherche d'image: {e}")
        return False if not return_coords else None
    

def search_follow():

    no_match_coords = if_image_found('images/no_match.png', 0.8, 1, True)
    if not no_match_coords: 

        only_search = if_image_found('images/only_search.png', 0.8, 1, True)

        search_coords = if_image_found('images/search.png', 0.8, 1, True)
        if search_coords:
            click_at_position(search_coords[0], search_coords[1])
            time.sleep(2)
            write_text_with_clipboard(random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))
            time.sleep(3)

            second_no_match_coords = if_image_found('images/no_match.png', 0.8, 1, True)
            if not second_no_match_coords:
                time.sleep(2)
                # click sur le follow
                print("=== click sur le follow ===")
                click_at_position(695, 395)
            else:
                hash_search()
        elif only_search:
            # click sur le follow
            print("=== click sur le follow ===")
            click_at_position(695, 474)

        else:
            followers_coords = if_image_found('images/following.png', 0.8, 1, True)
            click_at_position(followers_coords[0], followers_coords[1])
            time.sleep(3)
