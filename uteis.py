def normalizar(v):
    resp = list()
    for c in v:
        r = (c - min(v)) / (max(v) - min(v))
        resp.append(r)
    return resp
