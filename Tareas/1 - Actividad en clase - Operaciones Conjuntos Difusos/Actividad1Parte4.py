# ==========================
# IMPORTACIONES NECESARIAS
# ==========================
from juzzyPython.generic.Tuple import Tuple
from juzzyPython.generic.Input import Input
from juzzyPython.type1.sets.T1MF_Triangular import T1MF_Triangular
from juzzyPython.type1.sets.T1MF_Trapezoidal import T1MF_Trapezoidal
from juzzyPython.type1.sets.T1MF_Gaussian import T1MF_Gaussian
from juzzyPython.type1.system.T1_Antecedent import T1_Antecedent
from juzzyPython.generic.Plot import Plot

# ==========================
# DEFINICIÓN DE VARIABLES LINGÜÍSTICAS
# ==========================

# Estaturas (en cm)
estaturas = Input("Estaturas", Tuple(0, 210))  # Rango de estatura de 0 a 210 cm

# Edades (en años)
edades = Input("Edades", Tuple(0, 100))  # Rango de edad de 0 a 100 años

# ==========================
# DEFINICIÓN DE CONJUNTOS DIFUSOS (MFs)
# ==========================

# Para Estaturas
bajos_mf = T1MF_Trapezoidal("Bajos", [0, 0, 140, 160])
normales_mf = T1MF_Triangular("Normales", 150, 170, 190)
altos_mf = T1MF_Trapezoidal("Altos", [170, 190, 210, 210])

# Para Edades
jovenes_mf = T1MF_Trapezoidal("Jovenes", [0, 0, 15, 20])
adultos_jovenes_mf = T1MF_Gaussian("Adultos_Jovenes", 20, 5)
adultos_mayores_mf = T1MF_Trapezoidal("Adultos_Mayores", [40, 60, 100, 100])

# ==========================
# ASOCIACIÓN DE MFs A ANTECEDENTES (VARIABLES DIFUSAS)
# ==========================

# Estaturas
bajos = T1_Antecedent(estaturas, bajos_mf, "Estatura baja")
normales = T1_Antecedent(estaturas, normales_mf, "Estatura normal")
altos = T1_Antecedent(estaturas, altos_mf, "Estatura alta")

# Edades
jovenes = T1_Antecedent(edades, jovenes_mf, "Joven")
adultos_jovenes = T1_Antecedent(edades, adultos_jovenes_mf, "Adulto joven")
adultos_mayores = T1_Antecedent(edades, adultos_mayores_mf, "Adulto mayor")

# ==========================
# FUNCIÓN PARA GRAFICAR LOS MF
# ==========================

def plotMF(name, sets, xAxisRange, discretisationLevel):
    """
    Función para graficar los conjuntos difusos (MFs)
    :param name: Título del gráfico
    :param sets: Lista de objetos MF (no Antecedent)
    :param xAxisRange: Tupla con (min, max) del eje X
    :param discretisationLevel: Número de puntos a graficar
    """
    plotter = Plot()  # Crear el graficador
    plotter.figure()
    plotter.title(name)
    for s in sets:
        # Ajustar el soporte del conjunto difuso al rango deseado,
        # de modo que al llamar a plotMF, internamente use este rango.
        s.setSupport(Tuple(xAxisRange[0], xAxisRange[1]))

        # Llamada a plotMF de acuerdo con la firma de tu versión de juzzyPython:
        # plotMF(self, sets, xDisc, yAxisRange, addExtraEndPoints)
        plotter.plotMF(
            s,                         # Conjunto difuso (MF)
            discretisationLevel,       # Número de puntos para discretización
            (0.0, 1.0),                # Rango del eje Y
            True                       # Agregar puntos finales
        )
    plotter.show()

# ==========================
# LLAMADAS A LA FUNCIÓN DE GRAFICACIÓN
# ==========================

# Graficar Estaturas
plotMF("Conjuntos difusos - Estaturas", [bajos_mf, normales_mf, altos_mf], (0, 210), 100)

# Graficar Edades
plotMF("Conjuntos difusos - Edades", [jovenes_mf, adultos_jovenes_mf, adultos_mayores_mf], (0, 100), 100)
