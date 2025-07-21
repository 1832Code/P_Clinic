from models import Area, Doctor
from simulation import simular_llegada_pacientes, simular_atencion
from reports import reporte_tiempos_espera, grafico_pacientes_atendidos
from utils import menu_principal

# Crear áreas y doctores
areas = [Area("Emergencias"), Area("Consulta Externa"), Area("Laboratorio")]
doctores = [Doctor("Dr. Juan", areas[0]), Doctor("Dra. Rosa", areas[1]), Doctor("Dr. Pablo", areas[2])]
areas[0].agregar_doctor(doctores[0])
areas[1].agregar_doctor(doctores[1])
areas[2].agregar_doctor(doctores[2])

tiempo_actual = 0

while True:
    opcion = menu_principal()
    if opcion == "1":
        simular_llegada_pacientes(areas, tiempo_actual)
        print("Llegada de pacientes simulada.")
        tiempo_actual += 1
    elif opcion == "2":
        simular_atencion(areas, tiempo_actual)
        print("Atención de pacientes simulada.")
        tiempo_actual += 1
    elif opcion == "3":
        reporte_tiempos_espera(areas)
    elif opcion == "4":
        grafico_pacientes_atendidos(areas)
    elif opcion == "5":
        print("Saliendo del simulador.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
