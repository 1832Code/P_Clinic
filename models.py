class Paciente:
    def __init__(self, nombre, edad, prioridad, area_destino, tiempo_llegada):
        self.nombre = nombre
        self.edad = edad
        self.prioridad = prioridad  # 1=alta, 2=media, 3=baja
        self.area_destino = area_destino
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_atencion = None

    def __repr__(self):
        return f"Paciente({self.nombre}, Prioridad: {self.prioridad}, Area: {self.area_destino})"

class Doctor:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.pacientes_atendidos = []

    def atender_paciente(self, paciente, tiempo_actual):
        paciente.tiempo_atencion = tiempo_actual
        self.pacientes_atendidos.append(paciente)

    def __repr__(self):
        return f"Doctor({self.nombre}, Area: {self.area})"

class Area:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola = []  # Lista de pacientes
        self.doctores = []

    def agregar_paciente(self, paciente):
        self.cola.append(paciente)

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def __repr__(self):
        return f"Area({self.nombre}, Doctores: {len(self.doctores)}, Pacientes en cola: {len(self.cola)})" 