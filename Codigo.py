from flask import Flask, render_template, request, redirect
from Inicio import conectar_bd
from datetime import datetime

app = Flask(__name__)

#RUTAS PRINCIPALES

@app.route('/')
def index():
    """Dashboard principal del sistema"""
    conexion = conectar_bd()
    total_pacientes = 0
    total_medicos = 0
    
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) as total FROM pacientes")
        total_pacientes = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) as total FROM medicos")
        total_medicos = cursor.fetchone()[0]
        cursor.close()
        conexion.close()
    
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return render_template('menu.html', 
                         total_pacientes=total_pacientes, 
                         total_medicos=total_medicos,
                         fecha_actual=fecha_actual)

#RUTAS DE PACIENTES

@app.route('/paciente')
def formulario_paciente():
    """Muestra el formulario para registrar nuevo paciente"""
    return render_template('paciente.html')

@app.route('/guardar_paciente', methods=['POST'])
def guardar_paciente():
    """Guarda los datos del nuevo paciente en la BD"""
    if request.method == 'POST':
        nombre_apellido = request.form.get('nombre_apellido')
        dni = request.form.get('dni')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        edad = request.form.get('edad')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        obra_social = request.form.get('obra_social')
        grupo_sanguineo = request.form.get('grupo_sanguineo')
        alergias = request.form.get('alergias')
        antecedentes = request.form.get('antecedentes')
        
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = """INSERT INTO pacientes 
                     (nombre_apellido, dni, fecha_nacimiento, edad, direccion, 
                      telefono, obra_social, grupo_sanguineo, alergias, antecedentes) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            valores = (nombre_apellido, dni, fecha_nacimiento, edad, direccion, 
                      telefono, obra_social, grupo_sanguineo, alergias, antecedentes)
            
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            
    return redirect('/lista_pacientes')

@app.route('/lista_pacientes')
def lista_pacientes():
    """Muestra el historial de todos los pacientes"""
    conexion = conectar_bd()
    pacientes = []
    
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes ORDER BY historia_clinica DESC")
        pacientes = cursor.fetchall()
        cursor.close()
        conexion.close()
    
    return render_template('historial.html', pacientes=pacientes)

@app.route('/editar_paciente/<int:id>')
def editar_paciente(id):
    """Muestra el formulario de edición de paciente con sus datos"""
    conexion = conectar_bd()
    paciente = None
    
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes WHERE historia_clinica = %s", (id,))
        paciente = cursor.fetchone()
        cursor.close()
        conexion.close()
        
    if paciente:
        return render_template('datos_pacientes.html', paciente=paciente)
    else:
        return "Paciente no encontrado", 404

@app.route('/actualizar_paciente', methods=['POST'])
def actualizar_paciente():
    """Actualiza los datos del paciente en la BD"""
    if request.method == 'POST':
        historia_clinica = request.form.get('historia_clinica')
        nombre_apellido = request.form.get('nombre_apellido')
        dni = request.form.get('dni')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        edad = request.form.get('edad')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        obra_social = request.form.get('obra_social')
        grupo_sanguineo = request.form.get('grupo_sanguineo')
        alergias = request.form.get('alergias')
        antecedentes = request.form.get('antecedentes')
        
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = """UPDATE pacientes SET 
                     nombre_apellido=%s, dni=%s, fecha_nacimiento=%s, edad=%s, 
                     direccion=%s, telefono=%s, obra_social=%s, grupo_sanguineo=%s, 
                     alergias=%s, antecedentes=%s 
                     WHERE historia_clinica=%s"""
            
            valores = (nombre_apellido, dni, fecha_nacimiento, edad, direccion, 
                       telefono, obra_social, grupo_sanguineo, alergias, antecedentes, historia_clinica)
            
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            
    return redirect('/lista_pacientes')

#RUTAS DE MÉDICOS

@app.route('/medico')
def formulario_medico():
    """Muestra el formulario para registrar nuevo médico"""
    return render_template('medico.html')

@app.route('/guardar_medico', methods=['POST'])
def guardar_medico():
    """Guarda los datos del nuevo médico en la BD"""
    if request.method == 'POST':
        nombre_apellido = request.form.get('nombre_apellido_med')
        dni = request.form.get('dni_med')
        telefono = request.form.get('telefono_med')
        email = request.form.get('email_med')
        matricula = request.form.get('matricula')
        especialidad = request.form.get('especialidad')
        dias_atencion = request.form.get('dias_atencion', '')
        
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = """INSERT INTO medicos 
                     (nombre_apellido, dni, telefono, email, matricula, especialidad, dias_atencion) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            
            valores = (nombre_apellido, dni, telefono, email, matricula, especialidad, dias_atencion)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            
    return redirect('/lista_medicos')

@app.route('/lista_medicos')
def lista_medicos():
    """Muestra el listado de todos los médicos"""
    conexion = conectar_bd()
    medicos = []
    
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medicos ORDER BY id_medico DESC")
        medicos = cursor.fetchall()
        cursor.close()
        conexion.close()
    
    return render_template('lista_medicos.html', medicos=medicos)

@app.route('/editar_medico/<int:id>')
def editar_medico(id):
    """Muestra el formulario de edición de médico con sus datos"""
    conexion = conectar_bd()
    medico = None
    
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medicos WHERE id_medico = %s", (id,))
        medico = cursor.fetchone()
        cursor.close()
        conexion.close()
        
    if medico:
        return render_template('datos_medicos.html', medico=medico)
    else:
        return "Médico no encontrado", 404

@app.route('/actualizar_medico', methods=['POST'])
def actualizar_medico():
    """Actualiza los datos del médico en la BD"""
    if request.method == 'POST':
        id_medico = request.form.get('id_medico')
        nombre_apellido = request.form.get('nombre_apellido_med')
        dni = request.form.get('dni_med')
        telefono = request.form.get('telefono_med')
        email = request.form.get('email_med')
        matricula = request.form.get('matricula')
        especialidad = request.form.get('especialidad')
        dias_atencion = request.form.get('dias_atencion', '')
        
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = """UPDATE medicos SET 
                     nombre_apellido=%s, dni=%s, telefono=%s, email=%s, 
                     matricula=%s, especialidad=%s, dias_atencion=%s 
                     WHERE id_medico=%s"""
            
            valores = (nombre_apellido, dni, telefono, email, matricula, especialidad, dias_atencion, id_medico)
            
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            
    return redirect('/lista_medicos')

if __name__ == '__main__':
    app.run(debug=True)