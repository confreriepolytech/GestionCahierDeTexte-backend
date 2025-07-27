import os
import sys
import django

# 1. Calculate the correct base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. Add the project root to Python path
sys.path.insert(0, BASE_DIR)

# 3. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestionCahierDeTexte3.settings")

# 4. Initialize Django
try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    sys.exit(1)



import requests
import re
import json

from accounts.models import Professeur, Ue, Classe, CustomUser

file_path = './data.txt'   # chemin relatif vers le fichier .txt

"""with open(file_path, 'r', encoding='utf-8')  as f:
    content = f.read()

blocks = content.strip().split("1")
for block in blocks:
    lines = block.strip()
    print(lines)"""


"""
#with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split the file into blocks using regex: look for numbers followed by line breaks
blocks = re.split(r'\n\d+\n', content)

# Clean empty entries
blocks = [block.strip() for block in blocks if block.strip()]

data = []
# Now process each block
for i, block in enumerate(blocks, start=1):
    entry = {}
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    print(f"--- UE {i} ---")

    try:
        entry = {}

        if lines[0].strip().isdigit():
            # Case where first line is a digit → this line is  not the title
            ue_line = lines[1]
            classe_line = lines[2]
            teacher_line = lines[3]
        else:
            ue_line = lines[0]
            classe_line = lines[1]
            teacher_line = lines[2]

        # Extract UE title, code, intitule
        entry['ue_title'] = ue_line
        entry['ue_code'] = ue_line.split('-')[0].strip()
        entry['ue_intitule'] = ue_line.split('-')[-1].strip()

        # Extract mention
        entry['mention'] = classe_line[1:3]

        # Extract classes (handle +, et, or single)
        if '+' in classe_line:
            parts = classe_line.split('+')
            entry['classe'] = [part[3:-1].strip().replace(' ', '_') for part in parts]
        elif 'et' in classe_line:
            parts = classe_line.split('et')
            entry['classe'] = [part[3:-1].strip().replace(' ', '_') for part in parts]
        else:
            entry['classe'] = [classe_line[3:-1].strip().replace(' ', '_')]

        # Extract teacher(s)
        entry['teacher'] = [t.strip() for t in teacher_line.split('et')]

        #define 'creanaux'
        entry['creanaux']=[{
            'Lundi':'7H-9H'

        }]
        data.append(entry)

    except IndexError:
        print("Incomplete block:")
        print(lines)


for i,ue in enumerate(data):
    ue["teacher"]=[
        {
        'role':'professeur',
        'email': f'text_email_{i}@gmail.com',
        'nom': prof.strip(),
        'prenom': 'Unkown',
        'password': '123456',
        'is_active':True,
        'is_verified':True,
        }for prof in ue["teacher"]
    ]
    ue['classe']= [
        {
            'nom_licence':classe,
            'niveau':'Licence',
            'departement':'GI' if classe[:2] in ['SR','GL','IA','IS','LT'] else classe[:2] ,
            'mention': ue['mention']
        }for classe in ue["classe"]
    ]
    del ue['mention']
    del ue['ue_title']"""

"""try:
        if lines[0].strip() == 1:
            lines[1].split('-')
            entry['ue_title'] = lines[1]
            entry['ue_code'] = lines[1].split('-')[0].strip()
            entry['ue_intitule'] = lines[1].split('-')[-1].strip()
            entry['mention'] = lines[2][1:3]
            if '+' in lines[2].split(' '):
                entry['classe'] = [lines[2].split('+')[0][3:-1].strip().replace(' ', '_'),
                                   lines[2].split('+')[-1][3:-1].strip().replace(' ', '_')]
            elif 'et' in lines[2].split(' '):
                entry['classe'] = [lines[2].split('et')[0][3:-1].strip().replace(' ', '_'),
                                  lines[2].split('+')[-1][3:-1].strip().replace(' ', '_')]
            else:
                entry['classe'] = lines[2][3:-1].strip().replace(' ', '_')
            entry['teacher'] = lines[3].split('et')

        entry['ue_title'] = lines[0]
        entry['ue_code'] = lines[0].split('-')[0].strip()
        entry['ue_intitule'] = lines[0].split('-')[-1].strip()
        entry['mention'] = lines[1][1:3]
        if '+' in lines[1].split(' '):
            entry['classe'] = [lines[1].split('+')[0][3:-1].strip().replace(' ', '_'),
                               lines[1].split('+')[-1][3:-1].strip().replace(' ', '_')]
        elif 'et' in lines[2].split(' '):
            entry['classe'] = [lines[1].split('et')[0][3:-1].strip().replace(' ', '_'),
                               lines[1].split('+')[-1][3:-1].strip().replace(' ', '_')]
        else:
            entry['classe'] = lines[1][3:-1].strip().replace(' ', '_')
        entry['teacher'] = lines[2].split('et')
        data.append(entry)
    except IndexError:
        print("Incomplete block:")
        print(lines)"""





