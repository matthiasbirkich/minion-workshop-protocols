"""Optional cross-check of SHARK-Seq primer Ta values with polymerase-tm.

The official NEB Tm Calculator remains the primary manufacturer reference:
https://tmcalculator.neb.com/
"""
from polymerase_tm import ta

pairs = [
    ("short MiFish-U-F / MarVer3R", "GTCGGTAAAACTCGTGCCAGC", "GGATTGCGCTGTTATCCC", "q5"),
    ("ChimeraF / FR1d", "AAGGACTACTTTGATAGAGT", "CACCTCAGGGTGTCCGAARAAYCARAA", "q5"),
    ("MarVer3F / MarVer3R", "AGACGAGAAGACCCTRTG", "GGATTGCGCTGTTATCCC", "phusion"),
    ("ChimeraF / miniSharkR5", "AAGGACTACTTTGATAGAGT", "CCTATTCAAACTAGGAGTC", "phusion"),
    ("ChimeraF / miniSharkR2", "AAGGACTACTTTGATAGAGT", "GGAATRATGGCTAATGTGTT", "phusion"),
]

for name, fwd, rev, pol in pairs:
    try:
        result = ta(fwd, rev, polymerase=pol)
        print(name, result)
    except Exception as exc:
        print(f"{name}: {exc}")
