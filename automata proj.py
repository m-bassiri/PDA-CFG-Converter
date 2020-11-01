print('Hello and welcome to PDA/CFG converter!')
print('Created because of automata course project. 3962 semester - Isfahan University of Technology (IUT)')
print('By Mohammad Bassiri (9523773)')
print('Now please choose which one do you want to do?')
choice = int(input('1.Converting CFG to PDA\n2.Converting PDA to CFG\n'))
if choice == 1:
    print('Please enter the rules with this format: S --> Aa but remember:')
    print('1.DON\'T enter multiple rulse in one line like this: S --> Aa | Bb')
    print('2.Enter each rule in one line ending the rules with entering 0.')
    print('3.First variable is start variable.')
    print('4.Enter epsilon as 3!')
    rule = str(input())
    rules = []
    v = []
    sigma = []
    terminals = []
    delta = []
    while rule != '0':
        rules.append(rule)
        rule = str(input())
    start = rules[0][0]
    for s in rules:
        if s[0] not in v:
            v.append(s[0])
        rs = ''
        i = len(s) - 1
        while i!=5:
            rs += s[i]
            i -= 1
        delta.append((('eps', s[0]), rs))
        for c in s[6:len(s)]:
            if c.isupper() == False:
                if c not in terminals:
                    terminals.append(c)
    for c in terminals:
        delta.append(((c, c), 'eps'))
    print('---------------------------------------------')
    print('Here\'s your PDA specifications:')
    print('*Set of states(Q) = { q0 q1 q2 }')
    print('*Set of string alphabet(Sigma) = { ', end='')
    for c in terminals:
        print(c, end=' ')
    print('}')
    print('*Set of stack alphabet(Gamma) = { ', end='')
    for c in terminals:
        print(c, end=' ')
    if '3' not in terminals:
        print('eps ', end='')
    print('$ }')
    print('*Transition function (Delta):')
    print('delta(q0, eps, eps) = ($%s, q1)' % (start))
    for d in delta:
        print('delta(q1, %s, %s) = (%s ,q1)' % (d[0][0], d[0][1], d[1]))
    print('delta(q1, eps, $) = (eps, q2)')
    print('*Starting state (q0) = q0')
    print('*Accepting states (F) = {q2}')
