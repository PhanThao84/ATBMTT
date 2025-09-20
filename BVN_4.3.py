from math import gcd
def generate_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError("e không nguyên tố cùng nhau với phi(n).")
    # Euclid mở rộng để tìm nghịch đảo modular
    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)
    g, x, y = egcd(e, phi)
    d = x % phi
    return (n, e, d)
def encrypt_text(text, n, e):
    return [pow(ord(ch), e, n) for ch in text]
def decrypt_cipherlist(cipherlist, n, d):
    return ''.join(chr(pow(c, d, n)) for c in cipherlist)
if __name__ == "__main__":
    # Nhập tham số
    p = int(input("Nhập p: "))
    q = int(input("Nhập q: "))
    e = int(input("Nhập e: "))
    P = input("Nhập thông điệp P: ")
    n, e_val, d = generate_keys(p, q, e)
    print("\nKhóa công khai: (n={}, e={})".format(n, e_val))
    print("Khóa bí mật d =", d)
    C = encrypt_text(P, n, e_val)
    print("\nPlaintext:", P)
    print("Ciphertext:", C)
    recovered = decrypt_cipherlist(C, n, d)
    print("Giải mã:", recovered)
