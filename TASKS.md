# Workshop Tasks — Build the Excel Data Cleaner

These tasks are intentionally **not implemented yet** in the starter app.

A paper was published about antimicrobial resistance in Campylobacter and, along with it, supplemental material was published. Yet the supplemental Excel file, which harbors results from antimicrobial resistance testing and whole genome sequencing, is in its current format not well machine-readable and thus needs data cleaning.

Use these files as your core workshop inputs:

- `sample_data/Tab.S1_Sample_overview.xlsx`
- `sample_data/s12864-024-10014-w.pdf`

## How to approach each task

For every task, use this mini-process before saying "done":

1. **Discovery evidence** (what files/data were inspected)
2. **Decision note** (what behavior choices were made and why)
3. **Implementation** (actual code changes)
4. **Verification** (how the behavior was validated)

## Recommended Cline workflow progression (use this order)

1. Start with targeted `@file` / `@folder` context.
2. Use **Plan Mode** when behavior is ambiguous.
3. Start using **Memory Bank** once naming/cleaning conventions become stable.
4. Use **subagents** for multi-stream analysis/refactor tasks.
5. Use **/deep-planning** for final integration tasks.

---

## Task 1 — Header row selection and application

- **Cline workflow:** targeted `@file` references.
- **Problem:** note rows above true headers make previews hard to interpret.
- **Reason:** without stable headers, downstream column operations become unreliable.
- **Outcome:** a consistent schema baseline for all later transformations.
- **You must decide:** how duplicate/empty header names are sanitized.
- **Acceptance checks:**
  - UI control for header row index;
  - cleaned preview uses selected row as headers;
  - duplicate/blank headers are handled safely.

## Task 2 — Manual column exclusion

- **Cline workflow:** targeted `@file` references.
- **Problem:** helper columns add noise (e.g., `Alias`, which is often not needed in cleaner views).
- **Reason:** irrelevant columns reduce readability and inflate transformation complexity.
- **Outcome:** a reduced working table focused on analytical columns.
- **You must decide:** whether exclusion affects preview only or export too.
- **Acceptance checks:**
  - multiselect for excluding columns;
  - excluded columns disappear from cleaned preview;
  - behavior is consistent in export-ready dataset.

## Task 3 — Empty column handling (use Plan Mode)

- **Cline workflow:** switch to **Plan Mode**, define explicit empty-value rules, then implement.
- **Problem:** empty columns clutter output and confuse users.
- **Reason:** hidden empty-value patterns can silently break assumptions in later transforms.
- **Outcome:** deterministic cleanup behavior for truly empty columns.
- **You must decide:** what counts as empty (`NaN`, empty strings, whitespace-only, placeholder tokens).
- **Acceptance checks:**
  - explicit behavior documented in code comments or docs;
  - toggle for removing fully empty columns;
  - visible feedback on which columns were removed.

## Task 4 — Split a column by custom separator (use Plan Mode)

- **Cline workflow:** switch to **Plan Mode**, define split behavior and edge-case handling, then implement targeted edits.
- **Problem:** multi-value cells need structural cleanup (e.g., `isolation source` values like `broiler, meat` or `broiler, cecum`).
- **Reason:** packed fields block direct grouping/filtering and reduce machine readability.
- **Outcome:** one value concept per column wherever possible.
- **Example:** split `isolation source` by comma into columns such as `host` (`broiler`) and `matrix` (`meat` / `cecum`) after trimming whitespace.
- **You must decide:** naming strategy and handling of uneven split lengths.
- **Acceptance checks:**
  - user can choose source column, delimiter, and new column names;
  - split works with inconsistent row shapes;
  - collision handling for generated column names is explicit.

## Task 5 — Expand code-like values to indicator columns

- **Cline workflow:** targeted `@file` references.
- **Problem:** code lists are hard to filter/analyze directly (e.g., one cell in `Res profile [EUCAMP2]` contains `CIP, NAL, TET`).
- **Reason:** analysts need explicit feature columns for reproducible filtering and summaries.
- **Outcome:** wide-format indicator columns for selected codes.
- **Example:** convert `Res profile [EUCAMP2] = "CIP, NAL, TET"` into columns like `has_CIP=1`, `has_NAL=1`, `has_TET=1` (and `0` for non-present codes).
- **You must decide:** values for present/absent indicators and whether to keep original column.
- **Acceptance checks:**
  - selectable detected codes;
  - generated indicator columns with deterministic naming;
  - clear handling of empty or unknown code cells.

## Task 6 — Add row filtering controls

