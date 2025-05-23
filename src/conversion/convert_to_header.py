import numpy as np
import os

def convert_tflite_to_header(tflite_path, output_header_path):
    with open(tflite_path, 'rb') as tflite_file:
        tflite_content = tflite_file.read()

    hex_lines = [', '.join([f'0x{byte:02x}' for byte in tflite_content[i:i+12]]) for i in range(0, len(tflite_content), 12)]
    hex_array = ',\n  '.join(hex_lines)

    with open(output_header_path, 'w') as header_file:
        header_file.write('#include "model.h"\n\n')
        header_file.write('alignas(16) const unsigned char g_model[] = {\n  ')
        header_file.write(f'{hex_array}\n')
        header_file.write('};\n\n')
        header_file.write(f'const int g_model_len = {len(hex_lines) * 12};')
    
if __name__ == "__main__":
    tflite_path = 'models/350kb.tflite'
    output_header_path = 'models/model.cpp'
    
    convert_tflite_to_header(tflite_path, output_header_path)
