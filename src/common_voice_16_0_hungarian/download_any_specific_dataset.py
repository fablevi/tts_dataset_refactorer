from datasets import load_dataset

# Betöltés a Common Voice 16.0 adatbázisból
ds = load_dataset("mozilla-foundation/common_voice_16_0", "hu", split="train+validation+test")

# Magyar nyelvű adatok szűrése (biztonsági ellenőrzés)
# A Common Voice esetében a "hu" paraméter már automatikusan magyar adatokat tölt be,
# de itt egy extra szűrés a biztonság kedvéért:
# ds = ds.filter(lambda x: x["language"] == "hu")

# Mentés
ds.save_to_disk("../data/common_voice_16_0_hungarian")

print(f"Mentve {len(ds)} magyar nyelvű hangminta.")