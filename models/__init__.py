#!/usr/bin/python3
"""
Initialize File Storage.

This script creates a unique FileStorage instance for your application.
The FileStorage instance is responsible for
managing the storage and retrieval of data.
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()

# Load data from storage
storage.reload()
