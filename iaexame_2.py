import random
from datetime import datetime

def evaluar_consola():
    print("=" * 55)
    print("       SISTEMA DE AUTORIZACIÓN PARA EXAMEN")
    print("=" * 55)

    asistencia = float(input("Ingresa el porcentaje de asistencia: "))
    promedio = float(input("Ingresa el promedio: "))

    proyecto = input("¿Entregó el proyecto? (si/no): ").lower().strip()
    adeudos = input("¿Tiene adeudos? (si/no): ").lower().strip()
    autorizacion = input("¿Tiene autorización especial? (si/no): ").lower().strip()
    lista_oficial = input("¿Aparece en la lista oficial? (si/no): ").lower().strip()
    sistema_dual = input("¿Pertenece al Sistema Dual? (si/no): ").lower().strip()

    # P = Asistencia >= 80%
    # Q = Promedio >= 8
    # R = Proyecto entregado
    # S = Sin adeudos
    # T = Autorización especial
    # U = Aparece en lista oficial (REQUISITO OBLIGATORIO)
    # V = Pertenece al Sistema Dual (PASE AUTOMÁTICO)

    P = asistencia >= 80
    Q = promedio >= 8
    R = proyecto == "si"
    S = adeudos == "no"
    T = autorizacion == "si"
    U = lista_oficial == "si"
    V = sistema_dual == "si"

    no_P = not P
    conjuncion = P and Q
    disyuncion = Q or T
    condicional = (not P) or Q
    bicondicional = P == Q

    resultado = U and (V or (P and Q and R and S) or T)

    print("\n" + "=" * 55)
    print("             VALORES DE LAS PROPOSICIONES")
    print("=" * 55)

    print("P - Asistencia suficiente :", P)
    print("Q - Promedio aprobatorio :", Q)
    print("R - Proyecto entregado   :", R)
    print("S - Sin adeudos          :", S)
    print("T - Autorización especial:", T)
    print("U - Aparece en lista     :", U)
    print("V - Sistema Dual         :", V)

    print("\nNEGACIÓN")
    print("¬P =", no_P)

    print("\nCONJUNCIÓN")
    print("P ∧ Q =", conjuncion)

    print("\nDISYUNCIÓN")
    print("Q ∨ T =", disyuncion)

    print("\nCONDICIONAL")
    print("P → Q =", condicional)

    print("\nBICONDICIONAL")
    print("P ↔ Q =", bicondicional)

    print("\nEXPRESIÓN CON PARÉNTESIS")
    print("U ∧ (V ∨ (P ∧ Q ∧ R ∧ S) ∨ T) =", resultado)

    print("\n" + "=" * 55)
    print("                  RESULTADO FINAL")
    print("=" * 55)

    if not U:
        print("RESULTADO: El alumno NO puede presentar el examen.")
        print("\n[!] IMPORTANTE: No aparece en la lista oficial (U = False).")
        print("    Estar en la lista oficial es un REQUISITO OBLIGATORIO.")
    elif V:
        print("RESULTADO: El alumno PUEDE presentar el examen.")
        print("\n[✓] APROBADO VÍA SISTEMA DUAL: Pasa automáticamente por pertenecer al programa Dual (V = True).")
    elif resultado:
        print("RESULTADO: El alumno PUEDE presentar el examen.")
        print("\n[✓] APROBADO: Cumple con los requisitos académicos u homologación especial.")
    else:
        print("RESULTADO: El alumno NO puede presentar el examen.")
        print("\n[X] RECHAZADO: No cumple con los criterios académicos mínimos ni cuenta con autorización.")

if __name__ == "__main__":
    evaluar_consola()