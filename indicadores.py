
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import textwrap
import weightedstats as ws



pd.set_option('display.max_columns', None)

desktop = "C:/Users/pc/Desktop/"

inicio = 2004
fin = 2021
fuente = {'fontname': "Times New Roman"}


gi = ["sin nivel",
      "primaria incompleta", "primaria completa",
      "secundaria incompleta", "secundaria completa",
      "superior no universitaria incompleta", "superior no universitaria completa",
      "superior universitaria incompleta", "superior universitaria completa",
      "no sabe"]
grupos = ["Sin nivel", "Primaria", "Secundaria", "Superior no universitaria", "Superior universitaria"]
grupos2 = ["Sin nivel", "Educación básica", "Educación secundaria", "Educación superior"]

departamentos = ["Amazonas", "Áncash", "Apurímac", "Arequipa", "Ayacucho", "Cajamarca", "Callao", "Cusco",
                 "Huancavelica", "Huánuco", "Ica", "Junín", "La Libertad", "Lambayeque", "Lima", "Loreto",
                 "Madre de Dios", "Moquegua", "Pasco", "Piura", "Puno", "San Martín", "Tacna", "Tumbes",
                 "Ucayali"]

departamentosISO = ["AMA", "ANC", "APU", "ARE", "CAJ", "CAL", "CUS",
                    "HUV", "HUC", "ICA", "JUN", "LAL", "LAM", "LIM", "LOR",
                    "MDD", "MOQ", "PAS", "PIU", "PUN", "SAM", "TAC", "TUM",
                    "UCA"]




periodo_i = [i for i in range(inicio, fin + 1)]
periodo_s = [str(i) for i in periodo_i]
negro = "black"
color_dict = {'capprops': dict(color=negro),
              'medianprops': dict(color=negro, linewidth=2),
              'whiskerprops': dict(color=negro),
              'meanprops': dict(markeredgecolor=negro, markerfacecolor=negro)}
marcadores = ["^", "P", "s", "*", "D", "X", "p", "h", "8", "o"]
colores = [(0.2, 0.2, 0.8, 0.3), (0.2, 0.4, 0.8, 0.3), (0.2, 0.6, 0.8, 0.3), (0.2, 0.8, 0.8, 0.3)]
figsizes = (10, 5.7)
source = "Fuente: Elaboración propia a partir de datos del Instituto Nacional de Estadística e Informática (INEI)"
source_pos = (0.08, 0.01)


enaho = pd.read_csv(desktop + "data_indic.csv",
                    sep=";", encoding="ANSI", low_memory=False)


enaho = enaho[["p45_1", "p45_2", "factor07", "mieperho", "inghog1d", "aÑo", "defes", "dept"]]
enaho["yfam"] = enaho["inghog1d"]/(enaho["defes"] * 12)
# enaho["factorper"] = enaho["factor07"]*enaho["mieperho"]

#    Variables usadas
#        p45_1: Nivel estudios del padre del jefe del hogar
#        p45_2: Nivel de estudios de la madre del jefe del hogar
#     factor07: Factor de expansión del hogar
#     mieperho: Miembros por hogar
#     inghog1d: Ingreso bruto total anual
#        defes: Deflactor espacial

#     Listas para ingresos medios por grado de instrucción
#      0: sin nivel
#      1: primaria incompleta
#      2: primaria completa
#      3: secundaria incompleta
#      4: secundaria completa
#      5: superior no universitaria incompleta
#      6: superior no universitaria incompleta
#      7: superior universitaria incompleta
#      8: superior universitaria completa
#      9: no sabe
#     10: vacío


gi_dict = {key: value for (key, value) in zip(gi, [i for i in range(0, len(gi) - 1)])}
enaho["padre"] = enaho["p45_1"].map(gi_dict)
enaho["madre"] = enaho["p45_2"].map(gi_dict)
enaho["gimax"] = enaho[["padre", "madre"]].max(axis=1)
enaho["gimax"] = enaho["gimax"].map({key: value for (key, value) in zip(gi_dict.values(), gi_dict.keys())})

enaho = enaho.drop(["padre", "madre"], axis=1)
enahoyears = {key: value for (key, value) in zip([f"{i}" for i in range(inicio, fin + 1)], [enaho[enaho['aÑo'] == i] for i in range(inicio, fin + 1)])}


