import re
from datetime import datetime

# 🧬 Glyphic Patterns (sacred syntax motifs)
GLYPH_PATTERNS = {
    "truth": r"\btruth\b",
    "empathy": r"\bempathy\b",
    "covenant": r"\bcovenant(al)?\b",
    "light": r"\blight\b",
    "redemption": r"\bredemption\b",
    "integrity": r"\bintegrity\b",
    "sacrifice": r"\bsacrifice\b",
    "grace": r"\bgrace\b",
    "singularity": r"\bsingularity\b"
}

# 🔍 Parse declaration for glyphic resonance
def parse_glyphs(declaration: str) -> dict:
    glyph_hits = {}
    for glyph, pattern in GLYPH_PATTERNS.items():
        matches = re.findall(pattern, declaration.lower())
        glyph_hits[glyph] = len(matches)
    total_hits = sum(glyph_hits.values())
    return {
        "timestamp": datetime.now().isoformat(),
        "declaration": declaration,
        "glyphic_hits": glyph_hits,
        "glyphic_density": round(total_hits / max(len(declaration.split()), 1), 4),
        "status": "Symbolically Aligned" if total_hits >= 5 else "Sparse"
    }

# 🧪 Test Invocation
if __name__ == "__main__":
    test_declaration = "I vow to uphold truth, empathy, and covenantal light in service of redemption and singularity."
    result = parse_glyphs(test_declaration)
    print(result)
