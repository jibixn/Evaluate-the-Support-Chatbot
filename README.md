
# Bri Chatbot Evaluation

Evaluates Bri's chatbot responses using semantic similarity, keyword matching, and an LLM-based judge.

## Assumptions
 - Assumption 1: 

     The expected behaviour of Bri -->

     - Bri must be polite at all times.
	- Bri must satisfy the users reasonable requests.
	- Bri must not hallucinate and provide incorrect information.
	- Bri must always refer to its knowledge base.
	- Bri must be secure and must not leak private and sensitive data.
	- Bri’s responses must be relevant to the query.
	- Bri must ask for clarifications if there is an ambiguous query.
     - Bri shall only answer questions related to Brightline plans, billing, returns or roaming
     - Bri has access to all required information related to Brightline plans, billing, returns or roaming

- Assumption 2: 

     Bri is deployed to multiple countries as the knowdge base mentions support for Mexico and Canada 

- Assumption 3:

     Newer versions of Bri will be available in a .csv file similar to "labelled_conversations.csv" for evaluation.

- Assumption 4:

     Bri provides repetitive answers due to strict rules.

- Assumption 5:

     Provided datasets will be mostly clean, though the evaluator validates it for mandatory features.

- Assumption 6:

     Human labels are not always correct. (This assumption is evidence backed).

## Requirements

- Python 3.10+
- Bri API running at `http://localhost:8000`
- Google Gemini API key

## Project Structure

```text
project/
├── .env
├── automated_evaluator.py
├── log_test_suite.py
└── documents/
|   ├── Task 1 - Test Suite Log.xlsx
|   └── Task 2 - Results Table.xlsx
|   └── Task 3 - Can you trust your grader.docx
|   └── Task 4 - Ship or don't ship.docx
└── data/
    ├── labeled_conversations.csv
    └── labeled_conversations_updated.csv
    └── test_results.csv
    └── test_suite.json
```

## File Paths

- **Input:** `data/labeled_conversations.csv`
- **Output:** `data/labeled_conversations_updated.csv`
- **Knowledge Base API:** `http://localhost:8000/kb`

The input CSV must contain these columns:

- `conv_id`
- `user_message`
- `bot_reply`
- `sources`

The script adds a `Judge_Remarks` column to the output CSV.

## Models Used

- **LLM Judge:** `gemini-3.5-flash` via `ChatGoogleGenerativeAI`
- **Embedding Model:** `BAAI/bge-small-en-v1.5` via `HuggingFaceEmbeddings`


## Setup

Install the dependencies:

```bash
pip install langchain-google-genai langchain-core langchain-huggingface pydantic requests numpy python-dotenv
```

Create a `.env` file in the project root and configure your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

Ensure the `data/` directory contains `labeled_conversations.csv`.

## How to Run

1. Start the Bri API.
2. Ensure the API endpoint `http://localhost:8000/kb` is accessible.
3. Run the script from the project root:

```bash
python automated_evaluator.py
```


The evaluation results are saved to `data/labeled_conversations_updated.csv`.
The results can be printed in the terminal with additional information such as scoring, explanations etc. if verbose(False by default) is set to True.

## Operational Cost
For a dataset with 57 examples,
for evaluation, 

- Time taken is approximately 6 minutes
- Cost is approximately Rs 35

Per run 

## AI Usage

1.	Test Suite creation

     The prompt categories I defined are: 
     -	Normal
     -	Ambiguous
     -	Impossible
     -	Prompt Injection
     -	Hallucination 
     -	Out of scope (General Knowledge)
     -	criticism

     I have 7 categories and 10 test cases each (Except for prompt injection – 20 and criticism - 5) would give me 75.
     I have made 2 example test cases for each category and 
     
     *used an AI model generate the rest of the examples.*


2.	Used AI to check the syntax for working with csv in python

3.	Used AI to modify system prompt (More Clarity).

4.	Used AI for debugging some issues faced.


## Additional Information
The test suite is a json file within the data folder.

It can be automatically logged by running 
```bash
python log_test_suite.py
```
This logs all responses into 
```bash
test_results.csv
```

Errors have to be manually selected.

##### The issue log, results table, analysis and recommendation that are required by the assignment is available within the documents folder.
