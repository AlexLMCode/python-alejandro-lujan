#dics .py

nucleotidos = {
    "A": "Adenina",
    "C": "Citosina",
    "G": "Guanina",
    "T": "Timina"
}

print len(nucleotidos)
print nucleotidos
print nucleotidos["A"]
print nucleotidos["C"]

nucleotidos["A"] = "ADENINA"
nucleotidos["C"] = "CITOSINA"

print nucleotidos

nucleotidos.pop("A", None)
nucleotidos.pop("C", None)
print nucleotidos