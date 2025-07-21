import random
from models import Paciente, Doctor, Area

def simular_llegada_pacientes(areas, tiempo_actual, cantidad=5):
    nombres = ["Ana", "Luis", "Pedro", "Maria", "Jose", "Lucia", "Carlos", "Elena"]
    for _ in range(cantidad):
        nombre = random.choice(nombres)
        edad = random.randint(1, 90)
        prioridad = random.choice([1, 2, 3])
        area = random.choice(areas)
        paciente = Paciente(nombre, edad, prioridad, area.nombre, tiempo_actual)
        area.agregar_paciente(paciente)

def simular_atencion(areas, tiempo_actual):
    for area in areas:
        for doctor in area.doctores:
            if area.cola:
                # Atiende al paciente de mayor prioridad (menor número)
                area.cola.sort(key=lambda p: p.prioridad)
                paciente = area.cola.pop(0)
                doctor.atender_paciente(paciente, tiempo_actual) 