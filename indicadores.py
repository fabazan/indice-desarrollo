
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


enaho = pd.read_csv("D:/Universidad/Desarrollo Económico/Construcción de indicadores de desarrollo/sumaria_85_resumen.csv", sep=";", encoding="ANSI", low_memory=False)
enaho = enaho[["p45_1", "p45_2", "factor07", "mieperho", "inghog1d", "aÑo", "defes"]]

#   p45_1 : Nivel estudios del padre del jefe del hogar
#   p45_2 : Nivel de estudios de la madre del jefe del hogar
#   factor07 : Factor de expansión del hogar
#   mieperho : Miembros por hogar
#   inghog1d : Ingreso bruto total anual
#   defes : Deflactor espacial


ypc = [0 for i in range(467204)]

for index, row in enaho.iterrows():
    ypc[index] = row["inghog1d"]/(row["mieperho"] * row["defes"] * 12)

enaho["ypc"] = ypc


#     Listas para ingresos medios por grado de instrucción
#     0 : sin nivel
#     1 : primaria incompleta
#     2 : primaria completa
#     3 : secundaria incompleta
#     4 : secundaria completa
#     5 : superior no universitaria incompleta
#     6 : superior no universitaria incompleta
#     7 : superior universitaria incompleta
#     8 : superior universitaria completa
#     9 : no sabe
#     10 : vacio
gi = ["sin nivel", "primaria incompleta", "primaria completa", "secundaria incompleta", "secundaria completa", "superior no universitaria incompleta",
      "superior no universitaria completa", "superior universitaria incompleta", "superior universitaria completa", "no sabe"]

ypc_gi_p = [[[] for i in range(17)] for j in range(11)]

