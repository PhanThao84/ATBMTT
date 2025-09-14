def mahoa_phepcong(plaintext, k):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():  # chỉ mã hóa chữ cái
            base = ord('A') if ch.isupper() else ord('a')
            c = (ord(ch) - base + k) % 26 + base
            ciphertext += chr(c)
        else:
            ciphertext += ch  # giữ nguyên nếu không phải chữ
    return ciphertext

# Ví dụ:
P = input("Nhập tên của bạn: ")
STT = int(input("Nhập key tại đây: "))
C = mahoa_phepcong(P, STT)
print("Mã hoá:", C)