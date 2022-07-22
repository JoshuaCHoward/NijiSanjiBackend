import os
from dotenv import load_dotenv
from .enums import EnvVariables
load_dotenv()

for key in EnvVariables:
    if os.getenv(key) is None:
        raise ValueError(f'{key} does not exist')
