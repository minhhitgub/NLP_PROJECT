import sentencepiece as spm
import os

# Load model sentencepiece đã train sẵn (đường dẫn thay bằng model của bạn)
sp = spm.SentencePieceProcessor()
sp.load('lao_viet.model')

def detokenize_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as fin, \
         open(output_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            line = line.strip()
            # Tokenize (encode) câu
            tokens = sp.encode(line, out_type=str)
            # Loại bỏ dấu ▁ trong từng token
            clean_tokens = [t.replace('▁', '') for t in tokens]
            # Ghép lại thành câu (cách nhau bằng dấu cách)
            detok_line = ' '.join(clean_tokens)
            fout.write(detok_line + '\n')

# Danh sách file input và output tương ứng
file_pairs = [
    ('dev2023.lo', 'dev2023.detok.lo'),
    ('dev2023.vi', 'dev2023.detok.vi'),
    ('train2023.lo', 'train2023.detok.lo'),
    ('train2023.vi', 'train2023.detok.vi'),
    ('test2023.lo', 'test2023.detok.lo'),
    ('test2023.vi', 'test2023.detok.vi'),
]

for inp, outp in file_pairs:
    if os.path.exists(inp):
        detokenize_file(inp, outp)
        print(f'Processed {inp} -> {outp}')
    else:
        print(f'File not found: {inp}')
