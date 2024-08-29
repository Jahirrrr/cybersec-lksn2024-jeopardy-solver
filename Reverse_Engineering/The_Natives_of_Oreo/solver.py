# by Kurokazeee

import string

def cek_apakah_bit_benar(bit1, bit2, hasil_bismillah_bener):
    # hitung hasil perkalian dua byte bosku
    hasil = bit1 * bit2
    return hasil == hasil_bismillah_bener

# Kita pake metode bruteforce cuy, karena bit disini banyak bener
def bruteforce():
    # List variabel dari liblksnapp.so
    variabel = [
        0x0000000000001644, 0x0000000000001851, 0x000000000000194a,
        0x000000000000257a, 0x0000000000002031, 0x0000000000000b41,
        0x0000000000000739, 0x0000000000000ff5, 0x000000000000122f,
        0x000000000000150e, 0x00000000000028d2, 0x000000000000134c,
        0x0000000000001658, 0x0000000000002af8, 0x0000000000002c88,
        0x0000000000001560, 0x00000000000013b0, 0x0000000000002904,
        0x000000000000251c, 0x00000000000026f7, 0x0000000000002f2b,
        0x0000000000002aad, 0x00000000000025da, 0x0000000000002e9e,
        0x0000000000003246, 0x0000000000000e2e, 0x000000000000101d
    ]

    # kumpulan kata yang ada di dalam flag (karena ini bruteforce, jadi nebak aja WKWKWKWKWK)
    bf_chars = string.ascii_letters + string.digits + string.punctuation

    # karena format flag LKSN{}, kita awali dengan huruf depan nya 'L', karena jika di cek kode yg ada di liblksnapp.so, kode sangat bergantung pada indeks nya
    flag = ['L']

    for i in range(27):  # flag memiliki panjang 28 karakter, tau darimana? liat aja liblksnapp.so :>
        apakah_char_ketemu = False

        for c in bf_chars:
            bit1 = ord(flag[-1])
            bit2 = ord(c)

            if cek_apakah_bit_benar(bit1, bit2, variabel[i]):
                flag.append(c)
                apakah_char_ketemu = True
                print(f"Flag bocor cuyyyy {i+1}: {c}")
                break

        if not apakah_char_ketemu:
            print(f"Gagal mendapatkan flag {i+1}")
            break

    return ''.join(flag)

flag_asli = bruteforce()
print(f"Flag aseli: {flag_asli}")
