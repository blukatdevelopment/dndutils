import hashlib, secrets, random, string

def encode_raw(raw, salt=None):
  if salt is None:
    salt = get_random_string(32)
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

def get_random_string(length):
    letters = string.ascii_lowercase
    ret = ''.join(random.choice(letters) for i in range(length))
    return ret