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


if edad < 12:
    categoria_edad = "Pediátrico"
    saludo = f"\nHola {nombre}. Te daremos una atención adecuada. (Aviso: Al ser menor de edad, esta consulta debe ser supervisada por un adulto o tutor responsable)."
    nota_edad = "Cuidado Pediátrico: Los niños pueden deshidratarse o empeorar rápidamente. No administre medicamentos sin dosis recetada por un pediatra."
    pregunta_fatiga = "¿El niño/a presenta mucho cansancio, decaimiento o dolor en su cuerpito? (s/n): "
    pregunta_dispnea = "¿Nota que al niño/a le cuesta trabajo respirar, se le hunden las costillas o respira muy rápido? (s/n): "
    
    pregunta_vacunas = input("¿El niño/a tiene al día su esquema de vacunación (Influenza, BCG, Pentavalente/Hexavalente)? (s/n): ").lower().strip()
    if pregunta_vacunas == "n":
        nota_edad_especifica = "Recomendación Pediátrica: Es prioritario acudir a su centro de salud para completar el esquema de vacunación (especialmente Influenza)."

elif 12 <= edad < 18:
    categoria_edad = "Adolescente"
    saludo = f"\nHola, {nombre}. Vamos a revisar tus síntomas. (Recuerda informar a tus padres o tutores sobre cómo te sientes)."
    nota_edad = "Aviso Jóvenes: Si los síntomas interfieren con tus actividades escolares o descanso, avisa a un adulto."
    pregunta_fatiga = "¿Presentas dolor corporal o fatiga intensa? (s/n): "
    pregunta_dispnea = "¿Sientes dificultad para respirar o falta de aire? (s/n): "
    
    if sexo == "F":
        preg_periodo = input("¿Presentas cólicos fuertes, irregularidad o molestias relacionadas con el ciclo menstrual? (s/n): ").lower().strip()
        if preg_periodo == "s":
            nota_sexo_especifica = "Salud Femenina (Adolescencia): Los cólicos intensos (dismenorrea) requieren valoración ginecológica para descartar alteraciones y ajustar analgésicos."

elif 18 <= edad < 65:
    categoria_edad = "Adulto"
    saludo = f"\nEstimado/a {nombre}, vamos a comenzar con la evaluación de sus síntomas."
    nota_edad = "Indicación General: Guarde reposo y evite asistir al trabajo o realizar esfuerzo físico si presenta fiebre."
    pregunta_fatiga = "¿Presenta dolor corporal o fatiga intensa? (s/n): "
    pregunta_dispnea = "¿Sientes dificultad para respirar o falta de aire? (s/n): "

  
    if sexo == "F":
        if 40 <= edad < 50:
            preg_perimenopausia = input("¿Ha experimentado bochornos, cambios de humor o irregularidad menstrual (posible perimenopausia)? (s/n): ").lower().strip()
            if preg_perimenopausia == "s":
                nota_sexo_especifica = "Salud Femenina (Perimenopausia): Consulte con su ginecólogo para evaluar perfil hormonal y pautas para el alivio sintomático."
    
    elif sexo == "M":
        if edad >= 40:
            preg_prostata = input("¿Ha presentado dificultad para orinar, goteo o necesidad de orinar frecuentemente de noche? (s/n): ").lower().strip()
            if preg_prostata == "s":
                nota_sexo_especifica = "Salud Masculina (Urología): Se recomienda realizar chequeo prostático (Antígeno Prostático Específico y/o revisión urológica anual)."

else: 
    categoria_edad = "Adulto Mayor"
    saludo = f"\nEstimado/a {nombre}, es un gusto atenderle. Procederemos a evaluar su estado de salud."
    nota_edad = "Atención Geriátrica: En adultos mayores las infecciones pueden manifestarse sin fiebre alta. Si nota desorientación o debilidad extrema, consulte al médico de inmediato."
    pregunta_fatiga = "¿Siente debilidad extrema, cansancio o dolor en el cuerpo? (s/n): "
    pregunta_dispnea = "¿Sientes dificultad para respirar, opresión o falta de aire? (s/n): "
    
    preg_reuma = input("¿Presenta dolores articulares/reuma o rigidez en las mañanas? (s/n): ").lower().strip()
    if preg_reuma == "s":
        nota_edad_especifica = "Recomendación Gerontológica: Mantenga articulaciones calientes, realice movilidad suave y verifique vacunas de Neumococo e Influenza."

    if sexo == "F":
        preg_menopausia = input("¿Presenta síntomas de menopausia consolidada o resequedad/molestias pélvicas? (s/n): ").lower().strip()
        if preg_menopausia == "s":
            nota_sexo_especifica = "Salud Femenina (Adulto Mayor): Es importante realizar densitometría ósea periódica para prevenir osteopenia u osteoporosis."
    elif sexo == "M":
        preg_prostata_am = input("¿Cuenta con sus revisiones urológicas/prostáticas al día? (s/n): ").lower().strip()
        if preg_prostata_am == "n":
            nota_sexo_especifica = "Salud Masculina: Se aconseja mantener el control prostático de rutina con su médico tratante."

print(saludo)
print("-" * 50)

fiebre = input("¿Tiene fiebre? (s/n): ").lower().strip()
tos = input("¿Tiene tos? (s/n): ").lower().strip()
dolor_garganta = input("¿Tiene dolor de garganta? (s/n): ").lower().strip()
fatiga = input(pregunta_fatiga).lower().strip()
dificultad_respirar = input(pregunta_dispnea).lower().strip()


if dificultad_respirar == "s":
    diagnostico = "EVALUACIÓN CRÍTICA: Síntomas respiratorios graves detectados."
    if edad < 18:
        recomendacion = "Acuda inmediatamente a Urgencias Pediátricas acompañado de un adulto responsable."
    else:
        recomendacion = "Busque atención médica de urgencia inmediatamente o acuda al centro de salud más cercano."

elif fiebre == "s" and tos == "s" and fatiga == "s":
    diagnostico = "POSIBLE SÍNDROME VIRAL O GRIPA: Elevada correlación de síntomas sistémicos."
    recomendacion = "Descanse, manténgase hidratado y consulte a un médico si la fiebre supera los 38.5 °C."

elif fiebre == "s" and tos == "s":
    diagnostico = "POSIBLE INFECCIÓN RESPIRATORIA: Síntomas típicos de bronquitis o infección de vías superiores."
    recomendacion = "Monitoree su temperatura, guarde reposo y programe una consulta médica."

elif tos == "s" and dolor_garganta == "s":
    diagnostico = "POSIBLE IRRITACIÓN O FARINGITIS: Síntomas comunes de resfriado o irritación de la garganta."
    recomendacion = "Mantenga buena hidratación y realice gárgaras. Consulte al médico si el dolor aumenta."

elif fiebre == "s":
    diagnostico = "FIEBRE AISLADA: Síntoma no específico."
    recomendacion = "Monitoree su temperatura durante las próximas 24 a 48 horas. Consulte a un profesional si persiste."

elif tos == "s":
    diagnostico = "TOS AISLADA: Síntoma no específico."
    recomendacion = "Evite cambios bruscos de temperatura y tome líquidos tibios. Consulte al médico si no cede."

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