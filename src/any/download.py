from datasets import load_dataset

database_name = "mozilla-foundation/common_voice_17_0"
language = "hu"
#split="train+validation"
# Betöltés
ds = load_dataset(database_name, language, split="train+validation+other")

# JSON-ba mentés
ds.save_to_disk(f"../../data/{database_name}/train")  # Könyvtárba mentés (DatasetDict formátumban)