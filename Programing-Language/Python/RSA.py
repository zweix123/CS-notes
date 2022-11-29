import math


class RSA(Exception):
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1, 1):
            if num % i == 0:
                return False
        return True

    def exgcd(self, a, b):
        if b == 0:
            return 1, 0, a
        else:
            x, y, res = self.exgcd(b, a % b)
            x, y = y, (x - (a // b) * y)
            return x, y, res

    def __init__(self, prime_p, prime_q, secret_key_e):
        str_msg = ""
        if self.is_prime(prime_p) == False:
            str_msg = str_msg + "素数p(" + str(prime_p) + ")不是素数\n"
        if self.is_prime(prime_q) == False:
            str_msg = str_msg + "素数q(" + str(prime_q) + ")不是素数\n"

        self.prime_p = prime_p
        self.prime_q = prime_q
        self.secret_key_n = self.prime_p * self.prime_q
        self.secret_key_phi = (self.prime_p - 1) * (self.prime_q - 1)

        if math.gcd(self.secret_key_phi, secret_key_e) != 1:
            str_msg = str_msg + \
                "公开指数e(" + str(secret_key_e) + \
                ")和\phi{n} = " + str(self.secret_key_phi) + "不是互为素数"

        self.secrect_key_e = secret_key_e

        if len(str_msg) != 0:
            raise Exception(str_msg)

        self.secrect_key_d, sam1, sam2 = self.exgcd(
            self.secrect_key_e, self.secret_key_phi)
        self.secrect_key_d = (self.secrect_key_d +
                              self.secret_key_phi) % self.secret_key_phi

    def __str__(self):
        return "该RSA系统的公钥为(n = {}, e = {}), 私钥为(d = {})".format(self.secret_key_n, self.secrect_key_e, self.secrect_key_d)

    def e_(self, num):
        return num ** self.secrect_key_e % self.secret_key_n

    def d_(self, num):
        return num ** self.secrect_key_d % self.secret_key_n


if __name__ == '__main__':

    sam = RSA(3, 11, 3)
    print(sam)
    print(sam.e_(11))
    print(sam.d_(16))
    print("zweix")
