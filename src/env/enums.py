from typing import NamedTuple


class EnvVariablesClass(NamedTuple):
    SUPABASE_URL: str
    SUPABASE_KEY: str


EnvVariables = EnvVariablesClass(SUPABASE_KEY="SUPABASE_KEY", SUPABASE_URL="SUPABASE_URL")
