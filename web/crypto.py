import hashlib, secrets

def encode_raw(raw, salt=None):
  if salt is None:
    salt = "salty"#secrets.token_bytes(32)
    print("Creating salt: {}".format(salt))
  else:
    salt = salt
  m = hashlib.sha256()
  m.update(bytes(raw, 'utf-8'))
  m.update(bytes(salt,'utf-8'))
  hashed = m.digest()
  
  return {
    "hashed": str(hashed),
    "salt": str(salt)
  }