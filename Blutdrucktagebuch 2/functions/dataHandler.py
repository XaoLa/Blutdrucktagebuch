import json
import pandas as pd
from io import StringIO
from .github_contents import GithubContents


class DataHandler:
    def __init__(self, githubContents):
        self.github_contents = githubContents

    def save_object(self, obj, commit_message):
        """
        Save an object to a file in the GitHub repository.

        Args:
        - filepath: str, the file path where the object will be saved.
        - obj: dict, the object to be serialized and saved.
        - commit_message: str, the commit message for the operation.
        """
        self.github_contents.write_json("dataFile.csv", obj, commit_message)

    def load_object(self, filepath):
        """
        Load an object from a file in the GitHub repository.

        Args:
        - filepath: str, the file path from where the object will be loaded.

        Returns:
        - dict, the deserialized object.
        """
        return self.github_contents.read_json(filepath)

    def update_object(self, obj, commit_message):
        """
        Update an object in a file in the GitHub repository.

        Args:
        - filepath: str, the file path where the object is located.
        - obj: dict, the updated object to be saved.
        - commit_message: str, the commit message for the operation.
        """
        self.save_object("dataFile.csv", obj, commit_message)

    def delete_object(self, commit_message):
        """
        Delete an object from a file in the GitHub repository.

        Args:
        - filepath: str, the file path where the object is located.
        - commit_message: str, the commit message for the operation.
        """
        self.github_contents.write_text("dataFile.csv", "[]", commit_message)

# # Example usage:
# if __name__ == "__main__":
#     handler = FileHandler("<your_github_token>", "<your_github_username>", "<your_repository_name>")
#     # Example object to save
#     obj = {
#         "userId": "12345",
#         "x": 10.5,
#         "y": 20.6
#     }
#     # Save the object
#     handler.save_object("path/to/object.json", obj, "Saving object")

#     # Load the object
#     loaded_obj = handler.load_object("path/to/object.json")
#     print(loaded_obj)

#     # Update the object
#     updated_obj = {
#         "userId": "67890",
#         "x": 30.7,
#         "y": 40.8
#     }
#     handler.update_object("path/to/object.json", updated_obj, "Updating object")

#     # Delete the object
#     handler.delete_object("path/to/object.json", "Deleting object")
