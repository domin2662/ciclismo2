
madera = ['m1','m2','m3','m4','m5']
tirador = ['h01','h02','h03']
color_tirador = ['cromo','nickel','balck']
tipo_tir =['largo','corto']
estilo = ['mw12','mw13','mw14','mw15']

comb_totales =[]
comb_parciales =[]

# CARPINTERÍAS

for i in madera:
    for it in tirador:
        for col in color_tirador:
            for tip in tipo_tir:
                for es in estilo:
                    comb_parciales = []
                    comb_parciales.append(i)
                    comb_parciales.append(it)
                    comb_parciales.append(es)
                    comb_parciales.append(col)
                    comb_parciales.append(tip)
                    comb_parciales.sort()
                    if (comb_parciales not in comb_totales ) == True:
                        comb_totales.append(comb_parciales)


print(comb_totales)
print(len(comb_totales))