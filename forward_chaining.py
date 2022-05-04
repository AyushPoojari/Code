import aima3.utils
import aima3.logic
def forward_chaining():
    clauses = []
    # Add first-order logic clauses (rules and fact)
    clauses.append(aima3.utils.expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
    clauses.append(aima3.utils.expr("Enemy(Nono, America)"))
    clauses.append(aima3.utils.expr("Owns(Nono, M1)"))
    clauses.append(aima3.utils.expr("Missile(M1)"))
    clauses.append(aima3.utils.expr("(Missile(x) & Owns(Nono, x)) ==> Sells(Colonel, x, Nono)"))
    clauses.append(aima3.utils.expr("American(Colonel)"))
    clauses.append(aima3.utils.expr("Missile(x) ==> Weapon(x)"))
    KB = aima3.logic.FolKB(clauses)
    KB.tell(aima3.utils.expr("Enemy(x, America) ==> Hostile(x)"))
    hostile = aima3.logic.fol_fc_ask(KB, aima3.utils.expr('Hostile(x)'))
    criminal = aima3.logic.fol_fc_ask(KB, aima3.utils.expr('Criminal(x)'))

    # Print answers
    print('enemy?')
    print(list(hostile))
    print('\nCriminal?')
    print(list(criminal))
    print()

if __name__ == "__main__":
    forward_chaining()
