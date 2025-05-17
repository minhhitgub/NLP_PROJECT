import sentencepiece as spm

spm.SentencePieceTrainer.train(
    input='combined_train_merged.txt',
    model_prefix='lao_viet',
    vocab_size=16000,
    model_type='bpe'
)