"""
#with open("ue_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)"""

# Load data from your JSON file
with open("C:/Users/rustp/Documents/backend/GestionCahierDeTexte3/accounts/ue_data.json", encoding='utf-8') as f:
    ue_data_list = json.load(f)

for ue_data in ue_data_list:
    ue, created = Ue.objects.get_or_create(
        code_UEs=ue_data['ue_code'],
        defaults={'code_UEs': ue_data['ue_code'],
                  'intitule_UEs': ue_data['ue_intitule'],
                  'crenaux': ue_data['creanaux'],
                  }
    )

    for classe_data in ue_data['classe']:
        classe, _ = Classe.objects.get_or_create(
            nom_licence = classe_data['nom_licence'],
            defaults = classe_data,
        )
        ue.classe = classe
        ue.save()
        break

    if not created and ue.intitule_UEs != ue_data['ue_intitule']:
        ue.intitule_UEs = ue_data['ue_intitule']
        ue.save()

    for prof_data in ue_data['teacher']:
        custom_user, _ = CustomUser.objects.get_or_create(
            email=prof_data['email'],
            defaults=prof_data
        )
        prof,_= Professeur.objects.get_or_create(user_id=custom_user,defaults={
            'user_id':custom_user
        })
        ue.id_prof = prof  # M2M relationship
        ue.save()
        break

    print(f"UE '{ue.code_UEs}' populated with  professeur(s).")




base_url ="http://127.0.0.1:8000/"
add_class_endpoint = base_url + "/cahier-de-texte/Classe/"

data_classe = [
    {'nom_licence':'Tronc-commun_S1',
     'niveau':'Licence',
      'departement':'Tronc-commun',
      'mention':'Licence_Fondamentale'
},
 {'nom_licence':'Tronc-commun_S2',
     'niveau':'Licence',
      'departement':'Tronc-commun',
      'mention':'Licence_Fondamentale'
},
 {'nom_licence':'Tronc-commun_S3',
     'niveau':'Licence',
      'departement':'Tronc-commun',
      'mention':'Licence_Fondamentale'
},
 {'nom_licence':'GE_S4',
     'niveau':'Licence',
      'departement':'Génie_Electrique',
      'mention':'Licence_Fondamentale'
},
 {'nom_licence':'GE_S5',
     'niveau':'Licence',
      'departement':'Génie_Electrique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'GE_S6',
     'niveau':'Licence',
      'departement':'Génie_Electrique',
      'mention':'Licence_Fondamentale'
},

{'nom_licence':'GM_S4',
     'niveau':'Licence',
      'departement':'Génie_Mécanique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'GM_S5',
     'niveau':'Licence',
      'departement':'Génie_Mécanique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'GM_S6',
     'niveau':'Licence',
      'departement':'Génie_Mécanique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'GC_S4',
     'niveau':'Licence',
      'departement':'Génie_Civil',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'GC_S5',
     'niveau':'Licence',
      'departement':'Génie_Civil',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'GC_S6',
     'niveau':'Licence',
      'departement':'Génie_Civil',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'IS_S4',
     'niveau':'Licence',
      'departement':'Génie_Informatique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'IS_S5',
     'niveau':'Licence',
      'departement':'Génie_Informatique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'IS_S6',
     'niveau':'Licence',
      'departement':'Génie_Informatique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'IA-BD_S4',
     'niveau':'Licence',
      'departement':'Génie_Informatique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'IA-BD_S5',
     'niveau':'Licence',
      'departement':'Génie_Informatique',
      'mention':'Licence_Fondamentale'
},
{'nom_licence':'IA-BD_S6',
     'niveau':'Licence',
      'departement':'Génie_Informatique',
      'mention':'Licence_Fondamentale'
}
]
"""
for classe in data_classe:
    response = requests.post(add_class_endpoint, data=classe)
    print(response.text, response.status_code)"""






