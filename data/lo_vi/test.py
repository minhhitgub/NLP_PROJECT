import sentencepiece as spm

# Load tokenizer đã train
sp = spm.SentencePieceProcessor()
sp.load('lao_viet.model')

def tokenize_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as fin, \
         open(output_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            token_ids = sp.encode(line, out_type=int)
            # Ghi token IDs ra file, cách nhau bằng dấu cách
            fout.write(' '.join(map(str, token_ids)) + '\n')

# List các file cần tokenize
files_to_tokenize = [
    ('train2023.lo', 'train2023.tok.lo'),
    ('train2023.vi', 'train2023.tok.vi'),
    ('dev2023.lo', 'dev2023.tok.lo'),
    ('dev2023.vi', 'dev2023.tok.vi'),
    ('test2023.lo', 'test2023.tok.lo'),
    ('test2023.vi', 'test2023.tok.vi'),
]

for input_file, output_file in files_to_tokenize:
    print(f"Tokenizing {input_file} → {output_file}")
    tokenize_file(input_file, output_file)
print("Tokenize xong hết rồi!")
