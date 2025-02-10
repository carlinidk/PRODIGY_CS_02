import os
from PIL import Image
import numpy as np

def encrypt_image(img, method, operation=None, key=None):
    """Encrypt the image based on the chosen method."""
    img_array = np.array(img)
    
    if method == "swap":
        if img_array.shape[-1] == 3:  # Ensure RGB image
            img_array[:, :, [0, 2]] = img_array[:, :, [2, 0]]

    elif method == "math" and operation and key is not None:
        img_array = img_array.astype(np.int32)  
        if operation == "add":
            img_array = (img_array + key) % 256
        elif operation == "subtract":
            img_array = (img_array - key) % 256
        elif operation == "multiply":
            img_array = (img_array * key) % 256
        elif operation == "divide":
            if key == 0:
                raise ValueError("Division by zero is not allowed.")
            img_array = (img_array // key) % 256
        img_array = img_array.astype(np.uint8)  # Convert back to uint8
    
    return Image.fromarray(img_array)

def decrypt_image(img, method, operation=None, key=None):
    """Decrypt the image based on the chosen method."""
    img_array = np.array(img)
    
    if method == "swap":
        if img_array.shape[-1] == 3:  # Ensure RGB image
            img_array[:, :, [0, 2]] = img_array[:, :, [2, 0]]
    
    elif method == "math" and operation and key is not None:
        img_array = img_array.astype(np.int32)  
        if operation == "add":
            img_array = (img_array - key) % 256
        elif operation == "subtract":
            img_array = (img_array + key) % 256
        elif operation == "multiply":
            try:
                inverse_key = pow(key, -1, 256)  # Ensure key has an inverse under mod 256
                img_array = (img_array * inverse_key) % 256
            except ValueError:
                print("Error: The key is not invertible for multiplication!")
                return img
        elif operation == "divide":
            try:
                inverse_key = pow(key, -1, 256)  # Get modular inverse
                img_array = (img_array * inverse_key) % 256
            except ValueError:
                print("Error: The key is not invertible for division!")
                return img
        img_array = img_array.astype(np.uint8)  # Convert back to uint8
    
    return Image.fromarray(img_array)

def process_images(action, folder="example_images", output_folder="output_images"):
    """Encrypt or decrypt all images in the folder."""
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    # Get user input
    method = input("Choose a method ('swap' or 'math'): ").strip().lower()
    
    operation = None
    key = None

    if method == "math":
        operation = input("Choose a mathematical operation ('add', 'subtract', 'multiply', 'divide'): ").strip().lower()
        try:
            key = int(input("Enter the key (integer): "))
            if operation in ["multiply", "divide"] and key % 256 == 0:
                raise ValueError("Invalid key for multiplication or division.")
        except ValueError:
            print("Invalid key! Please enter a valid integer.")
            return
    
    print(f"Processing images using method '{method}' and key '{key}'...")

    for filename in os.listdir(folder):
        if filename.lower().endswith(("png", "jpg", "jpeg")):
            input_path = os.path.join(folder, filename)
            try:
                img = Image.open(input_path).convert("RGB")
                if action == "encrypt":
                    output_path = os.path.join(output_folder, f"encrypted_{filename}")
                    encrypted_img = encrypt_image(img, method, operation, key)
                    encrypted_img.save(output_path)
                    print(f"Encrypted '{filename}' -> '{output_path}'")
                elif action == "decrypt":
                    output_path = os.path.join(output_folder, f"decrypted_{filename}")
                    decrypted_img = decrypt_image(img, method, operation, key)
                    decrypted_img.save(output_path)
                    print(f"Decrypted '{filename}' -> '{output_path}'")
            except Exception as e:
                print(f"Error processing file '{filename}': {e}")
    
    print(f"All {action}ed images are saved in '{output_folder}'.")

# Main program
if __name__ == "__main__":
    action = input("Enter 'encrypt' or 'decrypt': ").strip().lower()
    if action in ["encrypt", "decrypt"]:
        process_images(action)
    else:
        print("Invalid action! Please enter 'encrypt' or 'decrypt'.")
