from pydantic import BaseModel, validator
from typing import Optional

class ImageUpload(BaseModel):
    file: Optional[bytes]

    @validator('file')
    def validate_file(cls, file):
        # Check file size
        max_size_mb = 4
        max_size_bytes = max_size_mb * 1024 * 1024
        if len(file) > max_size_bytes:
            raise ValueError(f"File size exceeds the maximum limit of {max_size_mb}MB")

        # Check file type
        if not file.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError("Invalid file type. Only PNG files are allowed.")

        return file