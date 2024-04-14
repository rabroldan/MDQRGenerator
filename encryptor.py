import os

encryption_key = b"\xc8\xcbLh\xed'\xa2\xe6\xe5A\xe4\x18\x04\xcd\x85\xee\x91J\x18\x8b\xb6;\ebO\xde\x82\xea\xfd\x01\xa6\xd5p"


def encrypt_data(data):
    encrypted_data = bytearray(data)
    for i in range(len(encrypted_data)):
        encrypted_data[i] ^= encryption_key[i % len(encryption_key)]
    return encrypted_data


def encrypt_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            data = bytearray(file.read())

        encrypted_data = encrypt_data(data)

        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def decrypt_data(data):
    decrypted_data = bytearray(data)
    for i in range(len(decrypted_data)):
        decrypted_data[i] ^= encryption_key[i % len(encryption_key)]
    return decrypted_data


def decrypt_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            data = bytearray(file.read())

        decrypted_data = decrypt_data(data)

        with open(output_file, 'wb') as file:
            file.write(decrypted_data)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def encrypt_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, f"encrypted_{filename}")
            encrypt_file(input_file, output_file)
            print(f"{input_file} has been encrypted and saved as {output_file}")
            os.remove(f"{folder_path}/{filename}")


def decrypt_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("encrypted_") and filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, filename.replace("encrypted_", ""))
            decrypt_file(input_file, output_file)
            print(f"{input_file} has been decrypted and saved as {output_file}")
            os.remove(f"{folder_path}/{filename}")

# Uncomment the following line to encrypt files
# encrypt_files_in_folder("uploads")

# Uncomment the following line to decrypt files
# decrypt_files_in_folder("uploads")
