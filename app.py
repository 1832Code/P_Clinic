from flask import Flask, render_template, redirect, url_for, request, session, flash, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from db_utils import crear_usuario, obtener_usuario_por_email, obtener_areas, obtener_doctores, obtener_pacientes, obtener_atenciones, actualizar_usuario, actualizar_password, crear_area, crear_doctor, crear_paciente, crear_atencion, actualizar_area, eliminar_area, actualizar_doctor, eliminar_doctor, actualizar_paciente, eliminar_paciente, actualizar_atencion, eliminar_atencion
from functools import wraps
import io
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = 'supersecretkeysupersecretkeysupersecretkeyhellowordtodocodewelcometoday'  
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/areas', methods=['GET', 'POST'])
@login_required
def areas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        crear_area(nombre)
        flash('Área creada exitosamente.', 'success')
        return redirect(url_for('areas'))
    lista_areas = obtener_areas()
    return render_template('areas.html', areas=lista_areas)

@app.route('/areas/editar/<int:area_id>', methods=['POST'])
@login_required
def editar_area(area_id):
    nuevo_nombre = request.form['nuevo_nombre']
    actualizar_area(area_id, nuevo_nombre)
    flash('Área actualizada exitosamente.', 'success')
    return redirect(url_for('areas'))

@app.route('/areas/eliminar/<int:area_id>', methods=['POST'])
@login_required
def eliminar_area_route(area_id):
    eliminar_area(area_id)
    flash('Área eliminada exitosamente.', 'success')
    return redirect(url_for('areas'))

@app.route('/doctores', methods=['GET', 'POST'])
@login_required
def doctores():
    if request.method == 'POST':
        nombre = request.form['nombre']
        area_id = request.form['area_id']
        crear_doctor(nombre, area_id)
        flash('Doctor creado exitosamente.', 'success')
        return redirect(url_for('doctores'))
    lista_doctores = obtener_doctores()
    lista_areas = {a['id']: a['nombre'] for a in obtener_areas()}
    return render_template('doctores.html', doctores=lista_doctores, areas=lista_areas)

@app.route('/doctores/editar/<int:doctor_id>', methods=['POST'])
@login_required
def editar_doctor(doctor_id):
    nuevo_nombre = request.form['nuevo_nombre']
    nuevo_area_id = request.form['nuevo_area_id']
    actualizar_doctor(doctor_id, nuevo_nombre, nuevo_area_id)
    flash('Doctor actualizado exitosamente.', 'success')
    return redirect(url_for('doctores'))

@app.route('/doctores/eliminar/<int:doctor_id>', methods=['POST'])
@login_required
def eliminar_doctor_route(doctor_id):
    eliminar_doctor(doctor_id)
    flash('Doctor eliminado exitosamente.', 'success')
    return redirect(url_for('doctores'))

@app.route('/pacientes', methods=['GET', 'POST'])
@login_required
def pacientes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        prioridad = request.form['prioridad']
        area_id = request.form['area_id']
        tiempo_llegada = request.form['tiempo_llegada']
        crear_paciente(nombre, edad, prioridad, area_id, tiempo_llegada)
        flash('Paciente creado exitosamente.', 'success')
        return redirect(url_for('pacientes'))
    lista_pacientes = obtener_pacientes()
    lista_areas = {a['id']: a['nombre'] for a in obtener_areas()}
    return render_template('pacientes.html', pacientes=lista_pacientes, areas=lista_areas)

@app.route('/pacientes/editar/<int:paciente_id>', methods=['POST'])
@login_required
def editar_paciente(paciente_id):
    nuevo_nombre = request.form['nuevo_nombre']
    nueva_edad = request.form['nueva_edad']
    nueva_prioridad = request.form['nueva_prioridad']
    nuevo_area_id = request.form['nuevo_area_id']
    nuevo_tiempo_llegada = request.form['nuevo_tiempo_llegada']
    actualizar_paciente(paciente_id, nuevo_nombre, nueva_edad, nueva_prioridad, nuevo_area_id, nuevo_tiempo_llegada)
    flash('Paciente actualizado exitosamente.', 'success')
    return redirect(url_for('pacientes'))

