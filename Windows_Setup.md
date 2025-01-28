# Windows Security Setup for Running Python Code

Follow these steps to add exclusions in Windows Security to ensure that your Python code runs without any interference:

1. **Open Windows Security:**
   - Click on the **Start** menu, type **Windows Security**, and press Enter to open the Windows Security settings.

2. **Access Virus & Threat Protection:**
   - In Windows Security, click on **Virus & Threat Protection**.

3. **Manage Virus & Threat Protection Settings:**
   - Scroll down and click on **Manage settings** under the "Virus & Threat Protection settings".

4. **Go to Exclusions:**
   - Scroll down again and click on **Add or remove exclusions**.

5. **Add Exclusion:**
   - Click on **Add an exclusion**, and choose **Folder**.

6. **Add the Folder Path:**
   - Select the folder where your Python code is stored, and click **Select Folder** to add the folder as an exclusion.

7. **Add the Python Code File:**
   - Click on **Add an exclusion** again, and this time select **File**.
   - Locate and select your Python code file (e.g., `keylogger.py`), then click **Open** to add the file as an exclusion.

8. **Save the Changes:**
   - The exclusions will now be added, and your Python code should run without interference from Windows Security.

Once you've completed these steps, you're ready to run your Python code without issues from Windows Security.

## Flowchart for Windows Security Setup for Python Code

```mermaid
graph TD;
    A[Open Windows Security] --> B[Click on Virus & Threat Protection];
    B --> C[Scroll down and click on Manage settings];
    C --> D[Scroll down and click on Add or remove exclusions];
    D --> E[Click Yes when prompted];
    E --> F[Click on Add an exclusion];
    F --> G[Choose Folder];
    G --> H[Select the folder where your Python code is stored];
    H --> I[Click Select Folder];
    I --> J[Click on Add an exclusion again];
    J --> K[Choose File];
    K --> L[Locate and select your Python code file];
    L --> M[Click Open];
    M --> N[Exclusions added successfully];
    N --> O[Run Python code without interference];
