import os

from supabase import Client, create_client

from src.env import EnvVariables

url: str = os.environ.get(EnvVariables.SUPABASE_KEY)
key: str = os.environ.get(EnvVariables.SUPABASE_URL)
supabase: Client = create_client(url, key)
