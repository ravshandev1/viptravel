import uuid


def generate_unique_filename(instance, filename):
    extension = filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return f"images/{unique_filename}"