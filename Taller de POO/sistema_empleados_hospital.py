class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nID: {self.id}\nDepartamento: {self.departamento}\nSalario Base: {self.salario_base}")

class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}\nNúmero de Pacientes: {self.num_pacientes}")

class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Turno: {self.turno}\nPlanta: {self.planta}")


medico1 = Medico("Dr. Valencia", "N091", "Cardiología", 5400, "Cardiología", 10)
enfermero1 = Enfermero("Isaac vasquez", "E061", "Urgencias", 5000, "Dia", 3)

medico1.mostrar_info()
enfermero1.mostrar_info()
