import os
from supabase import Client, create_client
from . import enums

url: str = os.environ.get(enums.EnvVariables.SUPABASE_KEY)
key: str = os.environ.get(enums.EnvVariables.SUPABASE_URL)
supabase_client: Client = create_client(url, key)
