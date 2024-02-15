import time
from ggtools import *

def aff():
    path="C:/Program Files (x86)/Thonny/Lib/site-packages/thonny/plugins"
    for dossier_racine, dossiers, fichiers in os.walk(path):
        for fichier in dossiers:
            w = os.path.join(dossier_racine, fichier).replace("\\","/")
            w=w.replace(path+"/","")
            pl(w)


def demarrer():
    aff()

try:
    topdeb=time.time()
    demarrer()
    pl("Duree "+tos(time.time()-topdeb)+" s")
except Exception as e:
    pl(exceptionToString(e))