from comet import download_model, load_from_checkpoint

# Tải và load model COMET
model_path = download_model("Unbabel/wmt22-comet-da")  # hoặc "Unbabel/wmt20-comet-da"
model = load_from_checkpoint(model_path)

# Đọc file input
with open(r"C:\Users\bruh\Downloads\KC4.0_MultilingualNMT-master\KC4.0_MultilingualNMT-master\data\lo_vi\test2023.tok.lo") as f:
    sources = [line.strip() for line in f.readlines()]

with open(r"C:\Users\bruh\Downloads\KC4.0_MultilingualNMT-master\KC4.0_MultilingualNMT-master\data\lo_vi/test2023.tok.vi") as f:
    references = [line.strip() for line in f.readlines()]

with open(r"C:\Users\bruh\Downloads\KC4.0_MultilingualNMT-master\KC4.0_MultilingualNMT-master\models/lo-vi.model/translate.lo2vi.vi") as f:
    hypotheses = [line.strip() for line in f.readlines()]

# Tạo tập đánh giá
data = [{"src": s, "ref": r, "mt": h} for s, r, h in zip(sources, references, hypotheses)]

# Tính điểm
results = model.predict(data, batch_size=8, gpus=1)  # đổi `gpus=0` nếu không dùng GPU

print("COMET Score:", results["mean"])
