import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mes_infos_mail(file: str = "input/TOUCHE_PAS_CA_mail.txt") -> tuple[str]:
    with open(file, 'r') as f:
        infos = f.readlines()
    
    #      smtp         , email        , mdp
    return infos[0][:-1], infos[1][:-1], infos[2][:-1]


def Init_destinataires(file: str = "input/destinataires.txt") -> list[str]:
    with open(file, 'r') as f:
        destinataires = f.writelines()
    
    return [m[:-1] for m in destinataires]
    


def envoie_mail_par_univ_angers(smtp: str, expediteur: str, mdp: str, destinataires: list[str], sujet: str, msg: str) -> int:
    
    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = ", ".join(destinataires)
    message["Subject"] = sujet
    message.attach(MIMEText(msg, "plain"))
    
    try:
        # Connexion au serveur SMTP
        with smtplib.SMTP(smtp, 587) as server:
            server.starttls()  # Sécurise la connexion
            server.login(expediteur, mdp)  # Authentification
            server.sendmail(expediteur, destinataires, message.as_string())
        print("E-mail envoyé avec succès !")
        return 0
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
        return 1
    

def envoie_notif(msg: str, destinataires: list[str]):
    
    smtp, expediteur, mdp = mes_infos_mail()
    
    sujet = "Des Notes !!!"
    
    prefix = "Bon bah aujourdhui, IL Y A DES NOTES !!\n\n"
    
    envoie_mail_par_univ_angers(smtp, expediteur, mdp, destinataires, sujet, prefix+msg)



def main():
    
    destinataires = Init_destinataires()
    
    msg = "Bip Boup test 1 2\nwow le saut de ligne de fou"
    
    envoie_notif(msg, destinataires)






if __name__ == "__main__":
    main()