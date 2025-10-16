import os
import json

# 🔧 Настройки
FOLDER_PATH = "arts"  # можно заменить на свой путь
GITHUB_BASE_URL = "https://raw.githubusercontent.com/meed0ff/arts/refs/heads/main/arts/"

# 🔍 Расширения изображений
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif")

def generate_image_links(folder):
    images = []

    for file in os.listdir(folder):
        if file.lower().endswith(IMAGE_EXTENSIONS):
            images.append(f"{GITHUB_BASE_URL}{file}".replace(' ', '%20'))

    return images

def save_to_json(data, filename="images.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Файл {filename} успешно создан ({len(data)} изображений).")

if __name__ == "__main__":
    links = generate_image_links(FOLDER_PATH)
    save_to_json(links)
