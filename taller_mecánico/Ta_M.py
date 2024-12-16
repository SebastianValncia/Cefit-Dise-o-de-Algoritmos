import sqlite3
import datetime

conn = sqlite3.connect('taller_mecanico.db')
cursor = conn.cursor()

fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')

cursor.execute('''
INSERT INTO Servicios (vehiculo_id, descripcion, fecha_servicio, costo)
VALUES (?, ?, ?, ?)
''', (1, 'Cambio de aceite', fecha_actual, 100.0))
conn.commit()

print("Servicio registrado con fecha actual:", fecha_actual)


def registrar_vehiculo(cliente_id, marca, modelo, ano, placa):
    cursor.execute('''
    INSERT INTO Vehiculos (cliente_id, marca, modelo, ano, placa)
    VALUES (?, ?, ?, ?, ?)
    ''', (cliente_id, marca, modelo, ano, placa))
    conn.commit()
    print("Vehículo registrado exitosamente.")

def programar_servicio(vehiculo_id, descripcion, fecha_servicio, costo):
    cursor.execute('''
    INSERT INTO Servicios (vehiculo_id, descripcion, fecha_servicio, costo)
    VALUES (?, ?, ?, ?)
    ''', (vehiculo_id, descripcion, fecha_servicio, costo))
    conn.commit()
    print("Servicio programado exitosamente.")


def registrar_reparacion(servicio_id, repuesto_id, cantidad):
    cursor.execute('''
    SELECT precio FROM Repuestos WHERE repuesto_id = ?
    ''', (repuesto_id,))

    resultado = cursor.fetchone()

    if resultado is None:
        print(f"Error: El repuesto con ID {repuesto_id} no existe en el inventario.")
        return

    precio = resultado[0]

    costo_total = precio * cantidad

    cursor.execute('''
    INSERT INTO Reparaciones (servicio_id, repuesto_id, cantidad, costo_total)
    VALUES (?, ?, ?, ?)
    ''', (servicio_id, repuesto_id, cantidad, costo_total))
    conn.commit()
    print("Reparación registrada exitosamente.")


def actualizar_inventario(repuesto_id, cantidad):
    cursor.execute('''
    UPDATE Repuestos
    SET cantidad = cantidad + ?
    WHERE repuesto_id = ?
    ''', (cantidad, repuesto_id))
    conn.commit()
    print("Inventario actualizado exitosamente.")

cursor.execute('''
CREATE TRIGGER IF NOT EXISTS actualiza_stock
AFTER INSERT ON Reparaciones
BEGIN
    UPDATE Repuestos
    SET cantidad = cantidad - (SELECT cantidad FROM Reparaciones WHERE reparacion_id = NEW.reparacion_id)
    WHERE repuesto_id = NEW.repuesto_id;
END
''')
conn.commit()

import datetime


def generar_recordatorios():
    hoy = datetime.datetime.now().date()
    cursor.execute('''
    SELECT v.placa, s.fecha_servicio
    FROM Vehiculos v
    JOIN Servicios s ON v.vehiculo_id = s.vehiculo_id
    WHERE s.fecha_servicio <= ?
    ''', (hoy,))
    servicios = cursor.fetchall()

    for servicio in servicios:
        print(f"Recordatorio: Vehículo {servicio[0]} necesita mantenimiento.")

cursor.execute('INSERT INTO Clientes (nombre, telefono, email) VALUES (?, ?, ?)', ('Juan Pérez', '123456789', 'juan@email.com'))
conn.commit()

registrar_vehiculo(1, 'Toyota', 'Corolla', 2015, 'MNU267')

programar_servicio(1, 'Cambio de aceite', '2024-12-20', 100)

registrar_reparacion(1, 1, 2)  # Reemplazo de filtro de aceite

actualizar_inventario(1, -1)

generar_recordatorios()