muestra = pd.DataFrame({"Año": periodo_i,
                        "Muestra": [enaho[enaho['aÑo'] == i].shape[0] for i in periodo_i],
                        "Población": [round(enahoyears[f'{i}']['factor07'].sum()) for i in periodo_i]})

# print(muestra)
# muestra.to_csv(desktop + "poblacion.csv", sep=";", encoding="ANSI")

yfam_medio = [round(np.average(enahoyears[f"{i}"]["yfam"], weights=enahoyears[f"{i}"]["factor07"])) for i in periodo_i]
yfam_mediano = [round(ws.weighted_median(enahoyears[f"{i}"]["yfam"], weights=enahoyears[f"{i}"]["factor07"])) for i in periodo_i]

# pd.DataFrame({"Año": periodo_i,
#               "Ingreso medio": yfam_medio,
#               "Ingreso mediano": yfam_mediano}).to_csv(desktop + "ymediomediano.csv", sep=";")


def reindex_df(dataframe, weight):
    dataframe = dataframe.reindex(dataframe.index.repeat(dataframe[weight]))
    dataframe.reset_index(drop=True, inplace=True)
    return dataframe["yfam"]


plt.figure(figsize=figsizes)
caja = plt.boxplot([reindex_df(enahoyears[f"{i}"], weight="factor07") for i in periodo_i],
                   showmeans=True, showfliers=False, showbox=True, showcaps=True, whis=3, **color_dict)
plt.legend([caja['medians'][0], caja['means'][0]], ['Ingreso mediano', 'Ingreso medio'],
           prop=font_manager.FontProperties(family=fuente["fontname"]))
# Ingreso medio
plt.plot([f"{inicio - 1}", f"{inicio}"], [yfam_medio[0], yfam_medio[1]], alpha=0)
for i in range(len(periodo_s) - 1):
    plt.plot([f"{periodo_s[i]}", f"{periodo_s[i + 1]}"], [yfam_medio[i], yfam_medio[i + 1]], negro, linestyle="dashed", linewidth=0.9)
# Ingreso mediano
plt.plot([f"{inicio - 1}", f"{inicio}"], [yfam_mediano[0], yfam_mediano[1]], alpha=0)
for i in range(len(periodo_s) - 1):
    plt.plot([f"{periodo_s[i]}", f"{periodo_s[i + 1]}"], [yfam_mediano[i], yfam_mediano[i + 1]], negro, linestyle="dashed", linewidth=0.9)
plt.xticks([i for i in range(1, len(periodo_s) + 1)], periodo_s, **fuente)
plt.yticks(**fuente)
plt.xlim([f"{inicio-1}", f"{fin+1}"])
plt.title(f"Ingreso familiar de la población peruana, {inicio}-{fin}", **fuente)
plt.xlabel("Año", **fuente)
plt.ylabel("Ingreso mensual familiar (en soles)", **fuente)
plt.grid()
plt.figtext(source_pos[0], source_pos[1], source, **fuente)
plt.subplots_adjust(bottom=0.12)
plt.savefig(desktop + f"imagenes/boxplot.png", bbox_inches='tight')
# plt.show()
plt.close()


def barchars(porcentajes, agrupado, labels, width=0.35):
    x = np.arange(len(labels))
    for j in ["padre", "madre"]:
        if j == "padre":
            colores1 = (0.1, 0.3, 0.8, 0.5)
            colores2 = (0.1, 0.3, 0.8, 0.8)
            k = "del"
        else:
            colores1 = (0.4, 0.2, 0.6, 0.3)
            colores2 = (0.4, 0.2, 0.6, 0.6)
            k = "de la"
        for i in range(2020, 2021 + 1):
            fig, ax = plt.subplots()
            fig.set_size_inches(figsizes[0], figsizes[1])
            rects1 = ax.bar(x - width / 2, porcentajes[f"{j}2004"], width, label=f'{periodo_s[0]}', color=colores1)
            rects2 = ax.bar(x + width / 2, porcentajes[f"{j}{i}"], width, label=f'{i}', color=colores2)
            plt.title(f"Grado de instrucción {k} {j} del jefe de hogar, {periodo_s[0]} vs. {i}", **fuente)
            plt.xlabel("Grado de instrucción", **fuente)
            plt.ylabel("% de las familias", **fuente)
            plt.xticks(x, [textwrap.fill(m.capitalize(), width=16) for m in labels], **fuente)
            plt.yticks(**fuente)
            ax.legend(prop=font_manager.FontProperties(family=fuente["fontname"]))
            ax.bar_label(rects1, padding=3, **fuente)
            ax.bar_label(rects2, padding=3, **fuente)
            fig.tight_layout()
            plt.figtext(source_pos[0], source_pos[1], source, **fuente)
            plt.subplots_adjust(bottom=0.18)
            plt.savefig(desktop + f"/imagenes/barras{agrupado}{j}{i}.png", bbox_inches='tight')
            # plt.show()
            plt.close()


