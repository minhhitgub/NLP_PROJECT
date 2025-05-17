import argparse
from nltk.translate.meteor_score import meteor_score

def main(args):
    with open(args.hypotheses, 'r', encoding='utf-8') as f:
        hypotheses = [line.strip().split() for line in f]  # tách token bằng khoảng trắng

    with open(args.references, 'r', encoding='utf-8') as f:
        references = [line.strip().split() for line in f]

    scores = []
    for hyp, ref in zip(hypotheses, references):
        score = meteor_score([ref], hyp)
        scores.append(score)

    avg_score = sum(scores) / len(scores)
    print(f"Average METEOR score: {avg_score:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hypotheses", required=True, help="File chứa bản dịch mô hình")
    parser.add_argument("--references", required=True, help="File chứa bản tham khảo")
    args = parser.parse_args()
    main(args)