# for creation of pofesseur

professeur_endpoint = base_url + '/accounts/api/auth/users/registration/'

data_professeur =[
    {
     'role':'professeur',
     'email': 'text_email_1@gmail.com',
     'nom': 'AFIO',
     'prenom': 'Ayaréma',
     'password': 'password_test_1',
     'is_active':True,
     'is_staff':True,
     'course' :'{ GEM1420 - Notion de RDM pour ingénieur GE ( LF_GE_S6) }'
},
{
     'role':'professeur',
     'email': 'text_email_2@gmail.com',
     'nom': 'ATTIPOU',
     'prenom': 'Kodjo',
     'password': 'password_test_2',
     'is_active':True,
     'is_staff':True,
     'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_3@gmail.com',
     'nom': 'AKORO',
     'prenom': 'justin',
     'password': 'password_test_3',
     'is_active':True,
     'is_staff':True,
     'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_4@gmail.com',
     'nom': 'GUENOUKPATI',
     'prenom': 'Agbassou',
     'password': 'password_test_4',
     'is_active':True,
     'is_staff':True,
     'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_5@gmail.com',
     'nom': 'TIASSOU',
     'prenom': 'Kevin',
     'password': 'password_test_5',
     'is_active':True,
     'is_staff':True,
     'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_6@gmail.com',
     'nom': 'LIMAZIE',
     'prenom': 'Toï',
     'password': 'password_test_6',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_7@gmail.com',
     'nom': 'AYELEH',
     'prenom': 'Edo-Owodou',
     'password': 'password_test_7',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_8@gmail.com',
     'nom': 'AYELEH',
     'prenom': 'Edo-Owodou',
     'password': 'password_test_8',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_9@gmail.com',
     'nom': 'WOTODZO',
     'prenom': 'Francis',
     'password': 'password_test_9',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_10@gmail.com',
     'nom': 'AGOSSEME',
     'prenom': 'Kokou Anani',
     'password': 'password_test_10',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_11@gmail.com',
     'nom': 'AGOSSEME',
     'prenom': 'Kokou Anani',
     'password': 'password_test_11',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},
{
     'role':'professeur',
     'email': 'text_email_12@gmail.com',
     'nom': 'AGOSSEME',
     'prenom': 'Kokou Anani',
     'password': 'password_test_12',
     'is_active':True,
     'is_staff':True,
'course' :'{}'
},

{
     'role':'professeur',
     'email': 'text_email_13@gmail.com',
     'nom': 'HOETOWOU',
     'prenom': 'Yao Amenouglo',
     'password': 'password_test_13',
     'is_active':True,
     'is_staff':True,
'course' :'{INF1426 - Développement d\’applications de bureau LP GL S4 , INF1428 - Modélisation  UML  (LP GL S4)}'
},
{
     'role':'professeur',
     'email': 'text_email_14@gmail.com',
     'nom': 'TAMPANGO',
     'prenom': 'Yannick',
     'password': 'password_test_14',
     'is_active':True,
     'is_staff':True,
'course' :'{MTH1620 - Statistiques exploratoires mltidimensionelles (LF IA S6) }'
},
{
     'role':'professeur',
     'email': 'text_email_15@gmail.com',
     'nom': 'MIHAM',
     'prenom': 'Kodjo',
     'password': 'password_test_15',
     'is_active':True,
     'is_staff':True,
'course' :'{ANG1220 - Anglais : Lire et Ecrire  LP GE S2 et LP GC S2 et LP GM S2) , ANG1221 - Anglais : compréhension orale et écrite ANG1620 - Anglais   (LF IA S6+LF IS S6+LF LT S6)}'
},
{
     'role':'professeur',
     'email': 'text_email_17@gmail.com',
     'nom': 'TCHIOU',
     'prenom': 'Solim',
     'password': 'password_test_17',
     'is_active':True,
     'is_staff':True,
'course' :'{ANG1221 - Anglais : compréhension orale et écrite LF TC S2}'
},
{
     'role':'professeur',
     'email': 'text_email_18@gmail.com',
     'nom': 'IDRISSOU',
     'prenom': 'Abdou Ahabou',
     'password': 'password_test_18',
     'is_active':True,
     'is_staff':True,
'course' :'{1GEC1622 - Hydrologie de Bases (LF GC S6), GEC1423 - Hydraulique des bases LF GC S4  ,2GEC1622 - Hydrologie appliquée GC S6}'
},
{
     'role':'professeur',
     'email': 'text_email_19@gmail.com',
     'nom': 'AGBOSSOU',
     'prenom': 'Komi Akpé',
     'password': 'password_test_19',
     'is_active':True,
     'is_staff':True,
'course' :'{GEL1428 - Introduction à l’Electronique de Puissance LP GE S4}'
},
{
     'role':'professeur',
     'email': 'text_email_20@gmail.com',
     'nom': 'GBAFA',
     'prenom': 'Senanou',
     'password': 'password_test_20',
     'is_active':True,
     'is_staff':True,
'course' :'{ 1GEC1620 - Routes : Conception Géométrique LF GC S6}'
},
{
     'role':'professeur',
     'email': 'text_email_21@gmail.com',
     'nom': 'ADJALLAH',
     'prenom': 'Kondo Hloindo',
     'password': 'password_test_21',
     'is_active':True,
     'is_staff':True,
'course' :'{GEL1624 - Système de Maintenance LF GE S6,  GEL1627 - Electroniques : Fonctions et  Systèmes LF GE S6}'
},
{
     'role':'professeur',
     'email': 'text_email_22@gmail.com',
     'nom': 'ANAKPA',
     'prenom': 'Manawa',
     'password': 'password_test_22',
     'is_active':True,
     'is_staff':True,
'course' :'{ INF1620 - Adminsitration de bases de données LF IA IS ,  INF1429 - Normes documentaires LP GL S4}'
},
{
     'role':'professeur',
     'email': 'text_email_23@gmail.com',
     'nom': 'N\'TSOUAGLO',
     'prenom': 'Kokouvi',
     'password': 'password_test_23',
     'is_active':True,
     'is_staff':True,
'course' :'{1GEM1627 - Fabrication mécanique : Tournage et Fraisage LF GM S6 ,}'
},
{
     'role':'professeur',
     'email': 'text_email_24@gmail.com',
     'nom': 'ABOLO-SEWOVi',
     'prenom': 'Komi Romain',
     'password': 'password_test_24',
     'is_active':True,
     'is_staff':True,
'course' :'{INF1625 - Développement d\'applications distribuées LF IA S6}'
},
    {
        'role': 'professeur',
        'email': 'text_email_25@gmail.com',
        'nom': 'AMEY',
        'prenom': 'Kossi Bollanigni',
        'password': 'password_test_25',
        'is_active': True,
        'is_staff': True,
'course' :'{}'
    },
{
        'role': 'professeur',
        'email': 'text_email_26@gmail.com',
        'nom': 'AMEY',
        'prenom': 'Kossi Bollanigni',
        'password': 'password_test_26',
        'is_active': True,
        'is_staff': True,
'course' :'{2GEC1424 - Justification des sections LP GC S4 , GEC1624 - Construction métallique : notions de bases et technologie LF GC S6}'
    },
{
        'role': 'professeur',
        'email': 'text_email_27@gmail.com',
        'nom': 'AYITE',
        'prenom': 'Danyi',
        'password': 'password_test_27',
        'is_active': True,
        'is_staff': True,
'course' :'{1GEC1621 - Béton armé : Calcul des sollicitations LF GE S6 ,  2GEC1422 - Résistance des Matériaux pour GC LF GC S4 , 2GEC1621 - Justification des sections des ouvrages LFGC S6'
    },
{
        'role': 'professeur',
        'email': 'text_email_28@gmail.com',
        'nom': 'POTOKOYE',
        'prenom': 'Gnimtou',
        'password': 'password_test_28',
        'is_active': True,
        'is_staff': True,
'course' :'{MTH1620 - Statistique exploratoires multidimensionelles LF IA BD S6}'
    },
]