def weighted_vals(valores, pesos):
    average = np.average(valores, weights=pesos)
    variance = np.average((valores-average)**2, weights=pesos)
    return average, variance


def etas_f(enahobygroups, etas, j, departamentos, dept_i, dept=False):
    # media de tipos
    medias = []
    # ponderación de tipos
    fs = []

    for i in range(len(grupos2)):
        if dept is True:
            data = enahobygroups[f"{j}g{i + 1}"][enahobygroups[f"{j}g{i + 1}"]["dept"] == departamentos[dept_i]]

        else:
            data = enahobygroups[f"{j}g{i + 1}"]

        media = weighted_vals(data["yfam"], pesos=data["factor07"])[0]
        medias.append(media)
        f = data.shape[0]
        fs.append(f)

    fs = [i / sum(fs) for i in fs]

    # media y varianza de ingreso familiar
    if dept is True:
        data2 = enahoyears[str(j)][enahoyears[str(j)]["dept"] == departamentos[dept_i]]
        # print(data2.head())
    else:
        data2 = enahoyears[str(j)]
    media_muestral, var_muestral = weighted_vals(data2["yfam"], pesos=data2["factor07"])

    var_phi = [((medias[i] - media_muestral) ** 2) * fs[i] for i in range(len(grupos2))]
    var_phi = sum(var_phi)

    var_H = var_muestral

    eta = 1 - var_phi / var_H
    etas.append(eta)
    return etas, medias





