# How to run it now
 
1. **Start Bri** (the evaluator fetches `/kb` as soon as it starts, so Bri must be running first):
```bash
   python bri_server.py        # http://localhost:8000
```

2. **Put your dataset in the `data/` folder** (a `.csv`). Two formats work:
   - *Prompts only:* columns `conv_id`, `user_message`. The script sends each prompt to Bri's `/chat` and records the reply and sources (e.g. `bri_test_cases.csv`).
   - *Recorded replies:* columns `conv_id`, `user_message`, `bot_reply`, `sources`. The script grades what is already in the file (e.g. `labeled_conversations.csv`). Extra columns are carried through.
3. **Run from the project root** (paths are relative to it):
```bash
   python automated_evaluator.py
```
4. **Enter the file name** when prompted: just the name inside `data/`, including `.csv` (e.g. `bri_test_cases.csv`).
5. **Read the results** in `data/updated_<file name>`. It is your input plus a `Judge_Remarks` column (`pass : <score>` or `fail - <severity>`), and the fetched `bot_reply` and `sources` columns if they were missing. 
Per-case details print to the console while it runs (if verbose = True).
---

# What changed since the previous version

This file lists **only** what is new or different. Everything not mentioned
(project goal, scoring weights, severity mapping, `log_test_suite.py`, the Task 1-4 documents) is unchanged.

## Evaluator can now fetch Bri's replies itself (`automated_evaluator.py`)

- **Before:** the script only graded a CSV that already contained `bot_reply` and `sources`. Input path was hard-coded to `data/labeled_conversations.csv`.
- **Now:** the script asks for a file name inside `data/`. If the CSV is **missing `bot_reply` and/or `sources`**, it sends each `user_message` to `POST /chat` (using `conv_id` as `session_id`), stores the reply and sources on the row, then grades as usual.
- Minimum columns for a prompts-only file: `conv_id`, `user_message`.
- Missing columns are now reported (`Missing columns: [...]`) instead of raising an error.


## Input and output files

| | Before | Now |
|---|---|---|
| Input | `data/labeled_conversations.csv` (fixed) | any `.csv` in `data/`, typed at the prompt |
| Output | `data/labeled_conversations_updated.csv` | `data/updated_<input file name>` |


`data/labeled_conversations_updated.csv` was removed; use `data/updated_labeled_conversations.csv`.

## Smaller code changes

- Added `clean_header()` for normalising column names. It is currently applied only inside the validation step, not in the main reading loop. (With help from AI)


## New data files

| File | What it is |
|---|---|
| `data/bri_test_cases.csv` | the 75 test-suite prompts as `conv_id,user_message` (prompts only, replies fetched live) (test_suite.json converted into csv) |
| `data/updated_bri_test_cases.csv` | live run: Bri's replies, sources, and `Judge_Remarks` for all 75 cases |
| `data/updated_labeled_conversations.csv` | re-run on the labeled set with the changes above |


## Known caveats of this version

- The deterministic check is tightly coupled to the knowledge base. Any change to the knowledge base may alter the deterministic changes.