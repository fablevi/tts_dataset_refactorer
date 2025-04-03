from datasets import Dataset, Audio
import json
import os

# 1. JSON betöltése
with open("../../data/hungarian-single-speaker-tts/pure/metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

# 2. Dataset létrehozása a WAV fájlokból
def create_dataset(metadata):
    audio_data = []
    text_data = []

    for item in metadata:
        if not os.path.exists(item["path"]):
            print(f"Figyelmeztetés: {item['path']} nem található, kihagyva.")
            continue

        # Hozzáadjuk a fájl elérési útját, a decode_example helyett
        audio_data.append({"path": item["path"]})
        text_data.append(item["text"])

    return Dataset.from_dict({
        "audio": audio_data,
        "text": text_data
    })


# 3. Dataset létrehozása és mentése
dataset = create_dataset(metadata)
dataset = dataset.cast_column("audio", Audio())  # Hangfájlok dekódolása

# 4. Mentés Arrow formátumba
dataset.save_to_disk("../data/hungarian-single-speaker-tts/arrow_cleared")
print("Kész! Az adathalmaz mentve 'output_arrow_dataset' könyvtárba.")