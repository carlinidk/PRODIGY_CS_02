# IMAGE ENCRYPTION AND DECRYPTION TOOL
A Python-based Image Encryption and Decryption Tool that allows users to securely encrypt and decrypt images using various cryptographic methods, including channel swapping and mathematical operations (addition, subtraction, multiplication, and division). Supports batch processing of multiple image formats like PNG, JPG, and JPE
----------------------
Features
Encryption Methods:
Channel Swap: Swaps the red and blue channels of an image for encryption.
Mathematical Operations: Uses addition, subtraction, multiplication, or division with a key to alter pixel values.
Decryption Support: Reverses the encryption process using the same method and key.
Batch Processing: Automatically processes all images in a specified folder.
Customizable:Users can choose their preferred encryption method, mathematical operation, and key. 
-----------------------
Installation
----------------------
Clone the repository:
git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool
----------------------
Install the required libraries:
pip install pillow numpy
Usage
----------------------
Prepare your images:
Place the images you want to process in the example_images folder.
----------------------
Run the program:
bash
python PIXELMANU.py
----------------------
Follow the prompts:
Choose an action: encrypt or decrypt.
Select the method: swap or math.
For mathematical operations:
Specify the operation: add, subtract, multiply, or divide.
Provide a key (an integer value).
Processed images:
Encrypted or decrypted images will be saved in the output_images folder.
------------------------------------
Example
Encryption:
Input: example_images/image1.jpg
Method: math
Operation: add
Key: 10
Output: output_images/encrypted_image1.jpg
Decryption:
Input: output_images/encrypted_image1.jpg
Method: math
Operation: add
Key: 10
Output: output_images/decrypted_image1.jpg
-----------------------------------
Future Improvements
Add support for more advanced encryption algorithms.
Implement GUI-based user interaction.
Enhance performance for larger images or datasets.
License
This project is licensed under the MIT License.
