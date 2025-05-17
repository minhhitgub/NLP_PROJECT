import chardet

filename = 'combined_train_merged.txt'

with open(filename, 'rb') as f:
    rawdata = f.read(10000)  # đọc 10KB đầu để đoán
    result = chardet.detect(rawdata)
    print(f"Encoding phát hiện: {result['encoding']}")
