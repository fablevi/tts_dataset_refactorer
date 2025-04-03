from datasets import load_from_disk

# 1. Arrow adathalmaz betöltése
dataset = load_from_disk("../../data/hungarian-single-speaker-tts")  # Az előzőleg mentett mappa elérési útja

# 2. Az első elem kiolvasása
print(len(dataset)-1)
first_item = dataset[len(dataset)-1]  # Vagy dataset["train"][0] ha több split van

# 3. Az adatok megjelenítése
print("Első elem hangadatai:")
print(f"- Fájl elérési út: {first_item['audio']['path']}")
print(f"- Mintavételezési ráta: {first_item['audio']['sampling_rate']} Hz")
print(f"- Hangminta tömb mérete: {len(first_item['audio']['array'])} mintából")
print(f"- Szöveg: {first_item['text']}")

# 4. Opcionális: hang lejátszása Jupyter notebookban
# from IPython.display import Audio as IPythonAudio
# IPythonAudio(first_item['audio']['array'], rate=first_item['audio']['sampling_rate'])