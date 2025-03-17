import math


class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """ Mã hóa bằng Transposition Cipher """
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt(self, text, key):
        num_cols = math.ceil(len(text) / key)  # Số cột trong lưới
        num_rows = key  # Số hàng
        num_shaded_boxes = (num_cols * num_rows) - len(text)  # Số ô trống
        
        decrypted_text = [""] * num_cols
        col, row = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1

            # Khi đến cột cuối hoặc đến vùng trống thì xuống hàng
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1


        return ''.join(decrypted_text)
