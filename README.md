# InMemorySystem
## In-Memory File System Overview

### Data Structures Utilized:

The InMemoryFileSystem employs a nested dictionary as its primary data structure, serving as a representation of the file system hierarchy.

#### Nested Dictionary:

- **Purpose:**
  - Represents the hierarchical structure of directories and files.
  - Facilitates efficient navigation and storage of the file system.

- **Structure:**
  - Keys correspond to the full paths of directories or files.
  - Values are either subdirectories (nested dictionaries) or file content (represented as an empty string in this basic implementation).

### InMemoryFileSystem Overview:

The InMemoryFileSystem is a Python-based implementation of an in-memory file system, offering a command-line interface for user interaction. It allows users to perform various file system operations such as creating directories, files, navigating the hierarchy, and manipulating file content. Here's an overview:

#### File System Hierarchy Representation:

- **Representation:**
  - The file system is structured hierarchically using a nested dictionary.
  - Directories and files are modeled as keys, and their contents are values (nested dictionaries for directories or empty strings for file content).

#### Supported Operations:

- **mkdir(directory_name):**
  - Creates a new directory with the specified name in the current directory.

- **cd(path):**
  - Navigates to the specified directory or moves to the parent directory (..).

- **touch(file_name):**
  - Creates an empty file with the specified name in the current directory.

- **echo('text', 'file.txt'):**
  - Writes the provided text to the specified file.

- **rm(target):**
  - Removes the specified file or empty directory.

- **cp(source, destination):**
  - Copies the content of one file to another.

- **cat(file_name):**
  - Displays the content of the specified file.

#### User Interaction:

- **Interactive Loop:**
  - The system operates in a loop where users input commands.
  - The run method interprets user input, extracts the operation and arguments, and dynamically invokes the corresponding method.

#### Path Handling:

- **Robust Path Handling:**
  - Utilizes `os.path.join` and `os.path.dirname` for robust path handling.
  - Ensures platform independence.

#### Error Handling:

- **Informative Error Messages:**
  - Provides clear error messages for invalid commands or operations.
  - Handles scenarios such as creating existing directories/files or navigating to non-existent directories.

#### Design Decisions:

- **Dictionary Representation:**
  - The system uses a dictionary for simplicity and efficiency in representing the hierarchical structure.
  - An empty string represents file content for simplicity in this basic implementation.

#### Extensibility:

- **Flexible and Extensible:**
  - The system is designed to be extensible, accommodating the addition of new commands or enhancements to existing functionalities.

#### Platform Independence:

- **Cross-Platform Compatibility:**
  - The use of `os.path.join` and `os.path.dirname` ensures that the system is platform-independent regarding path handling.

#### Conclusion:

The InMemoryFileSystem provides a foundational in-memory file system, offering basic functionality while serving as a customizable base for more advanced use cases or integration into larger applications. The utilization of nested dictionaries and thoughtful design decisions enables flexibility, extensibility, and cross-platform compatibility.
