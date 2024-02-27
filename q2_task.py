class Task:
    def __init__(self, function_name, args):
        self.function_name = function_name
        self.args = args

    def execute(self):
        try:
            # Dynamically call the function and pass arguments
            func = getattr(self, self.function_name)
            result = func(*self.args)
            return result
        except Exception as e:
            print(f"Error executing task: {e}")
            return None

    def print(self, message):
        print(message)

    # Other task functions can be defined here

if __name__ == "__main__":
    # Example usage of Task class
    task = Task("print", ["Hello, world!"])
    task.execute()
