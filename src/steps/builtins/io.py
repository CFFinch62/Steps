"""File I/O operations."""

import os
import csv as _csv
from typing import Optional

from ..types import (
    StepsValue, StepsText, StepsBoolean, StepsList, StepsTable,
    StepsNothing
)
from ..errors import StepsTypeError, StepsRuntimeError, ErrorCode, SourceLocation


def read_file(
    path: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsText:
    """Read entire contents of a text file."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"read_file requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call read_file with "myfile.txt"'
        )
    
    try:
        with open(path.value, 'r', encoding='utf-8') as f:
            return StepsText(f.read())
    except FileNotFoundError:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"File not found: '{path.value}'",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that the file path is correct."
        )
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not read file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions."
        )


def write_file(
    path: StepsValue,
    content: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNothing:
    """Write content to a text file (overwrites existing)."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"write_file requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call write_file with "myfile.txt", content'
        )
    
    text_content = content.as_text().value
    
    try:
        with open(path.value, 'w', encoding='utf-8') as f:
            f.write(text_content)
        return StepsNothing()
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not write to file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions and path."
        )


def append_file(
    path: StepsValue,
    content: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNothing:
    """Append content to a text file."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"append_file requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call append_file with "myfile.txt", content'
        )
    
    text_content = content.as_text().value
    
    try:
        with open(path.value, 'a', encoding='utf-8') as f:
            f.write(text_content)
        return StepsNothing()
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not append to file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions and path."
        )


def file_exists(
    path: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsBoolean:
    """Check if a file exists."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"file_exists requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call file_exists with "myfile.txt"'
        )
    
    return StepsBoolean(os.path.isfile(path.value))


def read_csv(
    path: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsList:
    """Read a CSV file and return a list of tables (each row is a table)."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"read_csv requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call read_csv with "data.csv"'
        )
    
    try:
        with open(path.value, 'r', encoding='utf-8', newline='') as f:
            reader = _csv.DictReader(f)
            rows = []
            for row in reader:
                # Convert each row (dict) to a StepsTable
                table = StepsTable({k: StepsText(v) for k, v in row.items()})
                rows.append(table)
            return StepsList(rows)
    except FileNotFoundError:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"CSV file not found: '{path.value}'",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check that the file path is correct."
        )
    except _csv.Error as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"CSV parsing error in '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check the CSV file format."
        )


def write_csv(
    path: StepsValue,
    data: StepsValue,
    location: Optional[SourceLocation] = None
) -> StepsNothing:
    """Write a list of tables to a CSV file."""
    if not isinstance(path, StepsText):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"write_csv requires a text path, got {path.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint='Use: call write_csv with "output.csv", data_list'
        )
    
    if not isinstance(data, StepsList):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message=f"write_csv requires a list of tables, got {data.type_name()}.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Data must be a list of tables."
        )
    
    if data.length() == 0:
        # Write empty file
        try:
            with open(path.value, 'w', encoding='utf-8', newline='') as f:
                pass
            return StepsNothing()
        except IOError as e:
            raise StepsRuntimeError(
                code=ErrorCode.E407,
                message=f"Could not write CSV file '{path.value}': {e}",
                file=location.file if location else None,
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint="Check file permissions and path."
            )
    
    # Get headers from first row
    first_row = data.elements[0]
    if not isinstance(first_row, StepsTable):
        raise StepsTypeError(
            code=ErrorCode.E302,
            message="write_csv: each element must be a table.",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Each row should be a table with key-value pairs."
        )
    
    headers = list(first_row.pairs.keys())
    
    try:
        with open(path.value, 'w', encoding='utf-8', newline='') as f:
            writer = _csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for row in data.elements:
                if isinstance(row, StepsTable):
                    row_dict = {k: v.as_text().value for k, v in row.pairs.items()}
                    writer.writerow(row_dict)
        return StepsNothing()
    except IOError as e:
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Could not write CSV file '{path.value}': {e}",
            file=location.file if location else None,
            line=location.line if location else 0,
            column=location.column if location else 0,
            hint="Check file permissions and path."
        )
