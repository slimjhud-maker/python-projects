import math, random, string
from collections import Counter

ALPHA = string.ascii_uppercase
EN_FREQ = {'E':12.70,'T':9.06,'A':8.17,'O':7.51,'I':6.97,'N':6.75,'S':6.33,'H':6.09,'R':5.99,'D':4.25,'L':4.03,'C':2.78,'U':2.76,'M':2.41,'W':2.36,'F':2.23,'G':2.02,'Y':1.97,'P':1.93,'B':1.49,'V':0.98,'K':0.77,'J':0.15,'X':0.15,'Q':0.10,'Z':0.07}
EN_FREQ_VEC = [EN_FREQ[c] for c in ALPHA]
COMMON_WORDS = {"THE","AND","THAT","HAVE","FOR","NOT","WITH","YOU","THIS","BUT","HIS","FROM","THEY","SAY","HER","SHE","OR","WILL","MY","ONE","ALL","WOULD","THERE","THEIR","WHAT","SO","UP","OUT","IF","ABOUT"}
TRIGRAMS = {"THE":1.0,"ING":0.9,"AND":0.85,"HER":0.6,"ERE":0.5,"ENT":0.5,"THA":0.5,"NTH":0.45,"WAS":0.45,"ETH":0.4,"FOR":0.4,"DTH":0.3}

def clean_text(s): return "".join(ch for ch in s.upper() if ch in ALPHA)
def letter_freq_score(text):
    if not text: return -float("inf")
    counts = Counter(text); total = sum(counts.values())
    vec = [100.0 * counts.get(c,0)/total for c in ALPHA]
    chi = sum((obs-exp)**2/(exp+1e-9) for obs,exp in zip(vec,EN_FREQ_VEC))
    return -chi
def word_score(text): return sum(1 for w in COMMON_WORDS if w in set(text.split()))*1.0
def trigram_score(text): return sum(TRIGRAMS.get(text[i:i+3],0.0) for i in range(len(text)-2))/max(1,len(text))
def total_score(text): t=clean_text(text); return letter_freq_score(t)+word_score(text.upper())+trigram_score(t)

def caesar_shift(s,k):
    out=[]
    for ch in s:
        if ch.upper() in ALPHA:
            base='A' if ch.isupper() else 'a'
            idx=(ord(ch.upper())-65+k)%26
            out.append(chr(ord(base)+idx))
        else: out.append(ch)
    return "".join(out)
def break_caesar(cipher):
    best=None
    for k in range(26):
        pt=caesar_shift(cipher,-k)
        score=total_score(pt.upper())
        if not best or score>best[2]:
            best=("Caesar",f"shift={k}",score,pt)
    return best

def vigenere_decrypt(cipher,key):
    out=[]; j=0
    for ch in cipher:
        if ch.upper() in ALPHA:
            k=ALPHA.index(key[j%len(key)])
            base='A' if ch.isupper() else 'a'
            idx=(ord(ch.upper())-65-k)%26
            out.append(chr(ord(base)+idx)); j+=1
        else: out.append(ch)
    return "".join(out)

def break_vigenere(cipher):
    # Simplified: try trivial keys only for demo
    key="AAA"
    pt=vigenere_decrypt(cipher,key)
    return ("Vigenere",f"key≈{key}",total_score(pt.upper()),pt)

def initial_subst_key(cipher):
    freq_order_en=[c for c,_ in sorted(EN_FREQ.items(),key=lambda x:-x[1])]
    counts=Counter(clean_text(cipher)); freq_order_ct=[c for c,_ in counts.most_common()]
    mapping={c:freq_order_en[i] for i,c in enumerate(freq_order_ct) if i<len(freq_order_en)}
    unused=[c for c in ALPHA if c not in mapping.values()]
    for c in ALPHA:
        if c not in mapping: mapping[c]=unused.pop(0) if unused else 'X'
    return mapping
def apply_subst(cipher,mapping):
    out=[]
    for ch in cipher:
        if ch.upper() in ALPHA:
            m=mapping[ch.upper()]
            out.append(m if ch.isupper() else m.lower())
        else: out.append(ch)
    return "".join(out)
def break_substitution(cipher):
    mapping=initial_subst_key(cipher)
    pt=apply_subst(cipher,mapping)
    return ("Substitution","freq-map",total_score(pt.upper()),pt)

def break_code(cipher):
    candidates=[break_caesar(cipher),break_vigenere(cipher),break_substitution(cipher)]
    candidates=[c for c in candidates if c]
    candidates.sort(key=lambda x:x[2],reverse=True)
    return candidates[0]

def main():
    cipher=input("Enter your coded message: ").strip()
    method,params,score,pt=break_code(cipher)
    print(f"Best guess:\n[{method}] {params} | score={score:.3f}\n{pt}")

if __name__=="__main__": main()