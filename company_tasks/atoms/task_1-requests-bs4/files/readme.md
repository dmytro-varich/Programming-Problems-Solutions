# Brain parser usage

1. Install this requirements:

   ```bash
   pip install requests beautifulsoup4 django
   ```

2. Go to the project folder:

   ```bash
   cd task_1-requests-bs4
   ```

3. Run the parser using the bash script:

   ```bash
   chmod +x ./tools/run.sh
   ./tools/run.sh
   ```

4. Or run manually step by step:

   ```bash
   python ./modules/1_parse_links.py   # Add a link to the database
   python ./modules/2_parse_data.py    # Parse product data
   ```
