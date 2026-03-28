# Brain parser usage

Install this requirements:

```bash
pip install selenium webdriver-manager playwright django && \
playwrigth install
```

## Selenium

   1. Go to the project folder:

      ```bash
      cd task_2-selenium-playwright
      ```

   2. Run the parser using the bash script:

      ```bash
      chmod +x ./tools/run_selenium.sh
      ./tools/run_selenium.sh
      ```

   3. Or run manually step by step:

      ```bash
      python ./modules/selenium_get_product_data.py
      ```

## Playwright

   1. Go to the project folder:

      ```bash
      cd task_2-selenium-playwright
      ```

   2. Run the parser using the bash script:

      ```bash
      chmod +x ./tools/run_playwright.sh
      ./tools/run_selenium.sh
      ```

   3. Or run manually step by step:

      ```bash
      python ./modules/playwright_get_product_data.py
      ```