@app.route('/pacientes/eliminar/<int:paciente_id>', methods=['POST'])
@login_required
def eliminar_paciente_route(paciente_id):
    eliminar_paciente(paciente_id)
    flash('Paciente eliminado exitosamente.', 'success')
    return redirect(url_for('pacientes'))

@app.route('/atenciones', methods=['GET', 'POST'])
@login_required
def atenciones():
    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        doctor_id = request.form['doctor_id']
        tiempo_atencion = request.form['tiempo_atencion']
        crear_atencion(paciente_id, doctor_id, tiempo_atencion)
        flash('Atención registrada exitosamente.', 'success')
        return redirect(url_for('atenciones'))
    lista_atenciones = obtener_atenciones()
    lista_pacientes = {p['id']: p['nombre'] for p in obtener_pacientes()}
    lista_doctores = {d['id']: d['nombre'] for d in obtener_doctores()}
    return render_template('atenciones.html', atenciones=lista_atenciones, pacientes=lista_pacientes, doctores=lista_doctores)

@app.route('/atenciones/editar/<int:atencion_id>', methods=['POST'])
@login_required
def editar_atencion(atencion_id):
    nuevo_paciente_id = request.form['nuevo_paciente_id']
    nuevo_doctor_id = request.form['nuevo_doctor_id']
    nuevo_tiempo_atencion = request.form['nuevo_tiempo_atencion']
    actualizar_atencion(atencion_id, nuevo_paciente_id, nuevo_doctor_id, nuevo_tiempo_atencion)
    flash('Atención actualizada exitosamente.', 'success')
    return redirect(url_for('atenciones'))

@app.route('/atenciones/eliminar/<int:atencion_id>', methods=['POST'])
@login_required
def eliminar_atencion_route(atencion_id):
    eliminar_atencion(atencion_id)
    flash('Atención eliminada exitosamente.', 'success')
    return redirect(url_for('atenciones'))

@app.route('/configuracion', methods=['GET', 'POST'])
@login_required
def configuracion():
    usuario = {
        'id': session['usuario_id'],
        'nombre': session['usuario_nombre'],
        'email': session['usuario_email']
    }
    if request.method == 'POST':
        if 'actualizar_info' in request.form:
            nuevo_nombre = request.form['nombre']
            nuevo_email = request.form['email']
            actualizar_usuario(usuario['id'], nuevo_nombre, nuevo_email)
            session['usuario_nombre'] = nuevo_nombre
            session['usuario_email'] = nuevo_email
            flash('Información actualizada.', 'success')
        elif 'cambiar_password' in request.form:
            nueva_password = request.form['nueva_password']
            actualizar_password(usuario['id'], generate_password_hash(nueva_password))
            flash('Contraseña actualizada.', 'success')
    return render_template('configuracion.html', usuario=usuario)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        if obtener_usuario_por_email(email):
            flash('El email ya está registrado.', 'danger')
            return redirect(url_for('register'))
        password_hash = generate_password_hash(password)
        crear_usuario(nombre, email, password_hash)
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = obtener_usuario_por_email(email)
        if usuario and check_password_hash(usuario['password_hash'], password):
            session['usuario_id'] = usuario['id']
            session['usuario_nombre'] = usuario['nombre']
            session['usuario_email'] = usuario['email']
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('login'))

@app.route('/reportes')
@login_required
def reportes():
    # Indicadores
    pacientes = obtener_pacientes()
    atenciones = obtener_atenciones()
    total_atenciones = len(atenciones)
    tiempos_espera = [p['tiempo_atencion'] - p['tiempo_llegada'] for p in pacientes if p['tiempo_atencion'] is not None and p['tiempo_llegada'] is not None]
    tiempo_espera_prom = round(sum(tiempos_espera)/len(tiempos_espera), 2) if tiempos_espera else 0
    return render_template('reportes.html', total_atenciones=total_atenciones, tiempo_espera_prom=tiempo_espera_prom)

