text = tuple(sorted(input()))
text_set = sorted(set(text))

for symbol in text_set:
    count = text.count(symbol)
    print(f"{symbol}: {count} time/s")

