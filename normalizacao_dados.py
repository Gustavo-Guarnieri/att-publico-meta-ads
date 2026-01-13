import re
import unicodedata
import hashlib

# ======== Normalizar texto (nome / sobrenome)
def normalize_text(value: str) -> str:
    value = value.strip().lower()
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("utf-8")
    value = re.sub(r"[^a-z]", "", value)
    return value

# ======== Normalizar email
def normalize_email(email: str) -> str:
    return email.strip().lower()

# ======== Normalizar numero
def normalize_phone(phone: str, country_code: str = "55") -> str:
    phone = re.sub(r"\D", "", phone)  # só números
    phone = phone.lstrip("0")         # remove zeros à esquerda

    if not phone.startswith(country_code):
        phone = country_code + phone

    return phone


# ======== Normalizar país
def normalize_country(country: str) -> str:
    return country.strip().lower()

# ======== Hash SHA-256
def hash_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

# ======== Aplicando normalização aos dados com loop
def normaliza_dados(lista_mix: list) -> list:
    usuarios_normalizados = []

    for item in lista_mix:
        props = item.get("$properties", {})

        #Verifica se o dado exsite
        first_name = normalize_text(props.get("Name", "").split(" ")[0]) or "Sem nome"
        email = normalize_email(props.get("Email", "")) or "Sem email"
        phone = normalize_phone(props.get("Phone", "")) or "Sem telefone"
        country = normalize_country(props.get("Pais", "br")) or "Sem pais"

        #Faz criptografia
        if first_name:
            norm_fn = hash_sha256(first_name)
        if email:
            norm_email = hash_sha256(email)
        if phone:
            norm_phone = hash_sha256(phone)
        if country:
            norm_country = hash_sha256(country)

        usuarios_normalizados.append([norm_fn, norm_email, norm_phone, norm_country])

    print('Dados normalizados')

    return usuarios_normalizados



