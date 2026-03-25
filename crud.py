import csv

PATH = "estudiantes.csv"


def buscar_por_id(id):
    with open(PATH, newline="") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if int(line["id"].strip().lower()) == id.strip().lower():
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
    if header is None:
        header = ["id", "nombre", "materia", "nota1", "nota2", "nota3"]

    with open(PATH, "w") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


