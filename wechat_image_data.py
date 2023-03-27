import os
import sys
import logging

logging.basicConfig(filename='file_encrypt_decrypt.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def encrypt_decrypt_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, "rb") as fin:
            with open(output_file_path, "wb") as fout:
                while True:
                    b = fin.read(1)
                    if not b:
                        break
                    fout.write(bytes([b[0] ^ 0xB0]))
        logging.info(f"{input_file_path} has been encrypted/decrypted successfully to {output_file_path}")
    except FileNotFoundError:
        logging.warning(f"Can not open file {input_file_path} or {output_file_path}")
        sys.exit(-1)

def main():
   # if len(sys.argv) != 2:
   #     print(f"Usage: {sys.argv[0]} <directory>")
   #     sys.exit(0)
    
    directory = input("请输入源文件路径：")
    if not os.path.isdir(directory):
        print(f"{directory} is not a directory")
        sys.exit(-1)

    for root, _, files in os.walk(directory):
        for filename in files:
            input_file_path = os.path.join(root, filename)
            output_file_path = input_file_path + ".jpg" # append ".enc" to encrypted/decrypted file
            encrypt_decrypt_file(input_file_path, output_file_path)
            print(input_file_path)
            os.remove(input_file_path)

if __name__ == '__main__':
    main()



    # 检查命令行参数
   # if len(sys.argv) != 3:
   #     print(f"使用方法：{sys.argv[0]} <输入文件路径> <输出文件路径>")
   #     sys.exit(0)

    # 获取输入和输出文件路径
    #input_file_path = sys.argv[1]
    #output_file_path = sys.argv[2]
 #   input_file_path = input("请输入源文件路径：")
  #  output_file_path = input("请输入目的文件路径：")
    # 检查输入文件是否存在
