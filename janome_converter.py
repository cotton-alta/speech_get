# from janome.tokenizer import Tokenizer
from pykakasi import kakasi

# tokenizer = Tokenizer()
# 
# data_array = []
# 
# with open("sample.txt") as f:
#     for line in f:
#         print("-----------------------------")
#         # data_array.append(line)
#         for token in tokenizer.tokenize(line):
#             print("   " + str(token))
# 
# print(data_array)

kakasi = kakasi()
kakasi.setMode("J", "H")
conv = kakasi.getConverter()

with open("sample.txt") as f:
    for line in f:
        print(conv.do(line))
