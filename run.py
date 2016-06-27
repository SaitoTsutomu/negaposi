import sys
if len(sys.argv) > 1:
    from janome.tokenizer import Tokenizer
    from collections import defaultdict
    with open("pn.csv.m3.120408.trim") as fp:
        ss = [s.split() for s in fp.read().strip().split('\n')]
    dc = defaultdict(int, {s:(1 if f=='p' else -1) for s, f, *_ in ss if f != 'e'})
    with open("wago.121808.pn") as fp:
        ss = [s.split() for s in fp.read().strip().split('\n')]
    dc.update({s[1]:(1 if s[0].startswith('ポジ') else -1) for s in ss if len(s) == 2})
    t = Tokenizer()
    n = sum(dc[token.base_form] for token in t.tokenize(sys.argv[1]))
    print('ポジ' if n > 0 else 'ネガ' if n < 0 else '中立')

