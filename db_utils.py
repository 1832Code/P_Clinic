from db_config import get_connection

# CRUD para Áreas

def crear_area(nombre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO areas (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_areas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM areas")
    areas = cursor.fetchall()
    cursor.close()
    conn.close()
    return areas

def actualizar_area(area_id, nuevo_nombre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE areas SET nombre=%s WHERE id=%s", (nuevo_nombre, area_id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_area(area_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM areas WHERE id=%s", (area_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD para Doctores

def crear_doctor(nombre, area_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doctores (nombre, area_id) VALUES (%s, %s)", (nombre, area_id))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_doctores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctores")
    doctores = cursor.fetchall()
    cursor.close()
    conn.close()
    return doctores

def actualizar_doctor(doctor_id, nuevo_nombre, nuevo_area_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE doctores SET nombre=%s, area_id=%s WHERE id=%s", (nuevo_nombre, nuevo_area_id, doctor_id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_doctor(doctor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM doctores WHERE id=%s", (doctor_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD para Pacientes

def crear_paciente(nombre, edad, prioridad, area_id, tiempo_llegada, tiempo_atencion=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pacientes (nombre, edad, prioridad, area_id, tiempo_llegada, tiempo_atencion)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, edad, prioridad, area_id, tiempo_llegada, tiempo_atencion))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_pacientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return pacientes

def actualizar_paciente(paciente_id, nuevo_nombre, nueva_edad, nueva_prioridad, nuevo_area_id, nuevo_tiempo_llegada):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE pacientes SET nombre=%s, edad=%s, prioridad=%s, area_id=%s, tiempo_llegada=%s WHERE id=%s", (nuevo_nombre, nueva_edad, nueva_prioridad, nuevo_area_id, nuevo_tiempo_llegada, paciente_id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_paciente(paciente_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id=%s", (paciente_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD para Atenciones

def crear_atencion(paciente_id, doctor_id, tiempo_atencion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO atenciones (paciente_id, doctor_id, tiempo_atencion)
        VALUES (%s, %s, %s)
    """, (paciente_id, doctor_id, tiempo_atencion))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_atenciones():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM atenciones")
    atenciones = cursor.fetchall()
    cursor.close()
    conn.close()
    return atenciones

def actualizar_atencion(atencion_id, nuevo_paciente_id, nuevo_doctor_id, nuevo_tiempo_atencion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE atenciones SET paciente_id=%s, doctor_id=%s, tiempo_atencion=%s WHERE id=%s", (nuevo_paciente_id, nuevo_doctor_id, nuevo_tiempo_atencion, atencion_id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_atencion(atencion_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM atenciones WHERE id=%s", (atencion_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD para Usuarios

def crear_usuario(nombre, email, password_hash):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, password_hash) VALUES (%s, %s, %s)", (nombre, email, password_hash))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_usuario_por_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario

def actualizar_usuario(usuario_id, nuevo_nombre, nuevo_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s", (nuevo_nombre, nuevo_email, usuario_id))
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_password(usuario_id, nuevo_password_hash):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET password_hash=%s WHERE id=%s", (nuevo_password_hash, usuario_id))
    conn.commit()
    cursor.close()
    conn.close() 