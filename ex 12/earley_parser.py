class State:
    def __init__(self, lhs, rhs, dot, start):
        self.lhs = lhs
        self.rhs = rhs
        self.dot = dot
        self.start = start

    def __eq__(self, other):
        return (self.lhs, self.rhs, self.dot, self.start) == \
               (other.lhs, other.rhs, other.dot, other.start)

    def __hash__(self):
        return hash((self.lhs, tuple(self.rhs), self.dot, self.start))

    def is_complete(self):
        return self.dot >= len(self.rhs)

    def next_symbol(self):
        if self.dot < len(self.rhs):
            return self.rhs[self.dot]
        return None

    def advance(self):
        return State(self.lhs, self.rhs, self.dot + 1, self.start)

    def __str__(self):
        rhs = self.rhs[:]
        rhs.insert(self.dot, "•")
        return f"{self.lhs} -> {' '.join(rhs)}, [{self.start}]"


def earley_parse(grammar, start_symbol, tokens):
    chart = [set() for _ in range(len(tokens) + 1)]

    start_state = State("GAMMA", [start_symbol], 0, 0)
    chart[0].add(start_state)

    for i in range(len(chart)):
        changed = True
        while changed:
            changed = False

            for state in list(chart[i]):
                if not state.is_complete():
                    symbol = state.next_symbol()

                    # Predictor
                    if symbol in grammar:
                        for production in grammar[symbol]:
                            new_state = State(symbol, production, 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    # Scanner
                    elif i < len(tokens) and symbol == tokens[i]:
                        chart[i + 1].add(state.advance())

                # Completer
                else:
                    for old_state in list(chart[state.start]):
                        if (not old_state.is_complete() and
                                old_state.next_symbol() == state.lhs):
                            new_state = old_state.advance()
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    final_state = State("GAMMA", [start_symbol], 1, 0)

    if final_state in chart[len(tokens)]:
        print("String Accepted")
    else:
        print("String Rejected")


# Grammar
grammar = {
    "S": [["a", "S", "b"], ["a", "b"]]
}

# Input string
inp = input("Enter string (e.g., aabb): ")

tokens = list(inp)

earley_parse(grammar, "S", tokens)
