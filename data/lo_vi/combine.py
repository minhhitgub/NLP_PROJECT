with open("train2023.lo", "r", encoding="utf-8") as f_lo, \
     open("train2023.vi", "r", encoding="utf-8") as f_vi, \
     open("combined_train1.txt", "w", encoding="utf-8") as f_out:

    # Ghi toàn bộ các dòng tiếng Lào trước
    for line in f_lo:
        f_out.write(line)

    # Ghi toàn bộ các dòng tiếng Việt tiếp theo
    for line in f_vi:
        f_out.write(line)
