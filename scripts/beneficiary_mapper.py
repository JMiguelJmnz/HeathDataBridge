# Script to MAP rows to FHIR

from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier
from datetime import datetime
import json
import pandas as pd

def map_row_to_patient(row):
    patient = Patient.model_construct()

    # Requiered fields
    patient.id = row["DESYNPUF_ID"]

    # Identifier (could be SSN or internal ID)
    patient.identifier = [Identifier.model_construct(
        system="https://example.org/cms-beneficiary-id",
        value=row["DESYNPUF_ID"]
    )]

    # Gender mapping
    sex_code = row["BENE_SEX_IDENT_CD"]
    patient.gender = {
        "1": "male",
        "2": "female"
    }.get(sex_code, "unknown")

    # Birth date
    if row.get("BENE_BIRTH_DT"):
        patient.birthDate = datetime.strptime(row["BENE_BIRTH_DT"], "%Y%m%d").date()

    # Death date (optional - needs 'deceasedDateTime')
    if pd.notnull(row.get("BENE_DEATH_DT")):
        patient.deceasedDateTime = datetime.strptime(row["BENE_DEATH_DT"], "%Y%m%d").date()

    # Name is synthetic - we'll fake a placeholder
    patient.name = [HumanName.model_construct(
        use="official",
        family="Doe",
        given=["John"] if patient.gender == "male" else ["Jane"]
    )]

    return patient
