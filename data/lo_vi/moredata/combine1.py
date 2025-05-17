with open("train_merged.lo", "w", encoding="utf-8") as f_out:
    # Đọc và ghi nội dung từ train2023.lo
    with open("train2023.lo", "r", encoding="utf-8") as f1:
        for line in f1:
            f_out.write(line)
    # Đọc và ghi nội dung từ train+.lo
    with open("train+.lo", "r", encoding="utf-8") as f2:
        for line in f2:
            f_out.write(line)

# Gộp file .vi
with open("train_merged.vi", "w", encoding="utf-8") as f_out_vi:
    with open("train2023.vi", "r", encoding="utf-8") as f1_vi:
        for line in f1_vi:
            f_out_vi.write(line)
    with open("train+.vi", "r", encoding="utf-8") as f2_vi:
        for line in f2_vi:
            f_out_vi.write(line)