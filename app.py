import os
import shutil

class InMemoryFileSystem:
    def _init_(self):
        self.current_directory = '/'
        self.file_system = {}

    def mkdir(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        if new_directory_path in self.file_system:
            print(f"Error: Directory '{directory_name}' already exists.")
        else:
            self.file_system[new_directory_path] = {}
            print(f"Directory '{directory_name}' created.")

    def cd(self, path):
        if path == '/':
            self.current_directory = '/'
        elif path == '..':
            # Move to the parent directory
            self.current_directory = os.path.dirname(self.current_directory)
        else:
            # Navigate to the specified path
            new_path = os.path.join(self.current_directory, path)
            if new_path in self.file_system and isinstance(self.file_system[new_path], dict):
                self.current_directory = new_path
            else:
                print(f"Error: Directory '{path}' not found.")

    def touch(self, file_name):
        new_file_path = os.path.join(self.current_directory, file_name)
        if new_file_path in self.file_system:
            print(f"Error: File '{file_name}' already exists.")
        else:
            self.file_system[new_file_path] = ""
            print(f"File '{file_name}' created.")

    def echo(self, *args):
        if len(args) < 2:
            print("Error: Invalid syntax for echo. Usage: echo 'text' file.txt")
            return

        text = ' '.join(args[:-1])
        file_name = args[-1]
        file_path = os.path.join(self.current_directory, file_name)

        if file_path in self.file_system and isinstance(self.file_system[file_path], str):
            self.file_system[file_path] = text
            print(f"Text written to '{file_name}'.")
            print(f"Updated content: {text}")
        else:
            print(f"Error: File '{file_name}' not found.")

    def rm(self, target):
        target_path = os.path.join(self.current_directory, target)

        if target_path not in self.file_system:
            print(f"Error: Target file/directory '{target}' not found.")
        elif isinstance(self.file_system[target_path], dict) and self.file_system[target_path]:
            # Directory is not empty
            print(f"Error: Directory '{target}' is not empty. Remove its contents first.")
        else:
            self.file_system.pop(target_path)
            print(f"Removed '{target}'.")

    def cp(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)

        if source_path not in self.file_system:
            print(f"Error: Source file '{source}' not found.")
        elif destination_path in self.file_system and isinstance(self.file_system[destination_path], str):
            print(f"Error: Destination '{destination}' is an existing file. Cannot copy.")
        else:
            self.file_system[destination_path] = self.file_system[source_path]
            print(f"File '{source}' copied to '{destination}'.")

    def cat(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if file_path in self.file_system and isinstance(self.file_system[file_path], str):
            print(self.file_system[file_path])
        else:
            print(f"Error: File '{file_name}' not found.")

    def run(self):
        while True:
            try:
                command = input(f"\n{self.current_directory}$ ").split()
                if not command:
                    continue

                operation = command[0]
                args = command[1:]

                if operation == 'exit':
                    print("Exiting the file system.")
                    break
                elif hasattr(self, operation):
                    getattr(self, operation)(*args)
                else:
                    print(f"Error: Invalid operation '{operation}'. Available operations: mkdir, cd, touch, echo, rm, cp, cat, exit")
            except EOFError:
                print("\nEOFError: Exiting the file system.")
                break

if __name__ == "_main_":
    file_system = InMemoryFileSystem()
    file_system.run()