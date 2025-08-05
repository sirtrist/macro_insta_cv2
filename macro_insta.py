import pyautogui
import time

from funclib_macro import *


def main():
    """
    Fonction principale
    """
    print("Script de clic automatique")
    print("Déplacement de la souris vers le coin supérieur gauche pour arrêter le script")
    
    while True:
        try:
            print("\n=== DÉBUT D'UN NOUVEAU CYCLE ===")
         

            
            # Attendre 3 secondes avant de commencer
            print("Démarrage dans 3 secondes...")
            time.sleep(3)

            if if_image_found('images/private_account.png', 0.8, 1, True):
                print("private account trouvé")
                hash_search()
                # if if_image_found('images/suggest.png', 0.8, 1, True):
                #     print("suggest trouvé")
                #     click_at_position(1298, 744)
                #     time.sleep(3)
                #     # hash_search('#business')
                #     # click_at_position(1533, 692)
                # else:
                #     print("suggest non trouvé")
                #     hash_search()


            # following_coords = if_image_found('images/followers.png', 0.8, 1, True)
            # click_at_position(following_coords[0], following_coords[1])

            # print("Attente de 3 secondes...")
            # time.sleep(3)
            
            # # search_follow()
            # click_at_position(695, 395)


            # print("Attente de 3 secondes...")
            # time.sleep(3)

    
            message_coords = if_image_found('images/message.png', 0.8, 1, True)
            if message_coords:
                print(f"Message trouvé à {message_coords}")
                click_at_position(message_coords[0], message_coords[1])
                # time.sleep(3)
            else:
                print("Message non trouvé")
                following_coords = if_image_found('images/following.png', 0.8, 1, True)
                click_at_position(following_coords[0], following_coords[1])

                print("Attente de 3 secondes...")
                time.sleep(3)
                
                # page following
                print("=== page following ===")
                click_at_position(695, 474)


            time.sleep(3)
            
            # Écrire le message
            print("=== Écriture du message ===")
            message = get_random_message()
                        
            # Utiliser la nouvelle fonction qui préserve les sauts de ligne
            if message_coords:
                hello_coords = if_image_found('images/hello.png', 0.8, 1, True)
                if not hello_coords:
                    write_text_with_typing(message)
                    # Appuyer sur Entrée après le message
                    print("=== Appui sur Entrée ===")
                    pyautogui.press('enter')
                    print("Entrée pressée avec succès!")
                else:
                    click_at_position(665, 141)
                    time.sleep(3)
                    hash_search()
             
            # time.sleep(3)
            # page profile
            click_at_position(715, 137)
            time.sleep(1)


            following_coords = if_image_found('images/followers.png', 0.8, 1, True)
            if following_coords and not hello_coords:
                print(f"following trouvé à {following_coords}")
                click_at_position(following_coords[0], following_coords[1])
                time.sleep(3)
                # click sur le follow
                print("=== click sur le follow ===")
                click_at_position(695, 474)
                # search_follow()

            else:
                print("following non trouvé")
                click_at_position(715, 137)
                time.sleep(3)

        
 
            # Attendre 3 secondes
            print("Attente de 3 secondes...")
            time.sleep(3)

            search_coords = if_image_found('images/search.png', 0.8, 1, True)
            if search_coords:
                print(f"search trouvé à {search_coords}")
                # click_at_position(search_coords[0], search_coords[1])
            else:
                followers_coords = if_image_found('images/followers.png', 0.8, 1, True)
                click_at_position(followers_coords[0], followers_coords[1])
                time.sleep(3)
            
                # click sur le follow
                print("=== click sur le follow ===")
                click_at_position(695, 474)
                
            print("=== CYCLE TERMINÉ - REDÉMARRAGE ===")
            
        except KeyboardInterrupt:
            print("\nScript arrêté par l'utilisateur")
            break
        except Exception as e:
            print(f"Erreur dans le cycle: {e}")
            print("Redémarrage du cycle dans 5 secondes...")
            time.sleep(5)
            click_at_position(196, 69)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            write_text_with_clipboard('https://www.instagram.com/')
            pyautogui.press('enter')
            time.sleep(5)
            hash_search()

if __name__ == "__main__":
    main()
