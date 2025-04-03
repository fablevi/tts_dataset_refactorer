from datasets import load_from_disk
import soundfile as sf
import json
import os

# Betöltés
dataset = load_from_disk("../../data/hungarian-single-speaker-tts")

# Készítsünk egy listát az összes adat tárolására
all_data = []

# Végigmegyünk a train split összes elemén
for i, item in enumerate(dataset["train"]):
    audio_data = item["audio"]
    text = item["original_text"]  # Feltehetően itt van a szöveg

    # Hangfájl mentése
    output_dir = "../../data/hungarian-single-speaker-tts/pure/data"
    os.makedirs(output_dir, exist_ok=True)

    # A fájlnevet az eredeti path-ból vesszük, vagy generálunk
    filename = os.path.basename(audio_data["path"]) if "path" in audio_data else f"audio_{i}.wav"
    output_path = os.path.join(output_dir, filename)

    sf.write(output_path, audio_data["array"], audio_data["sampling_rate"])

    # JSON adat összeállítása
    all_data.append({
        "path": output_path,
        "text": text,
        "sampling_rate": audio_data["sampling_rate"]
    })
output_dir = "../../data/hungarian-single-speaker-tts/pure"
# Összes adat mentése JSON fájlba
with open(os.path.join(output_dir, "metadata.json"), "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Kész! {len(all_data)} hangfájl mentve és JSON létrehozva.")