import random
from datetime import datetime

# ============================================
# SISTEMA DE CONSULTA MÉDICA EN LÍNEA
# ============================================

print("=== CONSULTA MÉDICA EN LÍNEA ===")
print("Por favor, responda las siguientes preguntas para recibir un diagnóstico preliminar.\n")

nombre = input("Ingrese su nombre completo: ").strip()

while True:
    try:
        edad = int(input("Ingrese su edad (en números): ").strip())
        break
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la edad.")

sexo = input("Ingrese su sexo biológico (M/F/Otro): ").strip().upper()

nota_edad_especifica = ""
nota_sexo_especifica = ""


# P1 = Edad menor a 12 (Pediátrico)
# P2 = Edad entre 12 y 17 (Adolescente)
# P3 = Edad entre 18 y 64 (Adulto)
# P4 = Edad mayor o igual a 65 (Adulto Mayor)
# S1 = Sexo Femenino (F)
# S2 = Sexo Masculino (M)
# A  = Esquema de vacunación incompleto
# B  = Presenta molestias/cólicos del ciclo menstrual
# C  = Presenta síntomas de perimenopausia
# D  = Presenta dificultad o alteración prostática
# E  = Presenta dolores articulares/reuma
# F  = Presenta síntomas de menopausia o molestias pélvicas
# G  = No cuenta con revisiones urológicas al día

P1 = edad < 12
P2 = 12 <= edad < 18
P3 = 18 <= edad < 65
P4 = edad >= 65

S1 = (sexo == "F")
S2 = (sexo == "M")

# Evaluamos P1
if P1:
    categoria_edad = "Pediátrico"
    saludo = f"\nHola {nombre}. Te daremos una atención adecuada. (Aviso: Al ser menor de edad, esta consulta debe ser supervisada por un adulto o tutor responsable)."
    nota_edad = "Cuidado Pediátrico: Los niños pueden deshidratarse o empeorar rápidamente. No administre medicamentos sin dosis recetada por un pediatra."
    pregunta_fatiga = "¿El niño/a presenta mucho cansancio, decaimiento o dolor en su cuerpito? (s/n): "
    pregunta_dispnea = "¿Nota que al niño/a le cuesta trabajo respirar, se le hunden las costillas o respira muy rápido? (s/n): "
    
    A = input("¿El niño/a tiene al día su esquema de vacunación (Influenza, BCG, Pentavalente/Hexavalente)? (s/n): ").lower().strip() == "n"
    # Evaluamos P1 ∧ A
    if A:
        nota_edad_especifica = "Recomendación Pediátrica: Es prioritario acudir a su centro de salud para completar el esquema de vacunación (especialmente Influenza)."

# Evaluamos P2
    categoria_edad = "Adolescente"
    saludo = f"\nHola, {nombre}. Vamos a revisar tus síntomas. (Recuerda informar a tus padres o tutores sobre cómo te sientes)."
    nota_edad = "Aviso Jóvenes: Si los síntomas interfieren con tus actividades escolares o descanso, avisa a un adulto."
    pregunta_fatiga = "¿Presentas dolor corporal o fatiga intensa? (s/n): "
    pregunta_dispnea = "¿Sientes dificultad para respirar o falta de aire? (s/n): "
    
    # Evaluamos P2 ∧ S1
    if S1:
        B = input("¿Presentas cólicos fuertes, irregularidad o molestias relacionadas con el ciclo menstrual? (s/n): ").lower().strip() == "s"
        # Evaluamos P2 ∧ S1 ∧ B
        if B:
            nota_sexo_especifica = "Salud Femenina (Adolescencia): Los cólicos intensos (dismenorrea) requieren valoración ginecológica para descartar alteraciones y ajustar analgésicos."

# Evaluamos P3 
elif P3:
    categoria_edad = "Adulto"
    saludo = f"\nEstimado/a {nombre}, vamos a comenzar con la evaluación de sus síntomas."
    nota_edad = "Indicación General: Guarde reposo y evite asistir al trabajo o realizar esfuerzo físico si presenta fiebre."
    pregunta_fatiga = "¿Presenta dolor corporal o fatiga intensa? (s/n): "
    pregunta_dispnea = "¿Sientes dificultad para respirar o falta de aire? (s/n): "

    # Evaluamos P3 ∧ S1
    if S1:
        if 40 <= edad < 50:
            C = input("¿Ha experimentado bochornos, cambios de humor o irregularidad menstrual (posible perimenopausia)? (s/n): ").lower().strip() == "s"
            # Evaluamos (P3 ∧ S1 ∧ 40 <= edad < 50) ∧ C
            if C:
                nota_sexo_especifica = "Salud Femenina (Perimenopausia): Consulte con su ginecólogo para evaluar perfil hormonal y pautas para el alivio sintomático."
    
    # Evaluamos P3 ∧ S2
    elif S2:
        if edad >= 40:
            D = input("¿Ha presentado dificultad para orinar, goteo o necesidad de orinar frecuentemente de noche? (s/n): ").lower().strip() == "s"
            # Evaluamos (P3 ∧ S2 ∧ edad >= 40) ∧ D
            if D:
                nota_sexo_especifica = "Salud Masculina (Urología): Se recomienda realizar chequeo prostático (Antígeno Prostático Específico y/o revisión urológica anual)."

