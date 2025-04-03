from datasets import load_dataset

# Betöltés
ds = load_dataset("KTH/hungarian-single-speaker-tts")

# JSON-ba mentés
ds.save_to_disk("../../data/hungarian-single-speaker-tts/train")  # Könyvtárba mentés (DatasetDict formátumban)