def porgi():
    enahobygi = {key: value for (key, value) in zip([f"{i}p{j}" for i in periodo_i for j in range(len(gi) - 1)], [enaho[(enaho['aÑo'] == i) & (enaho["gimax"] == gi[j])] for i in periodo_i for j in range(len(gi) - 1)])}

    df_yfam_medio = pd.DataFrame(
        {"Año": periodo_s,
         "0": [round(i) for i in [np.average(enahobygi[f"{i}p0"]["yfam"], weights=enahobygi[f"{i}p0"]["factor07"]) for i in periodo_i]],
         "1": [round(i) for i in [np.average(enahobygi[f"{i}p1"]["yfam"], weights=enahobygi[f"{i}p1"]["factor07"]) for i in periodo_i]],
         "2": [round(i) for i in [np.average(enahobygi[f"{i}p2"]["yfam"], weights=enahobygi[f"{i}p2"]["factor07"]) for i in periodo_i]],
         "3": [round(i) for i in [np.average(enahobygi[f"{i}p3"]["yfam"], weights=enahobygi[f"{i}p3"]["factor07"]) for i in periodo_i]],
         "4": [round(i) for i in [np.average(enahobygi[f"{i}p4"]["yfam"], weights=enahobygi[f"{i}p4"]["factor07"]) for i in periodo_i]],
         "5": [round(i) for i in [np.average(enahobygi[f"{i}p5"]["yfam"], weights=enahobygi[f"{i}p5"]["factor07"]) for i in periodo_i]],
         "6": [round(i) for i in [np.average(enahobygi[f"{i}p6"]["yfam"], weights=enahobygi[f"{i}p6"]["factor07"]) for i in periodo_i]],
         "7": [round(i) for i in [np.average(enahobygi[f"{i}p7"]["yfam"], weights=enahobygi[f"{i}p7"]["factor07"]) for i in periodo_i]],
         "8": [round(i) for i in [np.average(enahobygi[f"{i}p8"]["yfam"], weights=enahobygi[f"{i}p8"]["factor07"]) for i in periodo_i]]})

    # Ingreso medio
    plt.figure(figsize=figsizes)
    for i in range(len(df_yfam_medio.columns) - 1):
        plt.plot(df_yfam_medio["Año"], df_yfam_medio[f"{i}"], label=gi[i].capitalize(), marker=marcadores[i], alpha=0.7, linestyle="dashed")
    plt.plot(df_yfam_medio["Año"], yfam_medio, negro, linewidth=3, label="Ingreso medio", marker="o", alpha=0.6)
    plt.title(f"Ingreso medio familiar por grado de instrucción del padre más instruido del jefe de hogar, {inicio}-{fin}", **fuente)
    plt.xlabel("Año", **fuente)
    plt.ylabel("Ingreso mensual familiar (en soles)", **fuente)
    plt.xticks(**fuente)
    plt.yticks(**fuente)
    plt.ylim([-100, 8200])
    plt.legend(prop=font_manager.FontProperties(family=fuente["fontname"], size=8))
    plt.grid()
    plt.figtext(source_pos[0], source_pos[1], source, **fuente)
    plt.subplots_adjust(bottom=0.12)
    plt.savefig(desktop + f"/imagenes/ingresomediogi.png", bbox_inches='tight')
    # plt.show()
    plt.close()

    f1 = {key: value for (key, value) in zip([f"padre{i}" for i in periodo_i], [[enahoyears[f"{i}"][enahoyears[f"{i}"]["p45_1"] == j]["factor07"].sum() for j in gi[:-1]] for i in periodo_i])}
    f2 = {key: value for (key, value) in zip([f"madre{i}" for i in periodo_i], [[enahoyears[f"{i}"][enahoyears[f"{i}"]["p45_2"] == j]["factor07"].sum() for j in gi[:-1]] for i in periodo_i])}
    frecuencias = f1 | f2

    p1 = {key: value for (key, value) in zip([f"padre{i}" for i in periodo_i], [[round(j*100/sum(frecuencias[f"padre{i}"]), 1) for j in frecuencias[f"padre{i}"]] for i in periodo_i])}
    p2 = {key: value for (key, value) in zip([f"madre{i}" for i in periodo_i], [[round(j*100/sum(frecuencias[f"madre{i}"]), 1) for j in frecuencias[f"madre{i}"]] for i in periodo_i])}
    porcentajes = p1 | p2

    barchars(porcentajes, "gi", gi[:-1])