# Evaluamos P4 
else: 
    categoria_edad = "Adulto Mayor"
    saludo = f"\nEstimado/a {nombre}, es un gusto atenderle. Procederemos a evaluar su estado de salud."
    nota_edad = "Atención Geriátrica: En adultos mayores las infecciones pueden manifestarse sin fiebre alta. Si nota desorientación o debilidad extrema, consulte al médico de inmediato."
    pregunta_fatiga = "¿Siente debilidad extrema, cansancio o dolor en el cuerpo? (s/n): "
    pregunta_dispnea = "¿Sientes dificultad para respirar, opresión o falta de aire? (s/n): "
    
    E = input("¿Presenta dolores articulares/reuma o rigidez en las mañanas? (s/n): ").lower().strip() == "s"
    # Evaluamos P4 ∧ E
    if E:
        nota_edad_especifica = "Recomendación Gerontológica: Mantenga articulaciones calientes, realice movilidad suave y verifique vacunas de Neumococo e Influenza."

    # Evaluamos P4 ∧ S1
    if S1:
        F = input("¿Presenta síntomas de menopausia consolidada o resequedad/molestias pélvicas? (s/n): ").lower().strip() == "s"
        # Evaluamos P4 ∧ S1 ∧ F
        if F:
            nota_sexo_especifica = "Salud Femenina (Adulto Mayor): Es importante realizar densitometría ósea periódica para prevenir osteopenia u osteoporosis."
    
    # Evaluamos P4 ∧ S2
    elif S2:
        G = input("¿Cuenta con sus revisiones urológicas/prostáticas al día? (s/n): ").lower().strip() == "n"
        # Evaluamos P4 ∧ S2 ∧ G
        if G:
            nota_sexo_especifica = "Salud Masculina: Se aconseja mantener el control prostático de rutina con su médico tratante."

print(saludo)
print("-" * 50)


# H = El paciente presenta fiebre
# I = El paciente presenta tos
# J = El paciente presenta dolor de garganta
# K = El paciente presenta fatiga / dolor corporal
# L = El paciente presenta dificultad para respirar (Dispnea)
# M = Paciente es menor de edad (edad < 18)

H = input("¿Tiene fiebre? (s/n): ").lower().strip() == "s"
I = input("¿Tiene tos? (s/n): ").lower().strip() == "s"
J = input("¿Tiene dolor de garganta? (s/n): ").lower().strip() == "s"
K = input(pregunta_fatiga).lower().strip() == "s"
L = input(pregunta_dispnea).lower().strip() == "s"

M = (edad < 18)

# Evaluamos L 
if L:
    diagnostico = "EVALUACIÓN CRÍTICA: Síntomas respiratorios graves detectados."
    # Evaluamos L ∧ M
    if M:
        recomendacion = "Acuda inmediatamente a Urgencias Pediátricas acompañado de un adulto responsable."
    # Evaluamos L ∧ ¬M
    else:
        recomendacion = "Busque atención médica de urgencia inmediatamente o acuda al centro de salud más cercano."

# Evaluamos ¬L ∧ (H ∧ I ∧ K)
elif H and I and K:
    diagnostico = "POSIBLE SÍNDROME VIRAL O GRIPA: Elevada correlación de síntomas sistémicos."
    recomendacion = "Descanse, manténgase hidratado y consulte a un médico si la fiebre supera los 38.5 °C."

# Evaluamos ¬L ∧ ¬(H ∧ I ∧ K) ∧ (H ∧ I)
elif H and I:
    diagnostico = "POSIBLE INFECCIÓN RESPIRATORIA: Síntomas típicos de bronquitis o infección de vías superiores."
    recomendacion = "Monitoree su temperatura, guarde reposo y programe una consulta médica."

# Evaluamos ¬L ∧ ¬(H ∧ I) ∧ (I ∧ J)
elif I and J:
    diagnostico = "POSIBLE IRRITACIÓN O FARINGITIS: Síntomas comunes de resfriado o irritación de la garganta."
    recomendacion = "Mantenga buena hidratación y realice gárgaras. Consulte al médico si el dolor aumenta."

# Evaluamos H ∧ ¬L ∧ ¬I
elif H:
    diagnostico = "FIEBRE AISLADA: Síntoma no específico."
    recomendacion = "Monitoree su temperatura durante las próximas 24 a 48 horas. Consulte a un profesional si persiste."

# Evaluamos I ∧ ¬L ∧ ¬H ∧ ¬J
elif I:
    diagnostico = "TOS AISLADA: Síntoma no específico."
    recomendacion = "Evite cambios bruscos de temperatura y tome líquidos tibios. Consulte al médico si no cede."

# Evaluamos ¬H ∧ ¬I ∧ ¬J ∧ ¬K ∧ ¬L
else:
    diagnostico = "NO SE IDENTIFICÓ UN PATRÓN ESPECÍFICO."
    recomendacion = "No se detectaron patrones virales principales. Si continúa sintiéndose mal, solicite una valoración médica."

id_consulta = f"MED-{random.randint(10000, 99999)}"
fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print("\n" + "=" * 55)
print("             REPORTE DE CONSULTA MÉDICA          ")
print("=" * 55)
print(f"Fecha y Hora : {fecha_actual}")
print(f"ID Consulta  : {id_consulta}")
print("-" * 55)
print(f"Paciente     : {nombre}")
print(f"Edad         : {edad} años ({categoria_edad})")
print(f"Sexo         : {sexo}")
print("-" * 55)
print(f"Diagnóstico  : {diagnostico}")
print(f"Indicación   : {recomendacion}")
print("-" * 55)
print(f"Observación  : {nota_edad}")
if nota_edad_especifica:
    print(f"Adicional (Edad) : {nota_edad_especifica}")
if nota_sexo_especifica:
    print(f"Adicional (Sexo) : {nota_sexo_especifica}")
print("=" * 55)
print("Aviso: Este sistema proporciona orientación preliminar automatizada")
print("y no sustituye la valoración de un profesional de la salud.")