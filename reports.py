import matplotlib.pyplot as plt
from functools import reduce

def reporte_tiempos_espera(areas):
    tiempos = []
    for area in areas:
        for doctor in area.doctores:
            for paciente in doctor.pacientes_atendidos:
                espera = paciente.tiempo_atencion - paciente.tiempo_llegada
                tiempos.append(espera)
    if tiempos:
        promedio = sum(tiempos) / len(tiempos)
        print(f"Tiempo de espera promedio: {promedio:.2f} unidades de tiempo")
    else:
        print("No hay pacientes atendidos aún.")

def grafico_pacientes_atendidos(areas):
    nombres = []
    cantidades = []
    for area in areas:
        total = reduce(lambda acc, d: acc + len(d.pacientes_atendidos), area.doctores, 0)
        nombres.append(area.nombre)
        cantidades.append(total)
    plt.bar(nombres, cantidades)
    plt.title("Pacientes atendidos por área")
    plt.xlabel("Área")
    plt.ylabel("Cantidad de pacientes")
    plt.show() 