def porgrupos():

    # Grupo 1: Sin nivel
    g1 = {key: value for (key, value) in zip([f"{i}g1" for i in periodo_i], [enaho[(enaho["aÑo"] == i) & (enaho["gimax"] == gi[0])] for i in periodo_i])}

    # Grupo 2: Educación primaria
    g2 = {key: value for (key, value) in zip([f"{i}g2" for i in periodo_i], [enaho[(enaho["aÑo"] == i) & ((enaho["gimax"] == gi[1]) | (enaho["gimax"] == gi[2]))] for i in periodo_i])}

    # Grupo 3: Educación secundaria
    g3 = {key: value for (key, value) in zip([f"{i}g3" for i in periodo_i], [enaho[(enaho["aÑo"] == i) & ((enaho["gimax"] == gi[3]) | (enaho["gimax"] == gi[4]))] for i in periodo_i])}

    # Grupo 4: Educación superior
    g4 = {key: value for (key, value) in zip([f"{i}g4" for i in periodo_i], [enaho[(enaho["aÑo"] == i) & ((enaho["gimax"] == gi[5]) | (enaho["gimax"] == gi[6]) | (enaho["gimax"] == gi[7]) | (enaho["gimax"] == gi[8]))] for i in periodo_i])}

    enahobygroups = g1 | g2 | g3 | g4

    df_yfam_medio = pd.DataFrame(
        {"Año": periodo_s,
         "0": [round(i) for i in [np.average(enahobygroups[f"{i}g1"]["yfam"], weights=enahobygroups[f"{i}g1"]["factor07"]) for i in periodo_i]],
         "1": [round(i) for i in [np.average(enahobygroups[f"{i}g2"]["yfam"], weights=enahobygroups[f"{i}g2"]["factor07"]) for i in periodo_i]],
         "2": [round(i) for i in [np.average(enahobygroups[f"{i}g3"]["yfam"], weights=enahobygroups[f"{i}g3"]["factor07"]) for i in periodo_i]],
         "3": [round(i) for i in [np.average(enahobygroups[f"{i}g4"]["yfam"], weights=enahobygroups[f"{i}g4"]["factor07"]) for i in periodo_i]]})

    plt.figure(figsize=figsizes)
    for i in range(len(df_yfam_medio.columns) - 1):
        plt.plot(df_yfam_medio["Año"], df_yfam_medio[f"{i}"], label=grupos2[i], marker=marcadores[i], alpha=0.7, linestyle="dashed")
    plt.plot(df_yfam_medio["Año"], yfam_medio, negro, linewidth=3, label="Ingreso medio", marker="o", alpha=0.6)
    plt.title(f"Ingreso medio familiar por grado de instrucción del padre más instruido del jefe de hogar, {inicio}-{fin}", **fuente)
    plt.xlabel("Año", **fuente)
    plt.ylabel("Ingreso mensual familiar (en soles)", **fuente)
    plt.xticks(**fuente)
    plt.yticks(**fuente)
    plt.legend(prop=font_manager.FontProperties(family=fuente["fontname"]))
    plt.ylim([-100, 7100])
    plt.grid()
    plt.figtext(source_pos[0], source_pos[1], source, **fuente)
    plt.subplots_adjust(bottom=0.12)
    plt.savefig(desktop + f"/imagenes/ingresomediogrupos.png", bbox_inches='tight')
    # plt.show()
    plt.close()

    f1 = {key: value for (key, value) in
          zip([f"padre{i}" for i in periodo_i],
              [[enahoyears[f"{i}"][enahoyears[f"{i}"]["p45_1"] == gi[0]]["factor07"].sum(),
                enahoyears[f"{i}"][(enahoyears[f"{i}"]["p45_1"] == gi[1]) | (enahoyears[f"{i}"]["p45_1"] == gi[2])]["factor07"].sum(),
                enahoyears[f"{i}"][(enahoyears[f"{i}"]["p45_1"] == gi[3]) | (enahoyears[f"{i}"]["p45_1"] == gi[4])]["factor07"].sum(),
                enahoyears[f"{i}"][(enahoyears[f"{i}"]["p45_1"] == gi[5]) | (enahoyears[f"{i}"]["p45_1"] == gi[6]) |
                                   (enahoyears[f"{i}"]["p45_1"] == gi[7]) | (enahoyears[f"{i}"]["p45_1"] == gi[8])]["factor07"].sum()]
               for i in periodo_i])}
    f2 = {key: value for (key, value) in
          zip([f"madre{i}" for i in periodo_i],
              [[enahoyears[f"{i}"][enahoyears[f"{i}"]["p45_2"] == gi[0]]["factor07"].sum(),
                enahoyears[f"{i}"][(enahoyears[f"{i}"]["p45_2"] == gi[1]) | (enahoyears[f"{i}"]["p45_2"] == gi[2])]["factor07"].sum(),
                enahoyears[f"{i}"][(enahoyears[f"{i}"]["p45_2"] == gi[3]) | (enahoyears[f"{i}"]["p45_2"] == gi[4])]["factor07"].sum(),
                enahoyears[f"{i}"][(enahoyears[f"{i}"]["p45_2"] == gi[5]) | (enahoyears[f"{i}"]["p45_2"] == gi[6]) |
                                   (enahoyears[f"{i}"]["p45_2"] == gi[7]) | (enahoyears[f"{i}"]["p45_2"] == gi[8])]["factor07"].sum()]
               for i in periodo_i])}
    frecuencias = f1 | f2

    p1 = {key: value for (key, value) in zip([f"padre{i}" for i in periodo_i], [[round(j*100/sum(frecuencias[f"padre{i}"]), 1) for j in frecuencias[f"padre{i}"]] for i in periodo_i])}
    p2 = {key: value for (key, value) in zip([f"madre{i}" for i in periodo_i], [[round(j*100/sum(frecuencias[f"madre{i}"]), 1) for j in frecuencias[f"madre{i}"]] for i in periodo_i])}
    porcentajes = p1 | p2

    barchars(porcentajes, "grupos2", grupos2)

    etas_dep = []
    medias_dep = []
    etas = []
    for j in periodo_i:
        # Función de distribución acumulada (CDF)
        plt.figure(figsize=figsizes)
        for i in range(len(grupos2)):
            data = np.array(enahobygroups[f"{j}g{i + 1}"]["yfam"])
            x = np.sort(data)
            y = np.arange(len(x)) / float(len(x))
            plt.plot(x, y, marker='o', label=grupos2[i], color=colores[i])
        plt.xlabel('Ingreso familiar (en soles)', **fuente)
        plt.ylabel('Probabilidad', **fuente)
        plt.title("Perú: Función de distribución acumulada por grado de instrucción del padre más instruido ($G^t_{\phi}$), " + f"{j}", **fuente)
        plt.xticks(**fuente)
        plt.yticks(**fuente)
        plt.legend(prop=font_manager.FontProperties(family=fuente["fontname"]))
        plt.xlim([0, 10000])
        plt.grid()
        plt.figtext(source_pos[0], source_pos[1], source, **fuente)
        plt.subplots_adjust(bottom=0.12)
        plt.savefig(desktop + f"/imagenes/cdf{j}.png", bbox_inches='tight')
        # plt.show()
        plt.close()

        # Función inversa
        plt.figure(figsize=[figsizes[0], figsizes[1]])
        for i in range(len(grupos2)):
            data = np.array(enahobygroups[f"{j}g{i + 1}"]["yfam"])
            x = np.sort(data)
            y = np.arange(len(x)) / float(len(x))
            plt.plot(y, x, marker='o', label=grupos2[i], color=colores[i])
        plt.xlabel('Grado de esfuerzo ($\pi$)', **fuente)
        plt.ylabel('Ingreso familiar en soles ($v^t$) ', **fuente)
        plt.title(f'Perú: Función del objetivo dada la política: $v^t(\pi, \phi)$, {j}', **fuente)
        plt.xticks(**fuente)
        plt.yticks(**fuente)
        plt.legend(prop=font_manager.FontProperties(family=fuente["fontname"]))
        plt.ylim([0, 20000])
        plt.grid()
        plt.figtext(source_pos[0], source_pos[1], source, **fuente)
        plt.subplots_adjust(bottom=0.12)
        plt.savefig(desktop + f"/imagenes/cdf{j}_2.png", bbox_inches='tight')
        # plt.show()
        plt.close()

        etas = etas_f(enahobygroups, etas, j, departamentos, 1)[0]

        medias_final = []
        dep_final = []
        for h in range(len(departamentos)):
            dep_final, medias_fin = etas_f(enahobygroups, dep_final, j, departamentos, h, dept=True)
            medias_final.append(min(medias_fin))
        etas_dep.append(dep_final)
        medias_dep.append(medias_final)


    medias_dep_df = pd.DataFrame({"2004": medias_dep[0], "2005": medias_dep[1], "2006": medias_dep[2], "2007": medias_dep[3],
                                "2008": medias_dep[4], "2009": medias_dep[5], "2010": medias_dep[6], "2011": medias_dep[7],
                                "2012": medias_dep[8], "2013": medias_dep[9], "2014": medias_dep[10], "2015": medias_dep[11],
                                "2016": medias_dep[12], "2017": medias_dep[13], "2018": medias_dep[14], "2019": medias_dep[15],
                                "2020": medias_dep[16], "2021": medias_dep[17]}, index=departamentos)

    etas_dep_df = pd.DataFrame({"2004": etas_dep[0], "2005": etas_dep[1], "2006": etas_dep[2], "2007": etas_dep[3],
                                "2008": etas_dep[4], "2009": etas_dep[5], "2010": etas_dep[6], "2011": etas_dep[7],
                                "2012": etas_dep[8], "2013": etas_dep[9], "2014": etas_dep[10], "2015": etas_dep[11],
                                "2016": etas_dep[12], "2017": etas_dep[13], "2018": etas_dep[14], "2019": etas_dep[15],
                                "2020": etas_dep[16], "2021": etas_dep[17]}, index=departamentos)

    print(etas_dep_df)
    print(medias_dep_df)

    # resultados = pd.DataFrame({"periodos": periodo_i,
    #                            "etas": etas})

    # sns.regplot(data=resultados, x="periodos", y="etas")
    plt.figure(figsize=(figsizes[0]*1.2, figsizes[1]))
    plt.plot(periodo_s, etas, "black")
    plt.title("Perú: Evolución de los grados de equiparación de oportunidades ($\eta$), 2004-2021", **fuente)
    plt.xlabel('Año', **fuente)
    plt.ylabel('$\eta$', **fuente)
    plt.xticks(**fuente)
    plt.yticks(**fuente)
    plt.ylim([0.85, 1.05])
    plt.figtext(source_pos[0], source_pos[1], source, **fuente)
    plt.subplots_adjust(bottom=0.12)
    plt.grid()
    for x, y in zip(periodo_s, etas):
        label = "{:.5f}".format(y)

        plt.annotate(label, (x, y), xytext=(0, 10),
                     textcoords="offset points", ha='center',
                     arrowprops=dict(arrowstyle="->", color='black'), **fuente)
    plt.savefig(desktop + f"/imagenes/eta.png", bbox_inches='tight')
    # plt.show()
    plt.close()

    for j in periodo_s:
        dataf = pd.DataFrame({"dep": departamentos,
                              "dep_df": etas_dep_df[j]})
        dataf = dataf.sort_values("dep_df")

        plt.figure(figsize=(figsizes[0]*1.2, figsizes[1]*1.5))
        plt.barh(dataf["dep"], dataf["dep_df"], height=.8, align="center", color=(0.2, 0.4, 0.6, 0.6))
        plt.title(f"Perú: Grados de equiparación de oportunidades ($\eta$) por departamentos, {j}", **fuente)
        plt.xlabel('Grado de equiparación de oportunidades: $\eta$', **fuente)
        plt.ylabel('Departamento', **fuente)
        plt.xticks(**fuente)
        plt.yticks(**fuente)
        plt.xlim([0.75, 1.0])
        plt.figtext(source_pos[0], source_pos[1], source, **fuente)
        plt.subplots_adjust(bottom=0.12)
        plt.grid(axis="x")
        plt.savefig(desktop + f"/imagenes/eta{j}.png", bbox_inches='tight')
        # plt.show()
        plt.close()


        m, b = np.polyfit(medias_dep_df[j], etas_dep_df[j], deg=1)

        plt.figure(figsize=(figsizes[0]*1.2, figsizes[1]*1.4))
        plt.scatter(medias_dep_df[j], etas_dep_df[j], color="black")
        for i, txt in enumerate(departamentosISO):
            plt.annotate(txt, (medias_dep_df[j][i], etas_dep_df[j][i]), **fuente)
        plt.plot(medias_dep_df[j], m * medias_dep_df[j] + b, "black", alpha=0.7, linewidth=1.5)
        # Perú: Pares ordenados $d = (\hat{W}_i^{EO}, \eta_i)$ por departamentos y regresión lineal
        plt.title("Perú: Niveles ($\hat{W}_i^{EO}$) y grados ($\eta_i$) de desarrollo por departamentos, " + f"{j}", **fuente)
        plt.xlabel('Nivel de equiparación de oportunidades: $\hat{W}^{EO}$', **fuente)
        plt.ylabel('Grado de equiparación de oportunidades: $\eta$', **fuente)
        plt.xticks(**fuente)
        plt.yticks(**fuente)
        plt.figtext(source_pos[0], source_pos[1], source, **fuente)
        plt.subplots_adjust(bottom=0.12)
        plt.grid()
        plt.savefig(desktop + f"/imagenes/des{j}.png", bbox_inches='tight')
        # plt.show()
        plt.close()




