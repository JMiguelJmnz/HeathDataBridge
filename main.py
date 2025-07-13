from scripts.beneficiary_mapper import map_row_to_patient
from scripts.validator import validate_resource
from scripts.writer import write_resource
import pandas as pd


df = pd.read_csv("datasets/cms/DE1_0_2008_Beneficiary_Summary_File_Sample_1.csv", dtype=str)
for _, row in df.iterrows():
    patient = map_row_to_patient(row)
    is_valid, error = validate_resource(patient)
    if is_valid:
        # Get the patient ID for filename
        patient_id = patient.id or "unknown"
        filename = f"patient_{patient_id}.json"

        write_resource(patient, filename)
    else:
        print(f"Validation error for patient {patient.id}: {error}")
