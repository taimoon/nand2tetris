if __name__ == "__main__":
    from code_generator import Parser
    import sys
    path = sys.argv[1]
    Parser().write(path)