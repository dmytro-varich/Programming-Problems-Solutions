#!/bin/bash

echo "Seeding product links..."
python ./modules/1_parse_links.py

echo "Parsing product details and updating database..."
python ./modules/2_parse_data.py

echo "Done!"