class Patient:
    def __init__(self, patient_id, name, treatment_cost, category="General"):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category

    def __str__(self):
        return (
            f"ID: {self.patient_id} | Name: {self.name} | "
            f"Category: {self.category} | Cost: ₹{self.treatment_cost}"
        )


class GeneralPatient(Patient):
    def __init__(self, patient_id, name, treatment_cost):
        super().__init__(patient_id, name, treatment_cost, category="General")


class SpecialPatient(Patient):
    def __init__(self, patient_id, name, treatment_cost, ward_type="ICU"):
        super().__init__(patient_id, name, treatment_cost, category="Special")
        self.ward_type = ward_type

    def __str__(self):
        return f"{super().__str__()} | Ward: {self.ward_type}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_records(self):
        print(f"--- {self.name} Patient Records ---")
        if not self.patients:
            print("No records found.")
            return
        for p in self.patients:
            print(p)


if __name__ == "__main__":
    hospital = Hospital("City Care Hospital")

    p1 = GeneralPatient("P101", "Aarav Sharma", 3500)
    p2 = SpecialPatient("P102", "Neha Kulkarni", 18500, ward_type="ICU")
    p3 = GeneralPatient("P103", "Rohan Deshmukh", 2200)

    hospital.add_patient(p1)
    hospital.add_patient(p2)
    hospital.add_patient(p3)

    hospital.display_records()

#OUTPUT
#--- City Care Hospital Patient Records ---
#ID: P101 | Name: Aarav Sharma | Category: General | Cost: ₹3500
#ID: P102 | Name: Neha Kulkarni | Category: Special | Cost: ₹18500 | Ward: ICU
#ID: P103 | Name: Rohan Deshmukh | Category: General | Cost: ₹2200