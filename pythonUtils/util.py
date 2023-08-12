import os

def create_readme(directory):
    readme_content = f"{directory}"
    readme_path = os.path.join(directory, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(readme_content)

# Get the current directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# List all directories at the same level as the script
directories = [d for d in os.listdir(script_directory) if os.path.isdir(d)]

# Create or update README.md in each directory
for directory in directories:
    create_readme(directory)

print("README.md files created or updated in all directories.")
