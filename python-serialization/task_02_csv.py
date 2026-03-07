#!/usr/bin/python3
"""
This module provides a function to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named data.json.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion was successful, False if an error occurred.
    """
    try:
        # Step 1: Read the CSV file into a list of dictionaries
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader automatically uses the header row for dictionary keys
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Step 2: Serialize the list of dictionaries to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
