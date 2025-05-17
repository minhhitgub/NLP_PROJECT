import argparse
from comet import download_model, load_from_checkpoint

def main(args):
    model_path = download_model("wmt-large-da-estimator-1719")
    comet_model = load_from_checkpoint(model_path)

    with open(args.hypotheses, "r", encoding="utf-8") as f:
        hypotheses = [line.strip() for line in f]
    with open(args.references, "r", encoding="utf-8") as f:
        references = [line.strip() for line in f]

    scores = comet_model.predict(hypotheses, references)
    print(f"COMET score: {scores.mean():.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hypotheses", required=True, help="File chứa bản dịch mô hình")
    parser.add_argument("--references", required=True, help="File chứa bản tham khảo")
    args = parser.parse_args()
    main(args)
