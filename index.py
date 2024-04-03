import os
# sin SWI_HOME_DIR tira error de recursos
os.putenv("SWI_HOME_DIR","C:\\Program Files\\swipl")

from pyswip import Prolog

prolog = Prolog()

prolog.consult('index.pl')

for consulta in prolog.query('mi_nombre(X , Y)'):
    print("El nombre extraido de PROLOG es: "+ consulta['X'], consulta['Y'])