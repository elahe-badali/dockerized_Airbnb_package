import hashlib

DIRECT_PII_COLUMNS = ["host_name"]

def pseudonymize_value(value, salt='qbc12'):
    new_value = f"{salt}:{value}"
    code = hashlib.sha256(new_value.encode("utf-8")).hexdigest()
    return code

def handle_pii(df):

    df = df.copy()
    df = df.drop(columns=DIRECT_PII_COLUMNS, errors="ignore")

    df["host_key"] = df["host_id"].apply(pseudonymize_value)
    df = df.drop(columns=["host_id"])

    return df