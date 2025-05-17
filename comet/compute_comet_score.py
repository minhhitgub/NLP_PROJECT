from comet import download_model, load_from_checkpoint

# Tải model đánh giá (hoặc chỉ load lần đầu tiên)
model_path = download_model("wmt-large-da-estimator-1719")  # model phổ biến cho đánh giá

# Load model comet
comet_model = load_from_checkpoint(model_path)

# Đọc dữ liệu dịch và tham khảo
with open("path_to/translate.en2vi.vi", "r", encoding="utf-8") as f:
    hypotheses = [line.strip() for line in f]

with open("path_to/tst2012.vi", "r", encoding="utf-8") as f:
    references = [line.strip() for line in f]

# Tính điểm comet (ở đây giả sử 1 tham khảo)
scores = comet_model.predict(hypotheses, references)

print(f"COMET score: {scores.mean():.4f}")
