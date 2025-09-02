def mahoa(plaintext, k):
    Ketqua = ""
    for char in plaintext:
        if char.isalpha():  # chỉ mã hóa ký tự chữ cái
            shift = k % 26
            if char.isupper():
                Ketqua += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                Ketqua += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            Ketqua += char  
    return Ketqua

# Nhập từ bàn phím
plaintext = input("Nhập Plaintext: ")
k = int(input("Nhập khóa k: "))
KETQUA= mahoa(plaintext, k)
print("Ciphertext:", KETQUA)