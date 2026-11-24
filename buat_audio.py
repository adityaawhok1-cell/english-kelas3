import asyncio
import os
import edge_tts

INPUT_FILE = "daftar-audio.txt"
OUTPUT_DIR = "audio"
VOICE = "en-US-JennyNeural"  # Opsi lain: "en-US-AriaNeural" atau "en-GB-SoniaNeural"

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    items = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "|" not in line:
                continue
            filename, text = [part.strip() for part in line.split("|", 1)]
            if not filename.endswith(".mp3") or not text:
                continue
            items.append((filename, text, os.path.join(OUTPUT_DIR, filename)))

    print(f"Memproses {len(items)} file audio ke folder '{OUTPUT_DIR}/'...")

    for idx, (filename, text, out_path) in enumerate(items, 1):
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(out_path)
        print(f"[{idx}/{len(items)}] {filename} -> \"{text}\"")

    print("\nSelesai! Semua file .mp3 sudah siap di folder 'audio'.")

if __name__ == "__main__":
    asyncio.run(main())
