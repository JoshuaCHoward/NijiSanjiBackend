import os
from supabase import Client, create_client

from src.env import enums

url: str = os.environ.get(enums.EnvVariables.SUPABASE_URL)
key: str = os.environ.get(enums.EnvVariables.SUPABASE_KEY)
supabase_client: Client = create_client(url, key)
supabase_storage = supabase_client.storage()
