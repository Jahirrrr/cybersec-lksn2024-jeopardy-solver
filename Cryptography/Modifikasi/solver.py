# git clone https://github.com/upbit/clone-fastcoll
# cd fastcoll
# pindahin file executable fastcoll nya ke direktori soal
# eksekusi di command : ./fastcoll server.py
# cek md5 nya : md5sum md5_data*

# by Kurokaze
# ngebaca file md5 nya sebagai hex
def baca_hex(file_path):
    with open(file_path, "rb") as f:
        return f.read().hex()

def main():
    # baca dan konversi ke hex
    alice_ticket = baca_hex("md5_data1")
    bob_ticket = baca_hex("md5_data2")
    
    # tampilin tikeettt deehh, tinggal submit :>
    print(f"Tiket Alice (md5_data1): {alice_ticket}")
    print(f"Tiket Bob (md5_data2): {bob_ticket}")
    
    # Output Soal :
    # Bob: Terima kasih! Ini bayarannya :
    # LKSN{Blablablabla}

if __name__ == "__main__":
    main()
