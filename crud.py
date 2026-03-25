import csv

PATH = "estudiantes.csv"


def buscar_por_id(id: int):
    with open(PATH, newline="") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if int(line["id"].strip().lower()) == id:
                return line
        return None


def agregar(nombre, materia, nota1, nota2, nota3):
    with open(PATH) as file:
        lines = list(csv.DictReader(file))
        ultimo = int(lines[len(lines) - 1]["id"])

    with open(PATH, "a", newline="") as file:
        csv.writer(file).writerow(
            ["0" + str(ultimo + 1), nombre, materia, nota1, nota2, nota3]
        )


def editar(id, nombre=None, materia=None, nota1=None, nota2=None, nota3=None):
    with open(PATH) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        rows = []
        for persona in reader:
            if int(persona["id"]) == id:
                if nombre != None:
                    persona["nombre"] = nombre
                if materia != None:
                    persona["materia"] = materia
                if nota1 != None:
                    persona["nota1"] = nota1
                if nota2 != None:
                    persona["nota2"] = nota2
                if nota3 != None:
                    persona["nota3"] = nota3
            rows.append(persona)
    set_header(header)
    write_file(header, rows)


def eliminar(id: int):
    with open(PATH) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        rows = []
        for line in reader:
            if int(line["id"]) == id:
                continue
            rows.append(line)
    set_header()
    write_file(header, rows)


def write_file(header, rows):
    with open(PATH, "w") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def calcular_promedio_todos():
    with open(PATH) as file:
        reader = csv.DictReader(file)
        for line in reader:
            promedio = (
                float(line["nota1"]) + float(line["nota2"]) + float(line["nota3"])
            ) / 3
            print(f"{line["id"]} - {line["nombre"]} - promedio: {promedio:.2f}")


def calcular_promedio_id(id: int):
    estudiante = buscar_por_id(id)
    if estudiante is None:
        return None
    promedio = (
        float(estudiante["nota1"])
        + float(estudiante["nota2"])
        + float(estudiante["nota3"])
    ) / 3
    return f"{estudiante['id']} -  nombre: {estudiante["nombre"]} - materia: {estudiante["materia"]} - promedio: {promedio:.2f}"


print(calcular_promedio_id(1))


def set_header(header):
    if header is None:
        header = ["id", "nombre", "materia", "nota1", "nota2", "nota3"]
