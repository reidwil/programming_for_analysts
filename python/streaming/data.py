import random
import string

def generate_id(length: int = 16) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

BufferData = str