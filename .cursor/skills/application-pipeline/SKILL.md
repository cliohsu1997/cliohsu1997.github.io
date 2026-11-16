---
name: application-pipeline
description: >-
  Run the job-application pipeline for cliohsu1997.github.io: when given a
  job description or posting URL, scrape/confirm the JD, create the location
  and job folders under application/, write job_info.md, update
  application_list and recommendation_letters_to_send (Excel + PDF), and
  recompile list PDFs. HARD REQUIREMENT: every industry CV and cover letter
  must be a full dense exactly-1-page document (never short stubs). Use when
  the user adds a new JD, asks to update the application list, recommendation
  letters list, or says to follow the application pipeline.
---

# Application pipeline

Repo root: `cliohsu1997.github.io`. All paths below are under `application/`.

## HARD REQUIREMENT — full-page industry CV + cover letter (never skip)

**Non-negotiable for every industry / finance / consulting / MT / ops / quant / data / banking / trading role:**

1. **CV = full dense exactly 1 page.** Baseline = OHKF/FTI density. Required body:
   - Full Education + research line + CGA + full awards (Dean's List, University Scholarship, Academic Achievement Medal, Postgraduate studentship, Redbird)
   - Experience: RA + Teaching (full ratings); fold TA Coordinator into teaching if needed for space
   - Projects: **full** RPM (3 bullets) + **full** JMP (3 bullets) — never one-line stubs
   - Skills: Languages + Technical
   - Tailor **only** Professional Summary / light fit wording to the JD
2. **Cover letter = full dense exactly 1 page.** JD-mapped paragraphs with concrete evidence and numbers. Never a half-page / sparse letter.
3. **Verify with `pdfinfo` (or equivalent): Pages = 1** for both PDFs before telling the user the package is ready.
4. If overflow: trim summary or merge teaching lines — **never** gut projects or ship a short CV/letter.
5. Copy both full PDFs into `Application_Package_*`.
6. Canonical CV: `application/Hong Kong/Our Hong Kong Foundation - Researcher/Resume_HSU_Ke_Cheng_OHKF.tex`.
7. Also mirrored in `.cursor/rules/application-materials.mdc`.

**Forbidden:** short/thin/abbreviated industry resumes; stub project sections; half-page cover letters; “lighter CV for MT/ops” shortcuts.

## When to use

Use this skill whenever the user:

- Pastes a JD, posting URL, or says “add this job”
- Asks to update the application list or recommendation-letter list
- Says to follow the application / job pipeline

## Steps (do in order)

1. **Confirm the JD**
   - Prefer the official posting page (search or fetch). Also check English mirrors when they exist (EJM, POMS, department PDFs, etc.). Save facts in `job_info.md`.
   - **Deadlines:** if multiple posts list different deadlines, **use the earliest hard deadline** in `job_info.md`, `application_list`, and `recommendation_letters_to_send`. In `job_info.md`, briefly note the other dates and sources.
   - For this step only, scrape and record. Do not draft cover letters or research plans unless the user also asks for them.

2. **Location folder**
   - Create or reuse `application/<Location>/` (examples: `Beijing/`, `Shanghai/`, `Shenzhen/`, `Taiwan/`, `Japan/`, `Macau/`, `Singapore/`, `China/`).
   - Location = city or region of the job, not the employer’s brand.

3. **Job folder**
   - Create `application/<Location>/<Employer> - <Role>/`.
   - Write `job_info.md` with: employer, position, location, deadline, how to apply, link/email, role focus, **applicant materials**, and (if any) recommendation-letter notes pointing to the separate tracker.

4. **Application list**
   - Update `application/application_list.md` (grouped by location).
   - Update `application/application_list.tex` to match.
   - Compile PDF twice with `pdflatex` in `application/` (PowerShell: separate commands, no `&&`), then delete `.aux` / `.log` / `.out`.

5. **Recommendation letters (only if the JD requires them by email)**
   - Add a row **only** when writers / Crystal must **email** letters (not JOE / EJM / Interfolio / portal-only letter upload).
   - Add a row to `application/recommendation_letters_to_send.xlsx`.
   - Update `application/recommendation_letters_to_send.tex` and compile the PDF the same way.
   - **Materials column = recommendation / reference letter(s) only.** Never put cover letter, CV, JMP, or transcripts here.
   - **Subject column (Excel only):** fill `Subject` in the `.xlsx` for Crystal / the writers’ email. Do **not** add a Subject column to the `.tex` / `.pdf`.
     - If the JD **requires a specific subject** (for letters, or for the shared email inbox), use that **exact** required subject.
     - If the JD does **not** require a subject, use: `Recommendation Letters for Ke Cheng HSU — [Position Title]` (e.g. `Recommendation Letters for Ke Cheng HSU — Post Doctoral Fellow`).
     - If the only letter rule is “include the applicant’s full name,” the default format above already satisfies it.
   - **Do not** put letter-subject instructions in school-facing `Application_Email.md` or cover letters; subjects live in the Excel tracker for Crystal.
   - **Crystal:** department secretary at HKUST Economics sends letters on behalf of the referees. When asking Crystal to send, list each school’s To / Subject / referees / letter count from the Excel **To send** rows.

6. **Recommendation-letter list layout (Excel + `.tex` / PDF) — keep them unified**
   - **Excel is the source of truth.** After any Status / Sent? / row change, regenerate both Excel formatting and `recommendation_letters_to_send.tex` from the same sorted row list, then compile the PDF twice with `pdflatex` and delete `.aux` / `.log` / `.out`.
   - Keep rows in **three contiguous blocks**: **Sent** → **To send** → **Pending**, sorted **by deadline within each block** (then institution name).
   - Apply the **same three fills** to Excel columns A–J and to `.tex` `\rowcolor`:
     - **Sent** (`Sent?` = Yes; Status = `Sent`): light blue `#D6EAF8`
     - **To send** (`Sent?` = No; Status = `To send`): light green `#E2EFDA` — Crystal’s active queue
     - **Pending** (`Sent?` = No; Status = `Pending`): light yellow `#FFF2CC`
   - Excel formatting details:
     - Header row: dark blue `#1F4E79`, white bold text.
     - All data cells: wrap text + vertical center + thin borders.
     - Column widths (approx.): A Institution 48, B Position 28, C Deadline 12, D How 38, E Email 36, F Subject 42, G Materials 42, H Referees 12–42, I Status 10, J Sent? 10.
     - Row height: ~40 default; ~48–54 when Institution / Subject / email text is long (e.g. Guanghua), so the grid is tall enough.
   - PDF / `.tex` details:
     - Institution column wide enough for long names (about `p{4.3cm}`); `\arraystretch` about `1.2`.
     - No Subject column on the PDF (Excel only).
   - When the user marks jobs for Crystal, set Status to **To send** (`Sent?` = No). After Crystal sends, set Status to **Sent** and `Sent?` to **Yes**, then re-unify (re-sort, recolor Excel, regenerate `.tex`, recompile PDF).
   - If the user says “unify the recommendation list,” run this full Excel↔PDF sync even when row content did not change.

7. **Resumes / CVs (when drafting)**
   - Obey the **HARD REQUIREMENT** section above. No exceptions for “simple” or MT/ops roles.
   - Canonical template: `application/Hong Kong/Our Hong Kong Foundation - Researcher/Resume_HSU_Ke_Cheng_OHKF.tex`.

8. **Cover letters (when drafting)**
   - Obey the **HARD REQUIREMENT** section above (full dense 1 page for industry).
   - Do **not** put the AEA JOE ID / JOE listing number (or similar AEA reference codes) in the cover letter body or letterhead.
   - Prefer the school / unit name and position title only.
   - For email-path apps, say Crystal (secretary, Department of Economics, HKUST) will send the letters on behalf of the named referees.

## What goes where

| Tracker | Put here |
| --- | --- |
| **Application list** | What the **applicant** sends: cover letter, CV, JMP, transcripts, research statement, papers, forms. Note that letters are required if true, but do not list letters as applicant materials. |
| **Recommendation letters to send** | **Only** recommendation / reference letter(s). Count them (e.g. “Two recommendation letters”). Email **Subject** lives in the Excel file only. |

## Status meanings

- **Application list → Complete:** everything the **applicant** must submit is done. Recommendation letters may still be outstanding.
- **Application list → To apply / In progress:** materials not finished.
- **Recommendation letters:**
  - **Sent:** letters already emailed (`Sent?` = Yes).
  - **To send:** queued for Crystal / writers now (`Sent?` = No).
  - **Pending:** tracked but not queued yet (`Sent?` = No).
- **Never set Complete unless the user explicitly says to mark that job Complete.** Assembling a package, drafting a cover letter, or noting missing pieces (for example an official transcript) is not a request to mark Complete. Leave the existing status unchanged.

## Do not

- **Ship a short industry CV or short industry cover letter** (violates HARD REQUIREMENT).
- Invent nationality, deadlines, or materials not in the JD.
- Put recommendation letters in the application-list Materials / How-to-apply as if the applicant mails them, when the JD says writers send letters directly.
- Put AEA JOE / listing numbers in cover letters.
- Put the recommendation-letter Subject column on the letters `.tex` / `.pdf` (Excel only).
- Put letter-subject “suggested subject” lines in school-facing application emails.
- Mix JOE-only letter jobs into `recommendation_letters_to_send` (email tracker only).
- Draft full application essays unless the user asks (scraping + list updates is the default for “add this JD”).
- Leave `PIPELINE.md` as the source of truth; this skill is the source of truth. Keep `PIPELINE.md` as a short pointer if present.

## After finishing

Briefly tell the user: folder path, application-list row, whether a recommendation-letter row was added, what applicant materials the JD lists, and confirm **both CV and cover are full 1-page** (`pdfinfo` Pages: 1).
