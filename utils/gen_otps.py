import hashlib
import time

OTPS_FILE = "otps.txt"

with open(OTPS_FILE, "w") as f:
	for comb in [
		f"{a}{b}{c}{d}{e}{f}"
		for a in range(10)
		for b in range(10)
		for c in range(10)
		for d in range(10)
		for e in range(10)
		for f in range(10)
	]:
		hash_object = hashlib.sha256()
		hash_object.update(comb.encode("utf-8"))
		hash_hex = hash_object.hexdigest()
		f.write(f"{comb},{hash_hex}\n")

"""

otp = "93d07c938405633c7d31251154cc2d7dfa4f9df8a35f3eeb3d5620762f69d2e5"

start = time.time()

with open(OTPS_FILE, "r") as f:
	for line in f:
		if line.strip() == otp:
			break

print(time.time() - start)

"""