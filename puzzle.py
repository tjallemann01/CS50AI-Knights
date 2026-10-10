from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Biconditional(
        AKnight,
        And(AKnight, AKnave)
    )
)


# Puzzle 1
# A says "We are both knaves."
knowledge1 = And(
    # A debe ser caballero o bribón, pero no ambos
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B debe ser caballero o bribón, pero no ambos
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # La afirmación de A
    Biconditional(
        AKnight,
        And(AKnave, BKnave)
    )
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A pertenece exactamente a una categoría
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B pertenece exactamente a una categoría
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A afirma que ambos son del mismo tipo
    Biconditional(
        AKnight,
        Or(
            And(AKnight, BKnight),
            And(AKnave, BKnave)
        )
    ),

    # B afirma que son de tipos diferentes
    Biconditional(
        BKnight,
        Or(
            And(AKnight, BKnave),
            And(AKnave, BKnight)
        )
    )
)



# Puzzle 3
# A says either "I am a knight." or "I am a knave."
# B says "A said 'I am a knave.'"
# B says "C is a knave."
# C says "A is a knight."

ASaidKnight = Symbol("A said 'I am a knight'")
ASaidKnave = Symbol("A said 'I am a knave'")

knowledge3 = And(
    # Cada persona pertenece exactamente a una categoría
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A pronunció exactamente una de las dos frases
    Or(ASaidKnight, ASaidKnave),
    Not(And(ASaidKnight, ASaidKnave)),

    # Si A dijo "Soy caballero", debe respetar
    # la regla de caballeros y bribones
    Implication(
        ASaidKnight,
        Biconditional(AKnight, AKnight)
    ),

    # Si A dijo "Soy bribón", debe respetar
    # la regla de caballeros y bribones
    Implication(
        ASaidKnave,
        Biconditional(AKnight, AKnave)
    ),

    # B afirma que A dijo "Soy bribón"
    Biconditional(BKnight, ASaidKnave),

    # B también afirma que C es bribón
    Biconditional(BKnight, CKnave),

    # C afirma que A es caballero
    Biconditional(CKnight, AKnight)
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