# porgi()
porgrupos()





# sal_min    = [460, 460, 500, 530, 550, 550, 580, 675, 750, 750, 750, 750, 850, 850, 930, 930, 930]
# var_pib_pc = [5.4, 6.7, 7.8, 8.4, 0.4, 7.5, 5.5, 5.4, 5.0, 1.4, 2.1, 2.4, 0.7, 2.0, 0.3, -12.4, 12.1]


# #   Varación media (para el periodo 2004-2020) de la renta per cápita media (por grado de instrucción)
# ypc_media_var_media = [round(sum(ypc_media_var[i])/len(ypc_media_var[i]), 2) for i in range(11)]
#
# etiquetas2 = etiquetas[:-2] + ["media"]
# ypc_media_var_media = ypc_media_var_media[:-2] + [round(sum(ypc_media_var_media)/len(ypc_media_var_media), 2)]
#
# #   grafico de barras crecimiento en los ingresos por grado de instruccion crecimiento promedio 2004-2020
#
# # fig = plt.gcf()
# # fig.set_size_inches(10, 6.5)
# # plt.title("Crecimiento del ingreso medio para el periodo 2004-2020")
# # plt.xlabel("Grado de instrucción")
# # plt.ylabel("Crecimiento % promedio")
# # plt.bar(etiquetas2, ypc_media_var_media, color=[(0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
# #                                                 (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
# #                                                 (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
# #                                                 (0.1, 0.3, 0.6, 0.9)])
# # plt.savefig("C:/Users/pc/Desktop/imagenes/padre_crecimiento_medio1.png")
# # plt.show()
#
#
# x = np.arange(len(etiquetas2))
# width = 0.8
# fig, ax = plt.subplots()
# rects1 = ax.bar(x, ypc_media_var_media, width, color=[(0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
#                                                 (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
#                                                 (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5), (0.1, 0.3, 0.8, 0.5),
#                                                 (0.1, 0.3, 0.6, 0.9)])
# fig.set_size_inches(10, 6.5)
# plt.title("Crecimiento del ingreso medio para el periodo 2004-2020 por grado de instrucción del padre")
# plt.xlabel("Grado de instrucción")
# plt.ylabel("Crecimiento % del ingreso medio")
# ax.set_xticks(x)
# ax.set_xticklabels(etiquetas2)
# ax.bar_label(rects1)
# fig.tight_layout()
# plt.savefig("C:/Users/pc/Desktop/imagenes/padre_crecimiento_medio2.png")
# plt.show()














