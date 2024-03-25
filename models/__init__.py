"""
Import the FileStorage class from the file_storage module.
"""
import models.engine.file_storage as file_storage
"""
Instantiate a FileStorage object to manage object storage.
"""
storage = file_storage.FileStorage()
"""
Load any existing objects from the JSON file into the storage dictionary.
If the file doesn't exist, no action is taken.
"""
storage.reload()
