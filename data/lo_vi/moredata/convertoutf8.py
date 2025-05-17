import chardet

input_file = 'combined_train_merged.txt'
output_file = 'combined_train_merged_utf8.txt'

print("Bắt đầu đọc file để phát hiện encoding...")
with open(input_file, 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    source_encoding = result['encoding']
    print(f"Detected encoding: {source_encoding}")

print("Bắt đầu chuyển đổi sang UTF-8 và ghi ra file mới...")
with open(input_file, 'r', encoding=source_encoding, errors='ignore') as f_in, \
     open(output_file, 'w', encoding='utf-8') as f_out:
    line_count = 0
    for line in f_in:
        f_out.write(line)
        line_count += 1
        if line_count % 10000 == 0:
            print(f"Đã xử lý {line_count} dòng...")

print(f"Hoàn thành chuyển đổi {line_count} dòng sang UTF-8.")
