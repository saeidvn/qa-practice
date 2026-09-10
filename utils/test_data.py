import uuid
import random


USER_CREDENTIALS = [
    ("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "error"),
    ("problem_user", "secret_sauce", "success"),
    ("performance_glitch_user", "secret_sauce", "success"),
    ("error_user", "secret_sauce", "success"),
    ("visual_user", "secret_sauce", "success"),
]

def get_random_checkout_data():
    return {
        "first_name": f"User_{uuid.uuid4().hex[:6]}",
        "last_name": f"Test_{uuid.uuid4().hex[:6]}",
        "postal_code": str(random.randint(10000, 99999))
    }