from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
Puzzle0_say = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(AKnave, Not(Puzzle0_say)),
    Implication(AKnight, Puzzle0_say)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
Puzzle1_say = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnave, Not(BKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(AKnave, Not(Puzzle1_say)),
    Implication(AKnight, Puzzle1_say)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
Puzzle2_A = Or(And(AKnight, BKnight), And(AKnave, BKnave))
Puzzle2_B = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnave, Not(BKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(AKnave, Not(Puzzle2_A)),
    Implication(AKnight, Puzzle2_A),
    Implication(BKnave, Not(Puzzle2_B)),
    Implication(BKnight, Puzzle2_B)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
Puzzle3_C = AKnight
knowledge3 = And(
    Or(AKnight, AKnave),
    Implication(AKnave, Not(AKnight)),
    Implication(AKnight, Not(AKnave)),
    Or(BKnight, BKnave),
    Implication(BKnave, Not(BKnight)),
    Implication(BKnight, Not(BKnave)),
    Or(CKnave, CKnight),
    Implication(CKnave, Not(CKnight)),
    Implication(CKnight, Not(CKnave)),

    AKnight,
    BKnave,
    Implication(CKnight, Puzzle3_C),
    Implication(CKnave, Not(Puzzle3_C))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
