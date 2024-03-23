"""
Import the FileStorage class from the file_storage module.
"""
from models.engine.file_storage import FileStorage
"""
Instantiate a FileStorage object to manage object storage.
"""
storage = FileStorage()
"""
Load any existing objects from the JSON file into the storage dictionary.
If the file doesn't exist, no action is taken.
"""
storage.reload()
