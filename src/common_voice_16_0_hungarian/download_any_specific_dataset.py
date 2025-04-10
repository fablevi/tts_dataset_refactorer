from datasets import load_dataset

# Betöltés a Common Voice 16.0 adatbázisból
ds = load_dataset("mozilla-foundation/common_voice_16_1", "hu", split="train+validation")

# Mentés
ds.save_to_disk("../../data/common_voice_16_1_hungarian")

print(f"Mentve {len(ds)} magyar nyelvű hangminta.")