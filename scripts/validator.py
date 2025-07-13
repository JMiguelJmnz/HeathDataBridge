from pydantic import ValidationError

def validate_resource(resource):
    try:
        resource.dict()  # or resource.model_validate()
        return True, None
    except ValidationError as e:
        return False, e