for index, row in enaho.iterrows():
    if row["aÑo"] == 2004:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][0].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][0].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][0].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2005:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][1].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][1].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][1].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2006:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][2].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][2].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][2].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2007:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][3].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][3].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][3].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2008:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][4].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][4].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][4].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2009:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][5].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][5].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][5].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2010:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][6].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][6].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][6].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2011:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][7].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][7].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][7].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2012:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][8].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][8].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][8].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2013:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][9].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][9].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][9].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2014:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][10].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][10].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][10].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2015:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][11].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][11].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][11].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2016:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][12].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][12].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][12].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2017:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][13].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][13].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][13].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2018:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][14].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][14].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][14].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2019:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][15].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][15].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][15].append(round(row["ypc"], 2))

    elif row["aÑo"] == 2020:
        if row["p45_1"] == gi[0]:
            ypc_gi_p[0][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[1]:
            ypc_gi_p[1][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[2]:
            ypc_gi_p[2][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[3]:
            ypc_gi_p[3][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[4]:
            ypc_gi_p[4][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[5]:
            ypc_gi_p[5][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[6]:
            ypc_gi_p[6][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[7]:
            ypc_gi_p[7][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[8]:
            ypc_gi_p[8][16].append(round(row["ypc"], 2))
        elif row["p45_1"] == gi[9]:
            ypc_gi_p[9][16].append(round(row["ypc"], 2))
        else:
            ypc_gi_p[10][16].append(round(row["ypc"], 2))


#   Ingreso medio por grado de instrucción para los años - 2004-2020
#   ypc[grado][año]
ypc_media = [[] for i in range(11)]
for j in range(11):
    for i in range(17):
        media = sum(ypc_gi_p[j][i])/len(ypc_gi_p[j][i])
        ypc_media[j].append(round(media, 2))


frec_p = [[0 for i in range(11)] for j in range(17)]
frec_m = [[0 for e in range(11)] for f in range(17)]


#   index = fila, row = columna
#   suma de personas que cumplan las condiciones (con el factor de expansion por persona)
#   (a cuantos representa cada persona)
for index, row in enaho.iterrows():
    if row["aÑo"] == 2004:
        if row["p45_1"] == "sin nivel":
            frec_p[0][0] = round(frec_p[0][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[0][1] = round(frec_p[0][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[0][2] = round(frec_p[0][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[0][3] = round(frec_p[0][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[0][4] = round(frec_p[0][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[0][5] = round(frec_p[0][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[0][6] = round(frec_p[0][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[0][7] = round(frec_p[0][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[0][8] = round(frec_p[0][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[0][9] = round(frec_p[0][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[0][10] = round(frec_p[0][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[0][0] = round(frec_m[0][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[0][1] = round(frec_m[0][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[0][2] = round(frec_m[0][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[0][3] = round(frec_m[0][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[0][4] = round(frec_m[0][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[0][5] = round(frec_m[0][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[0][6] = round(frec_m[0][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[0][7] = round(frec_m[0][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[0][8] = round(frec_m[0][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[0][9] = round(frec_m[0][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[0][10] = round(frec_m[0][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2005:
        if row["p45_1"] == "sin nivel":
            frec_p[1][0] = round(frec_p[1][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[1][1] = round(frec_p[1][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[1][2] = round(frec_p[1][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[1][3] = round(frec_p[1][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[1][4] = round(frec_p[1][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[1][5] = round(frec_p[1][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[1][6] = round(frec_p[1][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[1][7] = round(frec_p[1][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[1][8] = round(frec_p[1][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[1][9] = round(frec_p[1][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[1][10] = round(frec_p[1][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[1][0] = round(frec_m[1][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[1][1] = round(frec_m[1][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[1][2] = round(frec_m[1][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[1][3] = round(frec_m[1][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[1][4] = round(frec_m[1][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[1][5] = round(frec_m[1][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[1][6] = round(frec_m[1][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[1][7] = round(frec_m[1][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[1][8] = round(frec_m[1][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[1][9] = round(frec_m[1][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[1][10] = round(frec_m[1][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2006:
        if row["p45_1"] == "sin nivel":
            frec_p[2][0] = round(frec_p[2][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[2][1] = round(frec_p[2][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[2][2] = round(frec_p[2][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[2][3] = round(frec_p[2][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[2][4] = round(frec_p[2][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[2][5] = round(frec_p[2][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[2][6] = round(frec_p[2][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[2][7] = round(frec_p[2][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[2][8] = round(frec_p[2][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[2][9] = round(frec_p[2][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[2][10] = round(frec_p[2][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[2][0] = round(frec_m[2][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[2][1] = round(frec_m[2][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[2][2] = round(frec_m[2][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[2][3] = round(frec_m[2][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[2][4] = round(frec_m[2][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[2][5] = round(frec_m[2][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[2][6] = round(frec_m[2][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[2][7] = round(frec_m[2][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[2][8] = round(frec_m[2][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[2][9] = round(frec_m[2][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[2][10] = round(frec_m[2][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2007:
        if row["p45_1"] == "sin nivel":
            frec_p[3][0] = round(frec_p[3][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[3][1] = round(frec_p[3][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[3][2] = round(frec_p[3][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[3][3] = round(frec_p[3][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[3][4] = round(frec_p[3][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[3][5] = round(frec_p[3][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[3][6] = round(frec_p[3][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[3][7] = round(frec_p[3][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[3][8] = round(frec_p[3][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[3][9] = round(frec_p[3][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[3][10] = round(frec_p[3][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[3][0] = round(frec_m[3][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[3][1] = round(frec_m[3][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[3][2] = round(frec_m[3][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[3][3] = round(frec_m[3][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[3][4] = round(frec_m[3][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[3][5] = round(frec_m[3][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[3][6] = round(frec_m[3][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[3][7] = round(frec_m[3][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[3][8] = round(frec_m[3][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[3][9] = round(frec_m[3][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[3][10] = round(frec_m[3][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2008:
        if row["p45_1"] == "sin nivel":
            frec_p[4][0] = round(frec_p[4][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[4][1] = round(frec_p[4][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[4][2] = round(frec_p[4][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[4][3] = round(frec_p[4][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[4][4] = round(frec_p[4][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[4][5] = round(frec_p[4][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[4][6] = round(frec_p[4][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[4][7] = round(frec_p[4][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[4][8] = round(frec_p[4][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[4][9] = round(frec_p[4][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[4][10] = round(frec_p[4][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[4][0] = round(frec_m[4][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[4][1] = round(frec_m[4][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[4][2] = round(frec_m[4][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[4][3] = round(frec_m[4][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[4][4] = round(frec_m[4][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[4][5] = round(frec_m[4][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[4][6] = round(frec_m[4][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[4][7] = round(frec_m[4][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[4][8] = round(frec_m[4][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[4][9] = round(frec_m[4][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[4][10] = round(frec_m[4][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2009:
        if row["p45_1"] == "sin nivel":
            frec_p[5][0] = round(frec_p[5][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[5][1] = round(frec_p[5][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[5][2] = round(frec_p[5][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[5][3] = round(frec_p[5][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[5][4] = round(frec_p[5][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[5][5] = round(frec_p[5][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[5][6] = round(frec_p[5][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[5][7] = round(frec_p[5][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[5][8] = round(frec_p[5][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[5][9] = round(frec_p[5][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[5][10] = round(frec_p[5][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[5][0] = round(frec_m[5][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[5][1] = round(frec_m[5][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[5][2] = round(frec_m[5][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[5][3] = round(frec_m[5][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[5][4] = round(frec_m[5][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[5][5] = round(frec_m[5][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[5][6] = round(frec_m[5][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[5][7] = round(frec_m[5][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[5][8] = round(frec_m[5][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[5][9] = round(frec_m[5][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[5][10] = round(frec_m[5][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2010:
        if row["p45_1"] == "sin nivel":
            frec_p[6][0] = round(frec_p[6][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[6][1] = round(frec_p[6][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[6][2] = round(frec_p[6][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[6][3] = round(frec_p[6][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[6][4] = round(frec_p[6][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[6][5] = round(frec_p[6][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[6][6] = round(frec_p[6][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[6][7] = round(frec_p[6][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[6][8] = round(frec_p[6][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[6][9] = round(frec_p[6][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[6][10] = round(frec_p[6][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[6][0] = round(frec_m[6][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[6][1] = round(frec_m[6][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[6][2] = round(frec_m[6][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[6][3] = round(frec_m[6][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[6][4] = round(frec_m[6][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[6][5] = round(frec_m[6][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[6][6] = round(frec_m[6][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[6][7] = round(frec_m[6][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[6][8] = round(frec_m[6][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[6][9] = round(frec_m[6][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[6][10] = round(frec_m[6][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2011:
        if row["p45_1"] == "sin nivel":
            frec_p[7][0] = round(frec_p[7][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[7][1] = round(frec_p[7][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[7][2] = round(frec_p[7][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[7][3] = round(frec_p[7][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[7][4] = round(frec_p[7][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[7][5] = round(frec_p[7][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[7][6] = round(frec_p[7][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[7][7] = round(frec_p[7][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[7][8] = round(frec_p[7][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[7][9] = round(frec_p[7][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[7][10] = round(frec_p[7][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[7][0] = round(frec_m[7][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[7][1] = round(frec_m[7][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[7][2] = round(frec_m[7][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[7][3] = round(frec_m[7][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[7][4] = round(frec_m[7][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[7][5] = round(frec_m[7][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[7][6] = round(frec_m[7][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[7][7] = round(frec_m[7][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[7][8] = round(frec_m[7][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[7][9] = round(frec_m[7][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[7][10] = round(frec_m[7][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2012:
        if row["p45_1"] == "sin nivel":
            frec_p[8][0] = round(frec_p[8][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[8][1] = round(frec_p[8][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[8][2] = round(frec_p[8][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[8][3] = round(frec_p[8][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[8][4] = round(frec_p[8][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[8][5] = round(frec_p[8][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[8][6] = round(frec_p[8][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[8][7] = round(frec_p[8][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[8][8] = round(frec_p[8][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[8][9] = round(frec_p[8][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[8][10] = round(frec_p[8][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[8][0] = round(frec_m[8][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[8][1] = round(frec_m[8][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[8][2] = round(frec_m[8][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[8][3] = round(frec_m[8][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[8][4] = round(frec_m[8][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[8][5] = round(frec_m[8][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[8][6] = round(frec_m[8][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[8][7] = round(frec_m[8][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[8][8] = round(frec_m[8][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[8][9] = round(frec_m[8][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[8][10] = round(frec_m[8][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2013:
        if row["p45_1"] == "sin nivel":
            frec_p[9][0] = round(frec_p[9][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[9][1] = round(frec_p[9][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[9][2] = round(frec_p[9][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[9][3] = round(frec_p[9][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[9][4] = round(frec_p[9][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[9][5] = round(frec_p[9][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[9][6] = round(frec_p[9][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[9][7] = round(frec_p[9][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[9][8] = round(frec_p[9][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[9][9] = round(frec_p[9][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[9][10] = round(frec_p[9][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[9][0] = round(frec_m[9][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[9][1] = round(frec_m[9][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[9][2] = round(frec_m[9][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[9][3] = round(frec_m[9][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[9][4] = round(frec_m[9][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[9][5] = round(frec_m[9][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[9][6] = round(frec_m[9][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[9][7] = round(frec_m[9][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[9][8] = round(frec_m[9][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[9][9] = round(frec_m[9][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[9][10] = round(frec_m[9][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2014:
        if row["p45_1"] == "sin nivel":
            frec_p[10][0] = round(frec_p[10][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[10][1] = round(frec_p[10][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[10][2] = round(frec_p[10][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[10][3] = round(frec_p[10][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[10][4] = round(frec_p[10][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[10][5] = round(frec_p[10][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[10][6] = round(frec_p[10][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[10][7] = round(frec_p[10][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[10][8] = round(frec_p[10][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[10][9] = round(frec_p[10][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[10][10] = round(frec_p[10][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[10][0] = round(frec_m[10][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[10][1] = round(frec_m[10][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[10][2] = round(frec_m[10][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[10][3] = round(frec_m[10][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[10][4] = round(frec_m[10][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[10][5] = round(frec_m[10][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[10][6] = round(frec_m[10][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[10][7] = round(frec_m[10][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[10][8] = round(frec_m[10][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[10][9] = round(frec_m[10][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[10][10] = round(frec_m[10][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2015:
        if row["p45_1"] == "sin nivel":
            frec_p[11][0] = round(frec_p[11][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[11][1] = round(frec_p[11][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[11][2] = round(frec_p[11][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[11][3] = round(frec_p[11][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[11][4] = round(frec_p[11][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[11][5] = round(frec_p[11][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[11][6] = round(frec_p[11][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[11][7] = round(frec_p[11][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[11][8] = round(frec_p[11][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[11][9] = round(frec_p[11][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[11][10] = round(frec_p[11][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[11][0] = round(frec_m[11][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[11][1] = round(frec_m[11][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[11][2] = round(frec_m[11][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[11][3] = round(frec_m[11][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[11][4] = round(frec_m[11][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[11][5] = round(frec_m[11][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[11][6] = round(frec_m[11][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[11][7] = round(frec_m[11][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[11][8] = round(frec_m[11][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[11][9] = round(frec_m[11][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[11][10] = round(frec_m[11][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2016:
        if row["p45_1"] == "sin nivel":
            frec_p[12][0] = round(frec_p[12][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[12][1] = round(frec_p[12][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[12][2] = round(frec_p[12][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[12][3] = round(frec_p[12][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[12][4] = round(frec_p[12][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[12][5] = round(frec_p[12][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[12][6] = round(frec_p[12][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[12][7] = round(frec_p[12][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[12][8] = round(frec_p[12][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[12][9] = round(frec_p[12][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[12][10] = round(frec_p[12][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[12][0] = round(frec_m[12][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[12][1] = round(frec_m[12][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[12][2] = round(frec_m[12][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[12][3] = round(frec_m[12][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[12][4] = round(frec_m[12][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[12][5] = round(frec_m[12][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[12][6] = round(frec_m[12][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[12][7] = round(frec_m[12][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[12][8] = round(frec_m[12][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[12][9] = round(frec_m[12][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[12][10] = round(frec_m[12][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2017:
        if row["p45_1"] == "sin nivel":
            frec_p[13][0] = round(frec_p[13][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[13][1] = round(frec_p[13][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[13][2] = round(frec_p[13][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[13][3] = round(frec_p[13][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[13][4] = round(frec_p[13][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[13][5] = round(frec_p[13][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[13][6] = round(frec_p[13][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[13][7] = round(frec_p[13][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[13][8] = round(frec_p[13][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[13][9] = round(frec_p[13][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[13][10] = round(frec_p[13][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[13][0] = round(frec_m[13][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[13][1] = round(frec_m[13][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[13][2] = round(frec_m[13][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[13][3] = round(frec_m[13][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[13][4] = round(frec_m[13][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[13][5] = round(frec_m[13][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[13][6] = round(frec_m[13][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[13][7] = round(frec_m[13][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[13][8] = round(frec_m[13][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[13][9] = round(frec_m[13][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[13][10] = round(frec_m[13][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2018:
        if row["p45_1"] == "sin nivel":
            frec_p[14][0] = round(frec_p[14][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[14][1] = round(frec_p[14][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[14][2] = round(frec_p[14][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[14][3] = round(frec_p[14][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[14][4] = round(frec_p[14][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[14][5] = round(frec_p[14][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[14][6] = round(frec_p[14][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[14][7] = round(frec_p[14][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[14][8] = round(frec_p[14][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[14][9] = round(frec_p[14][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[14][10] = round(frec_p[14][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[14][0] = round(frec_m[14][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[14][1] = round(frec_m[14][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[14][2] = round(frec_m[14][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[14][3] = round(frec_m[14][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[14][4] = round(frec_m[14][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[14][5] = round(frec_m[14][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[14][6] = round(frec_m[14][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[14][7] = round(frec_m[14][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[14][8] = round(frec_m[14][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[14][9] = round(frec_m[14][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[14][10] = round(frec_m[14][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2019:
        if row["p45_1"] == "sin nivel":
            frec_p[15][0] = round(frec_p[15][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[15][1] = round(frec_p[15][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[15][2] = round(frec_p[15][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[15][3] = round(frec_p[15][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[15][4] = round(frec_p[15][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[15][5] = round(frec_p[15][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[15][6] = round(frec_p[15][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[15][7] = round(frec_p[15][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[15][8] = round(frec_p[15][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[15][9] = round(frec_p[15][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[15][10] = round(frec_p[15][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[15][0] = round(frec_m[15][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[15][1] = round(frec_m[15][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[15][2] = round(frec_m[15][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[15][3] = round(frec_m[15][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[15][4] = round(frec_m[15][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[15][5] = round(frec_m[15][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[15][6] = round(frec_m[15][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[15][7] = round(frec_m[15][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[15][8] = round(frec_m[15][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[15][9] = round(frec_m[15][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[15][10] = round(frec_m[15][10] + row["factor07"]*row["mieperho"])

    elif row["aÑo"] == 2020:
        if row["p45_1"] == "sin nivel":
            frec_p[16][0] = round(frec_p[16][0] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria incompleta":
            frec_p[16][1] = round(frec_p[16][1] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "primaria completa":
            frec_p[16][2] = round(frec_p[16][2] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria incompleta":
            frec_p[16][3] = round(frec_p[16][3] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "secundaria completa":
            frec_p[16][4] = round(frec_p[16][4] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria incompleta":
            frec_p[16][5] = round(frec_p[16][5] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior no universitaria completa":
            frec_p[16][6] = round(frec_p[16][6] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria incompleta":
            frec_p[16][7] = round(frec_p[16][7] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "superior universitaria completa":
            frec_p[16][8] = round(frec_p[16][8] + row["factor07"]*row["mieperho"])
        elif row["p45_1"] == "no sabe":
            frec_p[16][9] = round(frec_p[16][9] + row["factor07"]*row["mieperho"])
        else:
            frec_p[16][10] = round(frec_p[16][10] + row["factor07"]*row["mieperho"])
        if row["p45_2"] == "sin nivel":
            frec_m[16][0] = round(frec_m[16][0] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria incompleta":
            frec_m[16][1] = round(frec_m[16][1] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "primaria completa":
            frec_m[16][2] = round(frec_m[16][2] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria incompleta":
            frec_m[16][3] = round(frec_m[16][3] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "secundaria completa":
            frec_m[16][4] = round(frec_m[16][4] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria incompleta":
            frec_m[16][5] = round(frec_m[16][5] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior no universitaria completa":
            frec_m[16][6] = round(frec_m[16][6] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria incompleta":
            frec_m[16][7] = round(frec_m[16][7] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "superior universitaria completa":
            frec_m[16][8] = round(frec_m[16][8] + row["factor07"]*row["mieperho"])
        elif row["p45_2"] == "no sabe":
            frec_m[16][9] = round(frec_m[16][9] + row["factor07"]*row["mieperho"])
        else:
            frec_m[16][10] = round(frec_m[16][10] + row["factor07"]*row["mieperho"])


porcen_p = [[] for i in frec_p]
porcen_m = [[] for i in frec_m]

#   porcentaje
#   (frecuencias / suma(frecuencias))*100
for i in range(len(frec_p)):
    for j in range(len(frec_p[i])-2):
        porcen_p[i].append(round((frec_p[i][j])*100/sum(frec_p[i][0:-2]), 2))

for i in range(len(frec_m)):
    for j in range(len(frec_m[i])-2):
        porcen_m[i].append(round((frec_m[i][j])*100/sum(frec_m[i][0:-2]), 2))

fechas = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

orden = [i+1 for i in range(11)]
etiquetas = ["sin\nnivel", "prim.\ninc.", "prim.\ncom.", "sec.\ninc.", "sec.\ncomp.", "sup. no\nun. inc.", "sup. no\nun. com.", "sup.\nun. inc.", "sup.\nun. com.", "no sabe", "vacio"]

sal_min = [460, 460, 500, 530, 550, 550, 580, 675, 750, 750, 750, 750, 850, 850, 930, 930, 930]
var_pib_pc = [5.4, 6.7, 7.8, 8.4, 0.4, 7.5, 5.5, 5.4, 5.0, 1.4, 2.1, 2.4, 0.7, 2.0, 0.3, -12.4]


#   Ingreso en soles por grado de instrucción
fig = plt.gcf()
fig.set_size_inches(10, 6.5)
plt.plot(fechas, ypc_media[0], color=(0.1, 0.3, 0.8, 1), label="Sin nivel")
plt.plot(fechas, ypc_media[2], color=(0.1, 0.3, 0.8, 0.7), label="Prim. completa")
plt.plot(fechas, ypc_media[4], color=(0.1, 0.3, 0.8, 0.5), label="Sec. completa")
plt.plot(fechas, ypc_media[6], color=(0.1, 0.3, 0.8, 0.3), label="Sup. no univ. comp.")
plt.plot(fechas, ypc_media[8], color=(0.1, 0.3, 0.8, 0.15), label="Sup. uni. comp.")
plt.plot(fechas, sal_min, linestyle='dashed', marker="o", label="Salario mínimo")
plt.legend()
plt.title("Ingreso medio por grado de instrucción del padre")
plt.xlabel("Año")
plt.ylabel("En soles del 2007")
plt.savefig("C:/Users/adswf/Desktop/imagenes/ingreso_por_padre.png")
plt.show()

ypc_media_var = [[] for i in range(11)]
for i in range(11):
    for j in range(16):
        ypc_media_var[i].append(round((((ypc_media[i][j + 1] - ypc_media[i][j]) * 100) / ypc_media[i][j]), 2))


ypc_media_var_0_df = pd.DataFrame(ypc_media_var[0]).rename(columns={0: "A"})


#   Variación porcentual (sin nivel vs sin nivel con media movil vs PIB per cápita
fig = plt.gcf()
fig.set_size_inches(10, 6.5)
plt.plot(fechas[1:], ypc_media_var[0], color=(0.1, 0.3, 0.8, 0.3), label="Ingreso medio: Sin nivel")
plt.plot(fechas[1:], ypc_media_var_0_df["A"].rolling(window=2).mean(), color=(0.1, 0.3, 0.8, 0.8), label="Ingreso medio: Sin nivel MA(2)")
# plt.plot(fechas[1:], ypc_media_var[4], color=(0.1, 0.3, 0.8, 0.5), label="Sec. completa")
# plt.plot(fechas[1:], ypc_media_var[8], color=(0.1, 0.3, 0.8, 0.2), label="Sup. uni. comp.")
plt.plot(fechas[1:], var_pib_pc, linestyle='dashed', marker="o", label="PIB per cápita")
plt.legend()
plt.title("Variación porcentual: Ingreso medio (sin nivel) vs. PIB per cápita")
plt.xlabel("Año")
plt.ylabel("En variación % con respecto al año anterior")
plt.savefig("C:/Users/adswf/Desktop/imagenes/ingreso_por_padre_var.png")
plt.show()


#   En porcentaje (2004 vs 2020)
#   padre
x = np.arange(len(etiquetas[0:-2]))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, porcen_p[0], width, label='2004', color=(0.1, 0.3, 0.8, 0.5))
rects2 = ax.bar(x + width/2, porcen_p[16], width, label='2020', color=(0.1, 0.3, 0.8, 0.8))
fig.set_size_inches(10, 6.5)
plt.title("Grado de instrucción: Padre 2004 vs. 2020")
plt.xlabel("Grado de instrucción")
plt.ylabel("% de la población")
ax.set_xticks(x)
ax.set_xticklabels(etiquetas[0:-2])
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
fig.tight_layout()
plt.savefig("C:/Users/adswf/Desktop/imagenes/padre_porcen_double_2004.png")
plt.show()

#   madre
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, porcen_m[0], width, label='2004', color=(0.4, 0.2, 0.6, 0.3))
rects2 = ax.bar(x + width/2, porcen_m[16], width, label='2020', color=(0.4, 0.2, 0.6, 0.6))
fig.set_size_inches(10, 6.5)
plt.title("Grado de instrucción: Madre 2004 vs. 2020")
plt.xlabel("Grado de instrucción")
plt.ylabel("% de la población")
ax.set_xticks(x)
ax.set_xticklabels(etiquetas[0:-2])
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
fig.tight_layout()
plt.savefig("C:/Users/adswf/Desktop/imagenes/madre_porcen_double_2004.png")
plt.show()


# #   En cantidad de personas (para cada uno de los 17 años 2004-2020)
# #   padre
# for i in range(17):
#     fig = plt.gcf()
#     fig.set_size_inches(10, 6.5)
#     plt.title("Grado de instrucción: Padre " + str(i+2004))
#     plt.xlabel("Grado de instrucción")
#     plt.ylabel("Total (en millones de personas)")
#     plt.bar(etiquetas[0:-1], frec_p[i][0:-1], color=(0.0, 0.35, 0.6, 0.8))
#     plt.savefig("C:/Users/adswf/Desktop/imagenes/padre_" + str(i+2004) + ".png")
#     plt.show()
# #   madre
# for i in range(17):
#     fig = plt.gcf()
#     fig.set_size_inches(10, 6.5)
#     plt.title("Grado de instrucción: Madre " + str(i + 2004))
#     plt.xlabel("Grado de instrucción")
#     plt.ylabel("Total (en millones de personas)")
#     plt.bar(etiquetas[0:-1], frec_m[i][0:-1], color=(0.4, 0.2, 0.6, 0.6))
#     plt.savefig("C:/Users/adswf/Desktop/imagenes/madre_" + str(i+2004) + ".png")
#     plt.show()
#
# #   En porcentaje (para cada uno de los 17 años 2004-2020)
# #   padre
# for i in range(17):
#     fig = plt.gcf()
#     fig.set_size_inches(10, 6.5)
#     plt.title("Grado de instrucción: Padre " + str(i+2004))
#     plt.xlabel("Grado de instrucción")
#     plt.ylabel("% de la población")
#     plt.bar(etiquetas[0:-1], porcen_p[i])
#     plt.savefig("C:/Users/adswf/Desktop/imagenes/padre_porcen_" + str(i+2004) + ".png")
#     plt.show()
# #   madre
# for i in range(17):
#     fig = plt.gcf()
#     fig.set_size_inches(10, 6.5)
#     plt.title("Grado de instrucción: Madre " + str(i+2004))
#     plt.xlabel("Grado de instrucción")
#     plt.ylabel("% de la población")
#     plt.bar(etiquetas[0:-1], porcen_m[i], color=(0.4, 0.2, 0.6, 0.6))
#     plt.savefig("C:/Users/adswf/Desktop/imagenes/madre_porcen_" + str(i+2004) + ".png")
#     plt.show()




#   Función de distribución acumulada

for an in range(17):
    fig = plt.gcf()
    fig.set_size_inches(10, 6.5)
    data = np.array(ypc_gi_p[0][an])
    x = np.sort(data)
    y = np.arange(len(ypc_gi_p[0][an])) / float(len(ypc_gi_p[0][an]))
    plt.plot(x, y, marker='o', label="sn", color=(0.1, 0.2, 0.8, 0.2))

    data = np.array(ypc_gi_p[4][an])
    x = np.sort(data)
    y = np.arange(len(ypc_gi_p[4][an])) / float(len(ypc_gi_p[4][an]))
    plt.plot(x, y, marker='o', label="sc", color=(0.1, 0.2, 0.6, 0.2))

    data = np.array(ypc_gi_p[8][an])
    x = np.sort(data)
    y = np.arange(len(ypc_gi_p[8][an])) / float(len(ypc_gi_p[8][an]))
    plt.plot(x, y, marker='o', label="suc", color=(0.1, 0.2, 0.4, 0.4))

    plt.xlabel('Ingreso medio en soles')
    plt.ylabel('Distribución acumulada')
    plt.legend()
    plt.xlim([0, 10000])
    plt.title('Función de distribución acumulada para el ingreso\npor grado de estudios del padre: ' + str(2004+an))
    plt.savefig("C:/Users/adswf/Desktop/imagenes/padre_porcen_fundis_" + str(2004+an) + ".png")
    plt.show()



#   Varación media (para el periodo 2004-2020) de la renta per cápita media (por grado de instrucción)
ypc_media_var_media = [round(sum(ypc_media_var[i])/len(ypc_media_var[i]), 2) for i in range(11)]

etiquetas2 = etiquetas[:-2] + ["media"]
ypc_media_var_media = ypc_media_var_media[:-2] + [round(sum(ypc_media_var_media)/len(ypc_media_var_media), 2)]

#   grafico de barras crecimiento en los ingresos por grado de instruccion crecimiento promedio 2004-2020

# fig = plt.gcf()
# fig.set_size_inches(10, 6.5)
# plt.title("Crecimiento del ingreso medio para el periodo 2004-2020")
# plt.xlabel("Grado de instrucción")
# plt.ylabel("Crecimiento % promedio")
# plt.bar(etiquetas2, ypc_media_var_media, color=[(0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
#                                                 (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
#                                                 (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
#                                                 (0.1, 0.3, 0.6, 0.9)])
# plt.savefig("C:/Users/adswf/Desktop/imagenes/padre_crecimiento_medio1.png")
# plt.show()


x = np.arange(len(etiquetas2))
width = 0.8
fig, ax = plt.subplots()
rects1 = ax.bar(x, ypc_media_var_media, width, color=[(0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
                                                (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
                                                (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
                                                (0.1, 0.3, 0.6, 0.9)])
fig.set_size_inches(10, 6.5)
plt.title("Crecimiento del ingreso medio para el periodo 2004-2020 por grado de instrucción del padre")
plt.xlabel("Grado de instrucción")
plt.ylabel("Crecimiento % del ingreso medio")
ax.set_xticks(x)
ax.set_xticklabels(etiquetas2)
ax.bar_label(rects1)
fig.tight_layout()
plt.savefig("C:/Users/adswf/Desktop/imagenes/padre_crecimiento_medio2.png")
plt.show()



# plt.bar(gi[:-1], porc_padre_2004)
# plt.xticks(gi[:-1], [textwrap.fill(i.capitalize(), width=17) for i in gi[:-1]], rotation="vertical", **fuente)
# plt.subplots_adjust(bottom=0.4, top=0.90)
# plt.show()
