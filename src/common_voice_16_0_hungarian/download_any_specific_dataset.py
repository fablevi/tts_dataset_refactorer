from datasets import load_dataset

# Betöltés a Common Voice 16.0 adatbázisból
ds = load_dataset("mozilla-foundation/common_voice_16_0", "hu", split="train+validation")

# Mentés
ds.save_to_disk("../../data/common_voice_16_0_hungarian")

print(f"Mentve {len(ds)} magyar nyelvű hangminta.")