- **Cline workflow:** targeted `@file` references.
- **Problem:** users need to keep/remove rows based on quick rules.
- **Reason:** downstream use cases often require scoped cohorts or quality subsets.
- **Outcome:** interactive data reduction without external spreadsheet edits.
- **You must decide:** minimum operator set for v1 (e.g., equals, contains, empty/not-empty).
- **Acceptance checks:**
  - simple interactive filter UI;
  - filtered row count feedback;
  - filters apply consistently before export.

## Task 7 — Persist cleaning conventions with Memory Bank

- **Cline workflow:** **Memory Bank** + targeted references.
- **Problem:** repeated decisions drift over time (naming, placeholder handling, trim rules).
- **Reason:** consistency across sessions is required for reproducible cleaning results.
- **Outcome:** stable project rules that reduce rework and divergence.
- **You must decide:** which conventions become project rules.
- **Acceptance checks:**
  - persisted conventions for at least: empty-like tokens, naming style, and default keep/drop behavior;
  - implementation follows stored conventions;
  - task notes show where Memory Bank helped avoid inconsistency.

## Task 8 — Use subagents for analysis and refactor

- **Cline workflow:** **subagents** for independent analysis streams.
- **Problem:** as features grow, transform flow and UI state can become tangled.
- **Reason:** multi-angle analysis uncovers structural issues that single-pass edits miss.
- **Outcome:** cleaner architecture with clearer boundaries and less fragile state.
- **You must decide:** which analysis streams are independent (e.g., pipeline order, state handling, UI sections).
- **Acceptance checks:**
  - use subagents for at least 2 independent analysis tracks;
  - consolidate findings into one refactor plan;
  - implement one concrete refactor (e.g., pipeline module extraction or clearer state model).

## Task 9 — Final integration with deep planning: cleaned Excel export

- **Cline workflow:** start with **/deep-planning**.
- **Problem:** final output must be reusable outside the app.
- **Reason:** workshop success depends on a portable result that can be shared and reused.
- **Outcome:** downloadable cleaned workbook aligned with selected transformations.
- **You must decide:** exact export scope (cleaned data only vs cleaned + transformation log).
- **Acceptance checks:**
  - working `.xlsx` download of cleaned dataset;
  - optional transformation-log sheet if implemented;
  - export content matches cleaned preview state.

## Task 10 — Final quality gate

- **Cline workflow:** targeted references + focused verification.
- **Problem:** workshop output should be stable and demonstrable.
- **Reason:** reliability is required before participants can trust or present outputs.
- **Outcome:** verified app behavior and documented final workflow.
- **You must decide:** minimum automated test coverage for confidence.
- **Acceptance checks:**
  - `pytest` passes;
  - app runs with sample workbook end-to-end;
  - README reflects final cleaner capabilities and workshop flow.

---

# 🚨 VERY HARD CHALLENGE TASK (EXPERT LEVEL)

## Task 11 — Migrate the Streamlit cleaner into a React app with Python API backend

- **Why this is very hard:** this is not a UI-only rewrite. It is an architecture migration from a single Python Streamlit app into a multi-part system (frontend + backend + API contracts + browser-tested flows).
- **Goal:** keep feature parity with the cleaner workflow while delivering a modern React frontend and stable Python backend for data processing.

### What to use

- **Deep-planning** to define architecture, migration phases, parity criteria, and rollback strategy.
- **Subagents** (at least 3) to parallelize work:
  1. backend/data-pipeline extraction and API contract design,
  2. React UI/state architecture and component decomposition,
  3. test/e2e strategy, migration risks, and verification plan.
- **Browser use** for end-to-end validation of upload, sheet selection, cleaning controls, preview updates, and cleaned-file download.
- **Tech stack suggestion:**
  - Frontend: React + TypeScript
  - Backend: FastAPI (Python)
  - Data processing: pandas/openpyxl (reuse cleaner logic)

### What to implement

1. **Extract cleaning logic from UI coupling** into backend service functions.
2. **Define API endpoints** (example set):
   - `POST /upload` → parse workbook, return sheet names and session/file id
   - `POST /preview` → return preview for current config
   - `POST /clean` → execute transformations and return summary/log
   - `GET /export/{id}` → download cleaned `.xlsx`
3. **Build React UI parity flow**:
   - upload file
   - pick worksheet
   - configure transforms
   - preview cleaned output
   - download cleaned workbook
4. **Implement robust state handling** for transformation settings and server responses.
5. **Add automated tests**:
   - backend unit tests for transformation pipeline
   - API tests for endpoints
   - frontend component/state tests
6. **Run browser-based e2e verification** against `sample_data/Tab.S1_Sample_overview.xlsx`.

### Minimum acceptance criteria

- React app supports the same end-to-end workflow as the Streamlit cleaner baseline.
- API contracts are documented and stable.
- Cleaned export is functionally correct and downloadable.
- E2E browser test (or scripted browser validation) passes for the core journey.
- A short migration note explains architecture decisions and known gaps.
