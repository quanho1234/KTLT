print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
input_string = input("Nhập dãy các từ: ")
words = input_string.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất là:", " ".join(longest_words))
