# loan_explainer.py
# Week 2 · Tiny local prototype
# Idea #1: Loan term explainer
# 用户群体：看不懂学生贷款 FAQ 的大学生
# 任务：输入术语 → 返回解释
# Does not: 不给个人借贷建议 / 不推荐贷款机构 / 不替人决定

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "loan_terms.json"

def load_terms():
    """Load the loan terms glossary from JSON."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["terms"]

def find_term(terms, query):
    """Find the best matching term for the user's query.
    Strategy: exact match > substring match > None.
    """
    q = query.strip().lower()
    # 1. exact match
    for t in terms:
        if t["term"] == q:
            return t
    # 2. substring match (bidirectional)
    for t in terms:
        if q in t["term"] or t["term"] in q:
            return t
    return None

def format_term(t):
    """Pretty-print a single term explanation."""
    lines = [f"\n  {t['term'].upper()}"]
    lines.append(f"  {t['short']}")
    if t.get("example"):
        lines.append(f"  例: {t['example']}")
    if t.get("needs"):
        lines.append(f"  限制: {t['needs']}")
    return "\n".join(lines)

def main():
    terms = load_terms()
    print(f"Loaded {len(terms)} loan terms.")
    print("输入一个贷款术语（比如 'grace period'），或者 'quit' 退出。\n")

    while True:
        try:
            q = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break
        if not q:
            continue
        if q.lower() in {"quit", "exit", "q"}:
            print("Bye.")
            break
        if q.lower() in {"list", "?"}:
            print("\n  可查的术语:")
            for t in terms:
                print(f"    - {t['term']}")
            print()
            continue
        match = find_term(terms, q)
        if match:
            print(format_term(match))
        else:
            print(f"\n  没找到 '{q}'。试试 list 看所有术语，或换个问法。\n")

if __name__ == "__main__":
    main()