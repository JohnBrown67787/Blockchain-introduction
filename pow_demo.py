import hashlib, time

def mine_block(data: str, difficulty: int) -> dict:
    prefix = "0" * difficulty
    nonce = 0
    start = time.time()
    while True:
        candidate = f"{data}{nonce}"
        h = hashlib.sha256(candidate.encode()).hexdigest()
        if h.startswith(prefix):
            elapsed = time.time() - start
            return {"nonce": nonce, "hash": h, "time": elapsed}
        nonce += 1

for d in (3, 4, 5):
    result = mine_block("SSBlock#1", difficulty=d)
    print(f"Difficulty {d} -> nonce: {result['nonce']:>10} | time: {result['time']:.3f}s")
    print(f"             hash: {result['hash']}")