@app.route('/grafico/atendidos_por_area.png')
@login_required
def grafico_atendidos_por_area():
    areas = obtener_areas()
    atenciones = obtener_atenciones()
    doctores = obtener_doctores()
    area_id_to_nombre = {a['id']: a['nombre'] for a in areas}
    doctor_id_to_area = {d['id']: d['area_id'] for d in doctores}
    conteo = {a['nombre']: 0 for a in areas}
    for at in atenciones:
        area_id = doctor_id_to_area.get(at['doctor_id'])
        if area_id:
            nombre_area = area_id_to_nombre.get(area_id, 'Desconocido')
            conteo[nombre_area] += 1
    fig, ax = plt.subplots()
    ax.bar(conteo.keys(), conteo.values(), color='skyblue')
    ax.set_title('Pacientes atendidos por área')
    ax.set_xlabel('Área')
    ax.set_ylabel('Cantidad')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/grafico/prioridades.png')
@login_required
def grafico_prioridades():
    pacientes = obtener_pacientes()
    prioridades = {'Alta': 0, 'Media': 0, 'Baja': 0}
    for p in pacientes:
        if p['prioridad'] == 1 or p['prioridad'] == '1':
            prioridades['Alta'] += 1
        elif p['prioridad'] == 2 or p['prioridad'] == '2':
            prioridades['Media'] += 1
        elif p['prioridad'] == 3 or p['prioridad'] == '3':
            prioridades['Baja'] += 1
    fig, ax = plt.subplots()
    ax.pie(prioridades.values(), labels=prioridades.keys(), autopct='%1.1f%%', startangle=90)
    ax.set_title('Distribución de prioridades de pacientes')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/grafico/atenciones_por_doctor.png')
@login_required
def grafico_atenciones_por_doctor():
    doctores = obtener_doctores()
    atenciones = obtener_atenciones()
    doctor_id_to_nombre = {d['id']: d['nombre'] for d in doctores}
    conteo = {d['nombre']: 0 for d in doctores}
    for at in atenciones:
        nombre_doctor = doctor_id_to_nombre.get(at['doctor_id'], 'Desconocido')
        conteo[nombre_doctor] += 1
    fig, ax = plt.subplots()
    ax.bar(conteo.keys(), conteo.values(), color='orange')
    ax.set_title('Atenciones por doctor')
    ax.set_xlabel('Doctor')
    ax.set_ylabel('Cantidad')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/grafico/pacientes_estado.png')
@login_required
def grafico_pacientes_estado():
    pacientes = obtener_pacientes()
    atendidos = sum(1 for p in pacientes if p['tiempo_atencion'] is not None)
    pendientes = sum(1 for p in pacientes if p['tiempo_atencion'] is None)
    labels = ['Atendidos', 'Pendientes']
    sizes = [atendidos, pendientes]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#4CAF50', '#FFC107'], startangle=90)
    ax.set_title('Pacientes por estado de atención')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/grafico/pacientes_por_area.png')
@login_required
def grafico_pacientes_por_area():
    areas = obtener_areas()
    pacientes = obtener_pacientes()
    area_id_to_nombre = {a['id']: a['nombre'] for a in areas}
    conteo = {a['nombre']: 0 for a in areas}
    for p in pacientes:
        nombre_area = area_id_to_nombre.get(p['area_id'], 'Desconocido')
        conteo[nombre_area] += 1
    fig, ax = plt.subplots()
    ax.bar(conteo.keys(), conteo.values(), color='purple')
    ax.set_title('Pacientes por área')
    ax.set_xlabel('Área')
    ax.set_ylabel('Cantidad')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True) 