# var_H = [weighted_vals(pesos=enahobygroups[f"{j}g{i + 1}"]["factor07"]) for i in range(len(grupos2))]
# tam = [enahobygroups[f"{j}g{i + 1}"]["factor07"].sum() for i in range(len(grupos2))]
# var_H = [(((enahobygroups[f"{j}g{i + 1}"]["yfam"] - medias[i])**2)*enahobygroups[f"{j}g{i + 1}"]["factor07"]) for i in range(len(grupos2))]
# var_H = sum([var_H[i].sum()/tam[i] for i in range(len(grupos2))])
# print(var_H)
# #
# sizes = [enahobygroups[f"{j}g{i + 1}"]["yfam"].size for i in range(len(grupos2))]
# wm = [np.average(enahobygroups[f"{j}g{i + 1}"]["yfam"], weights=enahobygroups[f"{j}g{i + 1}"]["factor07"]) for i in range(len(grupos2))]
#
# x1 = enahobygroups[f"{j}g{1}"]["yfam"].iloc[0:min(sizes)].reset_index()["yfam"].to_frame()
# x2 = enahobygroups[f"{j}g{2}"]["yfam"].iloc[0:min(sizes)].reset_index()["yfam"].to_frame()
# x3 = enahobygroups[f"{j}g{3}"]["yfam"].iloc[0:min(sizes)].reset_index()["yfam"].to_frame()
# x4 = enahobygroups[f"{j}g{4}"]["yfam"].iloc[0:min(sizes)].reset_index()["yfam"].to_frame()
#
# w1 = enahobygroups[f"{j}g{1}"]["factor07"].iloc[0:min(sizes)].reset_index()["factor07"].to_frame()
# w2 = enahobygroups[f"{j}g{2}"]["factor07"].iloc[0:min(sizes)].reset_index()["factor07"].to_frame()
# w3 = enahobygroups[f"{j}g{3}"]["factor07"].iloc[0:min(sizes)].reset_index()["factor07"].to_frame()
# w4 = enahobygroups[f"{j}g{4}"]["factor07"].iloc[0:min(sizes)].reset_index()["factor07"].to_frame()
#
# covs = np.average((x1-wm[0])*(x2-wm[1]), axis=0, weights=w1) + \
#        np.average((x1-wm[0])*(x3-wm[2]), axis=0, weights=w1) + \
#        np.average((x1-wm[0])*(x4-wm[3]), axis=0, weights=w1) + \
#        np.average((x2-wm[1])*(x3-wm[2]), axis=0, weights=w2) + \
#        np.average((x2-wm[1])*(x4-wm[3]), axis=0, weights=w2) + \
#        np.average((x3-wm[2])*(x4-wm[3]), axis=0, weights=w3)
#
#
#
# var_H = sum(var_H) + 2*covs

