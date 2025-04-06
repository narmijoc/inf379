import matplotlib.pyplot as plt
import numpy as np

anios = np.array(['03/2021', '06/2021', '09/2021', '12/2021',
         '03/2022', '06/2022', '09/2022', '12/2022', 
         '03/2023', '06/2023', '09/2023', '12/2023', 
         '03/2024' ,'06/2024' ,'09/2024' ,'12/2024'])

# Sectores económicos como porcentaje del PIB
Agropecuario_silvicola = np.array([2752.92, 1666.64, 894.03, 1947.45,
                2656.80, 1470.28, 877.28, 1925.29,
                3072.11, 1852.16, 1055.37, 2526.73,	
                3912.49, 2227.04, 1181.80, 3296.07])

Pesca = np.array([229.12, 300.05, 313.00, 290.46,
        353.58, 510.36, 367.79, 347.95,
        409.57, 486.07, 193.23, 242.21,
        405.25, 519.25, 248.82, 401.41])

mineria = np.array([7544.02, 7672.36, 8425.10, 10040.68, 
           7897.27, 8046.36, 8616.41, 10614.68, 
           7445.87, 6562.36, 7274.40, 8204.11, 
           9085.06, 8672.63, 9171.80, 9670.48])

industria_manufacturera = np.array([4779.12, 4803.22, 5124.19, 5717.15, 
                           5736.00, 5812.23, 6479.87, 6898.58, 
                           6850.17, 5922.74, 6524.63, 7214.92, 
                           7079.88, 6318.73, 7006.47, 7674.33])

consumos_basicos = np.array([1580.70, 1553.73, 1283.77, 1561.77, 
                            1523.71, 1259.40, 1480.76, 1843.88, 
                            1729.06, 2070.92, 2263.82, 2421.76, 
                            2321.14, 2396.20, 2851.75, 3526.34])

construccion = np.array([3348.33, 3148.19, 3491.82, 3810.41, 
                         3751.62, 3592.10, 3888.16, 4196.18, 
                         4129.64, 3904.68, 4194.76, 4469.65, 
                         4475.06, 4213.04, 4520.43, 4773.46])

comercio = np.array([6333.43, 6531.03, 6742.19, 7459.86, 
                     7254.92, 7039.26, 6754.52, 7437.04, 
                     8181.07, 7751.69, 7446.53, 8224.96, 
                     8607.33, 7782.56, 7625.79, 8576.11])

transporte = np.array([2890.87, 2499.19, 2841.47, 3469.58, 
                       3786.51, 3141.79, 2895.77, 2658.85,
                       3868.32, 3993.93, 3560.73, 3879.23, 
                       4350.55, 4174.73, 4078.55, 4879.87])

comunicaciones = np.array([1425.37, 1467.73, 1515.22, 1678.33, 
                           1648.67, 1638.40, 1697.54, 1862.28, 
                           1783.26, 1751.35, 1832.51, 1928.19, 
                           1894.71, 1878.15, 1853.75, 2057.65])

finanzas_empresas = np.array([6864.55, 7004.88, 7326.71, 8032.84, 
                              7855.13, 8163.21, 8432.30, 9300.67, 
                              8788.09, 8882.27, 9319.27, 9968.90, 
                              9555.20, 9836.74, 10109.39, 11336.74])

vivienda = np.array([4404.17, 4389.89, 4619.66, 4887.13, 
                     4988.34, 5123.88, 5226.22, 5411.86, 
                     5481.74, 5548.55, 5492.73, 5777.42, 
                     5751.36, 5853.74, 5870.31, 6196.45])

servicios_personales = np.array([5975.31, 7316.51, 7235.83, 7885.43, 
                                 6879.78, 8236.69, 7867.96, 8725.55, 
                                 7730.98, 9629.41, 8956.30, 9565.39, 
                                 8483.12, 10262.88, 9716.41, 10350.90])

administracion_publica = np.array([2618.22, 2652.99, 2702.42, 2904.67, 
                                   2736.36, 2866.13, 2938.46, 3096.72, 
                                   3108.57, 3233.86, 3276.76, 3395.64, 
                                   3358.65, 3421.08, 3417.08, 3474.91])

impuestos_productos = np.array([5580.88, 5936.62, 6567.45, 7379.47,
                                6568.06, 6509.49, 6733.55, 7442.97, 
                                7051.38, 7062.22, 6800.60, 7564.68, 
                                7252.90, 7534.78, 7691.84, 8447.75])

PIB = Agropecuario_silvicola + Pesca + mineria + industria_manufacturera + consumos_basicos + construccion + comercio + transporte + comunicaciones + finanzas_empresas + vivienda + servicios_personales + administracion_publica + impuestos_productos
# Convertir a array para acumulación
datos = np.vstack([mineria/PIB*100, Agropecuario_silvicola/PIB*100, Pesca/PIB*100, industria_manufacturera/PIB*100, consumos_basicos/PIB*100, construccion/PIB*100, comercio/PIB*100, transporte/PIB*100, comunicaciones/PIB*100, finanzas_empresas/PIB*100, vivienda/PIB*100, servicios_personales/PIB*100, administracion_publica/PIB*100, impuestos_productos/PIB*100])

# Crear gráfico tipo streamgraph
fig, ax = plt.subplots(figsize=(15, 6))
ax.axhline(100, color='gray', linestyle='--', linewidth=0.5)
ax.stackplot(anios, datos, labels=["Minería", "Agropecuario-silvícola", "Pesca", "Industria Manufacturera", "Electricidad, gas, agua y gestión de desechos", "Construcción", "Comercio, restaurantes y hoteles", "Transporte", "Comunicaciones y servicios de información", "Servicios financieros y empresariales", "Servicios de vivienda e inmobiliarios", "Servicios Personales", "Administración Pública", "Impuestos sobre los Productos"],
             colors=["#AA4499", "#D8A7FF","#B39DDB","#9B77CC","#C58BF2","#D6A1E5","#B28DFF","#A288D6","#9F7AEF","#E1B7F5","#D3A2F0","#B87BC6","#C4A4E7","#B2A0D6" ], alpha=0.8)
ax.set_yticks(np.arange(0, 101, 10))
# Personalización
ax.set_title("Contribución de actividades económicas al PIB de Chile", fontsize=14, weight='bold')
ax.set_xlabel("Año")
ax.set_ylabel("Porcentaje del PIB")
ax.set_xticks(anios)
ax.grid(False)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)
plt.tight_layout() 
plt.xticks(rotation=45)
plt.show()