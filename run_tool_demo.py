from agent import Agent


def main():
    agent = Agent()
    result = agent.call_tool('multiply', {'a': 5, 'b': 5})
    print('multiply(5,5) ->', result)


if __name__ == '__main__':
    main()
