print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
class ReverseWords:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        
        words = self.sentence.split()
        reversed_sentence = ' '.join(reversed(words))
        return reversed_sentence

input_sentence = 'hello .py'


reverser = ReverseWords(input_sentence)
output_sentence = reverser.reverse()

print("Đầu vào:", input_sentence)
print("Đầu ra:", output_sentence)
