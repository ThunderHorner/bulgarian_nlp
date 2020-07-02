from text_processor import TextProcessor
f = TextProcessor('example_data/btv_terms.txt')

print(type(f.freq))
print(dict(f.freq))
f.freq.plot(20, cumulative=False)