class AFD:
    def __init__(self):
        self.state = 'q00'
        self.transitions = {
            'q00': {'0': 'q10', '1': 'q01'},
            'q01': {'0': 'q11', '1': 'q00'},
            'q10': {'0': 'q00', '1': 'q11'},
            'q11': {'0': 'q01', '1': 'q10'}
        }
        self.accepting_states = {'q00'}

    def reset(self):
        self.state = 'q00'

    def process_input(self, input_string):
        self.reset()
        state_sequence = [self.state]
        for char in input_string:
            if char not in self.transitions[self.state]:
                raise ValueError(f"Caracter inválido '{char}' na entrada")
            self.state = self.transitions[self.state][char]
            state_sequence.append(self.state)
        return state_sequence, self.state in self.accepting_states

def main():
    afd = AFD()
    input_str = input("Digite a cadeia de entrada (composta por '0' e '1'): ").strip()
    try:
        state_sequence, result = afd.process_input(input_str)
        print(f"Cadeia: '{input_str}'")
        print(f"Sequência dos estados: {state_sequence}")
        print(f"A cadeia é aceita: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
