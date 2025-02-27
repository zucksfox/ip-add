import os

def add_protocol_if_missing(url, protocol):
    # Periksa apakah URL sudah dimulai dengan salah satu protokol
    if not url.startswith(('http://', 'https://', 'socks4://', 'socks5://')):
        url = protocol + url
    
    # Periksa apakah URL diakhiri dengan /
    if not url.endswith('/'):
        url += '/'
    
    return url

def process_file(input_file, output_file, protocol):
    try:
        # Hapus file output jika sudah ada
        if os.path.exists(output_file):
            os.remove(output_file)
            print(f"File {output_file} telah dihapus.")

        # Buka file input untuk dibaca
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        # Proses setiap baris dengan protokol yang dipilih
        processed_lines = [add_protocol_if_missing(line.strip(), protocol) for line in lines]
        
        # Tulis hasil ke file output
        with open(output_file, 'w') as outfile:
            for line in processed_lines:
                outfile.write(line + '\n')
        
        print(f"Proses selesai. Hasil disimpan di {output_file}")
    
    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def choose_protocol():
    print("=============================")
    print("Pilih Salah Satu")
    print("1. HTTP (http://)")
    print("2. SOCKS4 (socks4://)")
    print("3. SOCKS5 (socks5://)")
    print("=============================")
    
    choice = input("Masukkan nomor pilihan (1/2/3): ").strip()
    
    if choice == "1":
        return "https://", "https.txt"
    elif choice == "2":
        return "socks4://", "socks4.txt"
    elif choice == "3":
        return "socks5://", "socks5.txt"
    else:
        print("Pilihan tidak valid. Menggunakan default (HTTP/HTTPS).")
        return "https://", "https.txt"

def main():
    # Input nama file dari pengguna
    input_file = input("Masukkan nama file input (contoh: input.txt): ").strip()

    # Validasi input file
    if not input_file:
        print("Nama file input tidak boleh kosong!")
        return

    # Pilih protokol dan nama file output
    protocol, output_file = choose_protocol()

    # Proses file dengan output sesuai protokol
    process_file(input_file, output_file, protocol)

# Jalankan program
if __name__ == "__main__":
    main()