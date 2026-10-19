patients_original = ["Amina", "Peter", "Grace", "John", "Maria"]
patients_current = ["Amina", "John", "Maria", "Grace", "Peter"]

patients_current.reverse()
patients_current.append("Maria")
patients_current.remove("Maria")
patients_current.insert(0, "Amina")   
patients_current.pop(4)

print(patients_current)