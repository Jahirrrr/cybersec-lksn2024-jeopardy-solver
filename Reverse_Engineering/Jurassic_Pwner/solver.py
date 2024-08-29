# by Kurokaze

from sympy import mod_inverse

# isi value nya
p1 = 294704857459121458995842604700946850751
p2 = 314052721216923470597325825556277950411
res = 54846125195579777053464962994274277267744411269096779149171289487630586305476
e = 65537

n = p1 * p2
phi_n = (p1 - 1) * (p2 - 1)

d = mod_inverse(e, phi_n)

hr = pow(res, d, n)

# flagnya boyyy
flag = 4830690556514140397518897252109979335664677923435018942901273242454015697691068037340554551586759138432178879438287937684165299693520135533018994309974094302098369656069901396834

ril_flag = hr ^ flag

flag_bentuk_hex = hex(ril_flag)[2:]

ubah_flag = bytes.fromhex(flag_bentuk_hex)

flag_aseli = ubah_flag.decode('utf-8')
print(f"Flag aseli : {flag_aseli}")
# Output :
# Flag aseli : LKSN{you_reached_the_super_duper_high_score_you_dirty_ch34t3rrrrRrrrrawr!}
