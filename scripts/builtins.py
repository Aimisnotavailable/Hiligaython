class Builtins:
    def is_builtin(self, command):
        return command in ['cd', 'exit', 'help']

    def execute(self, command, args):
        if command == 'cd':
            try:
                import os
                os.chdir(args[0] if args else os.path.expanduser('~'))
                return f"Changed directory to {os.getcwd()}"
            except Exception as e:
                return f"cd error: {str(e)}"
        elif command == 'exit':
            return "Exiting shell."
        elif command == 'help':
            return "Available commands: cd, exit, help"
        else:
            return f"{command}: command not found"