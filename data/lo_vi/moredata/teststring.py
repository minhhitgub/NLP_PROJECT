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
            # Tokenize ra token string (subword units)
            token_pieces = sp.encode_as_pieces(line)
            # Ghi token string ra file, cách nhau bằng dấu cách
            fout.write(' '.join(token_pieces) + '\n')

# List các file cần tokenize
files_to_tokenize = [
    ('train_merged.lo', 'train_merged.tok.lo'),
    ('train_merged.vi', 'train_merged.tok.vi'),
    
]

for input_file, output_file in files_to_tokenize:
    print(f"Tokenizing {input_file} → {output_file}")
    tokenize_file(input_file, output_file)
print("Tokenize xong hết rồi!")