1. **Open a Terminal or Command Prompt. Navigate to the desired directory**

2. **Create a Python Virtual Environment**:

   ```
   python -m venv myenv
   ```

3. **Activate the Virtual Environment**:

   ```
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

5. **Clone the Git Repository**:
   ```
   git clone https://github.com/botvyns/text_summarizer.git
   ```

6. **Navigate into the Cloned Repository Directory**:
   ```
   cd text_summarizer
   ```

7. **Install Dependencies**:
   ```
   python -m pip install -r requirements.txt
   ```

8. **Start the app what might take some time**:
   ```
   python main.py
   ```
10. **Open another command prompt/terminal with activated environment in the folder with cloned repo and run**
    ```
    python test_endpoint.py
    ```
    This might take some time too. After you should receive JSON with summary of the text provided in `test_endpoint.py`
