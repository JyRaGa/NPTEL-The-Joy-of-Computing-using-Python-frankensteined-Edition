# Repository structure audit

Snapshot: 2026-10-09 · 591 files (≈126 MB) · scope: **past questions and answers** for NPTEL *The Joy of Computing using Python* (IIT Ropar, Prof. Sudarshan Iyengar).
Lecture source code and its sample data are logged here only so they can be removed.

Legend: ⭐ keep (unique Q&A) · ♻️ duplicate · 🧹 drop (not Q&A / junk) · ⚠️ needs work

---

## 1. Where this repo came from

| Layer | Origin | Evidence |
|---|---|---|
| Base (root `Assignments/`, `NOTES/`, `Excali-notes/`, `Source-codes/`, `README.md`, `JOCP ROAD MAP.md`, `LICENSE`) | Fork of `gxuxhxm/NPTEL-The-Joy-of-Computing-using-Python` (Goutham S K, Oct 2023, MIT) | `git remote upstream`, first commits 2023-10-28 |
| `second repo/` | `kishanrajput23/NPTEL-The-Joy-of-Computing-using-Python` (Kishan Kumar Rai, 2021, MIT) | its own `LICENSE`, README links |
| `third repo/` | Unknown author, Jupyter-notebook repo for the Jul–Dec 2023 run | `EXAM_PATTERN.md` says "October 2023" |
| `4th repo/` | Unknown author, 2020–21 lecture code + quiz PDFs | `.DS_Store` files (macOS), `noc2x` codes in PDFs |
| `5th repo/` | Answer-site style markdown (SEO text, Telegram/"join" spam) | covers 2023–2026 runs |
| Root-level PDFs + `Question Papers/` | Collected by you from Scribd, YouTube channel "getpythoncode", swayam print-outs | see `Question Papers/relevant urls.md` |

**Session tagging rule:** NPTEL runs each course twice a year. If Week 1 starts in Dec/Jan, it's the **Jan** session (runs Jan–Apr, exam late Apr/May). If Week 1 starts in Jul/Aug, it's the **Jul** session (runs Jul–Oct, exam late Oct/Nov). Files are tagged `Jan-YYYY` / `Jul-YYYY`. 2020 had a COVID off-cycle run that started in September, tagged `Sep-2020`. The older "Jan-Aug 2020" name refers to the Jan-2020 run, which was stretched by COVID.

NPTEL course codes found (used to date each file):
`noc18_cs35` (Jul-2018) · `noc20_cs35` (Jan-2020) · `noc20_cs83` (Sep-2020) · `noc21_cs32` (Jan-2021) · `noc21_cs75` (Jul-2021) · `noc22_cs31` (Jan-2022) · `noc23_cs108` (Jul-2023) · `noc24_cs57` (Jan-2024) · `noc24_cs113` (Jul-2024) · `noc25_cs69` (Jan-2025) · `noc25_cs103` (Jul-2025) · `noc26_cs84` (Jan-2026)

---

## 2. Folder-by-folder

### Root
| Path | What it is | Verdict |
|---|---|---|
| `README.md` | 1 line from the upstream fork ("Archived course notes…open in Obsidian") | ⚠️ rewrite |
| `JOCP ROAD MAP.md` | Obsidian checklist of `[[WEEK n]]` links | 🧹 or fold into README |
| `LICENSE` | MIT, © 2023 Goutham S K | ⚠️ decide licence (see §5) |
| `JOY-OF-COMPUTING-USING-PYTHON.pdf` | swayam print, **Jul–Dec 2024** (`noc24_cs113`), Weeks 0–12, 84 p, 129 "Accepted Answers" | ⭐ |
| `Python-NPTEL.pdf` | swayam print, **Jan–Apr 2025** (`noc25_cs69`), Weeks 1–12, 66 p, 118 answers | ⭐ |
| `The-Joy-of-Computing-Using-Python-JAN-2025.pdf` | Typed Jan 2025 assignment Qs, 38 p, inline `Ans.` lines | ⭐ (overlaps Python-NPTEL.pdf, different format) |
| `Joy-Jan-Aug-2020.pdf` | **Jan–Apr 2020** (`noc20_cs35`), 72 p | ♻️ same text as `Question Papers/JOC Jan-Aug 2020.pdf` (different bytes, line-wrap only) |
| `The-Joy-of-Computing-Using-Python-PART-1/2/3.pdf` | "IMP QUESTIONS" Scribd sets, 5–6 p each, 16 Q+A each (48 total), undated | ⭐ small |
| `Nptel-Python-Mcqs.pdf` | 2 p generic MCQs with answers, looks AI-generated, not from the course | 🧹 low value |
| `NptelQuizzes.pdf` | 70 p, **Sep-2020** run: typed answer sheets with explanations for Wk1–8 + portal printouts Wk9–12. Text layer is a letter-substitution cipher, **now decoded** → `_incoming/scribd/JOC Sep-2020 Wk1-12 answers (decoded text of NptelQuizzes).txt` via `_incoming/nq_decode.py`. Source: <https://www.scribd.com/document/521374064/NptelQuizzes> | ⭐ use decoded text |

### `Question Papers/` (29 MB)
| File | Term | Notes | Verdict |
|---|---|---|---|
| `JOC 2018.pdf` | 2018 (`noc18_cs35`), 37 p, 88 answers | identical to 2 other copies | ⭐ canonical copy |
| `JOC Jan-Aug 2020.pdf` | Jan–Apr 2020, 72 p, 118 answers | identical to `4th repo/…/3. Joy Jan-Aug 2020.pdf` & second-repo copy | ⭐ canonical |
| `JOC Sep-Dec 2020.pdf` | Sep–Dec 2020 (`noc20_cs83`), 60 p, 119 answers | identical to second-repo copy; same text as 4th-repo copy | ⭐ canonical |
| `JOC Jan-Apr 2021.pdf` | Jan–Apr 2021, 56 p, **scanned images, no text layer**, watermarked "Coding Buddies" | identical to second-repo copy | ♻️ prefer the text PDF in `4th repo/` |
| `JOC_2022_APRIL_DEC.pdf` | 2022 (term unclear, probably Jul–Dec 2022), 61 p, **scanned**, "getpythoncode" watermark | only source for 2022 H2 | ⭐ ⚠️ OCR |
| `34 questions asked in JOC final center exam morning session.pdf` | Proctored **final exam** recollection, 25 p, screenshot per question, watermarked | only final-exam material | ⭐ ⚠️ OCR |
| `relevant urls.md` | Scribd + kishanrajput23 + 4 YouTube links | keep as sources list |

### `Assignments/` (12 md, 56 KB) — Jul–Dec 2023 weekly quizzes, Weeks 1–12
- Converted by ChatGPT (lines like "Certainly, here are the MCQs…"); answers marked with ✓ / **Correct Answer:**.
- Same questions as `third repo/` notebooks (e.g. W7 Q1 "Values of CSV files are separated by?").
- ⚠️ **64 broken Obsidian embeds** `![[Pasted image 2023…]]` — the images were never committed. Code-output questions are unreadable without them; recover from `third repo` notebook screenshots.
- Verdict: ⭐ keep, clean up.

### `NOTES/` (12 md, 172 KB), `Excali-notes/` (2 Excalidraw md)
Lecture notes per week (Scratch, magic square, FLAMES, PageRank, …). Not Q&A. 🧹 or move to an optional `notes/` folder — your call.

### `Source-codes/` (44 files, 9.1 MB)
Lecture demo programs Weeks 2–12 (FizzBuzz, Magic Square, FLAMES, PageRank…) + `DNA_data.txt`, a `.wav`, `input.png`. 🧹

### `second repo/NPTEL-The-Joy-of-Computing-using-Python-main/` (213 files, 18 MB)
| Subfolder | Content | Verdict |
|---|---|---|
| `Week0/`…`Week12/` (`README.md` each) | **Jan–Apr 2021** (`noc21_cs32`) weekly quiz, markdown, ✅ on answer, ~130 Qs | ⭐ |
| `Week2/`…`Week12/*.py` | Jan–Apr 2021 **programming-assignment solutions** (no problem statements) | ⭐ answers (code, but they *are* Q&A) |
| `Aug - Dec 2021 JOC Course/Week 0–12/README.md` | **Jul–Dec 2021** (`noc21_cs75`) quizzes, 260 Qs ✅ | ⭐ |
| `Aug - Dec 2021 JOC Course/Week n/*.py` | Jul–Dec 2021 programming-assignment solutions (31 files) | ⭐ |
| `Aug - Dec 2021 JOC Course/Online Programming Test Solution/` | Morning/Evening session solutions for the online programming exam | ⭐ |
| `Jan - Apr 2022 JOC Course/Week 0–12/README.md` + `*.py` | **Jan–Apr 2022** (`noc22_cs31`) quizzes 260 Qs ✅ + 33 PA solutions | ⭐ |
| `Online Programming Test Solution/` | 2021 online programming test solutions (`README.md` + 3 `.py`) | ⭐ |
| `JOC previous years weekly quizes/` | 4 PDFs, all byte-identical to `Question Papers/` | ♻️ delete |
| `Exam Pattern.md`, `Aug-Dec 2021/Exam Pattern.md` | exam format notes | ⭐ merge into one exam-pattern page |
| `NPTEL-Course-Lecture Programmes/` | 45 lecture `.py` + images/gexf/ipynb | 🧹 |
| `README.md`, `Code Of Conduct.md`, `LICENSE` | upstream boilerplate | 🧹 (keep attribution) |

⚠️ Quiz READMEs hot-link **~465 question/option images** from `storage.googleapis.com/swayam-node1-production…` (still returning 200 today). If NPTEL purges them, many questions become blank → mirror them locally.

### `third repo/` (117 files, 46 MB)
| Path | Content | Verdict |
|---|---|---|
| `Week 00`…`Week 12/Week_XX.ipynb` | **Jul–Dec 2023** weekly quiz: ~131 questions as embedded screenshots **with "Accepted Answers" visible** (Weeks 0–2 quiz only; Weeks 3–12 also mix in lecture code and 3 programming assignments each) | ⭐ extract screenshots |
| `EXAM_PATTERN.md` | Oct 2023 final: 50 Qs × 2 marks, no negative marking, section split | ⭐ |
| `README.md` | course blurb | 🧹 |
| `Week 03/05/06/08/09` data (`*.txt`, `.wav`, `.jpeg`, `federalist_*.txt` ×86, `facebook_combined.txt`, `.gexf`) | lecture data | 🧹 |
| `Week 11/chromedriver-win64/chromedriver.exe` | binary | 🧹 **remove** (binary in git) |
| `.vscode/`, `.gitattributes` | editor config | 🧹 |

### `4th repo/` (159 files, 24 MB)
| Path | Content | Verdict |
|---|---|---|
| `Previous Year Quizes/1. Joc 2021 January to April.pdf` | **Jan–Apr 2021** (`noc21_cs32`), 66 p, **text layer**, 105 answers | ⭐ canonical for 2021 H1 |
| `Previous Year Quizes/2. Joy Sep-Decem 2020.pdf` | same text as `Question Papers/JOC Sep-Dec 2020.pdf` | ♻️ |
| `Previous Year Quizes/3. Joy Jan-Aug 2020.pdf` | byte-identical to `Question Papers/JOC Jan-Aug 2020.pdf` | ♻️ |
| `Previous Year Quizes/Joy 2018.pdf` | byte-identical to `Question Papers/JOC 2018.pdf` | ♻️ |
| `Week-3`…`Week-12/*.py` + images, `federalist_*.txt` ×86, `mymap.html`, `route.csv` | 2020-era lecture code + data | 🧹 |
| `.DS_Store` ×7 | macOS junk | 🧹 |

### `5th repo/` (13 md, 178 KB)
`week-01.md`…`week-12.md`: answer-site dumps, several terms stacked per file, heavy SEO/"join Telegram" filler.

| File | Terms covered |
|---|---|
| week-01, 02 | Jan–Apr 2026, Jul–Dec 2025, Jan–Apr 2025 |
| week-03 | Jul–Dec 2025, Jan–Apr 2025 |
| week-04 | Jan–Apr 2025, Jul–Dec 2024, Jan–Apr 2024 |
| week-05, 08, 11 | Jan–Apr 2025 |
| week-07 | Jan–Apr 2025, Jul–Dec 2024 |
| week-09 | Jan–Apr 2025, Jul–Dec 2024, Jan–Apr 2024, Jul–Dec 2023 |
| week-06 | untagged Qs |
| week-10, week-12 | **empty** (header only) |

Verdict: ⭐ only source for 2025-H2 / 2026 — but strip the spam and split by term; answers are unverified.

---

## 3. Coverage matrix (unique Q&A after de-duplication, incl. Scribd harvest)

`scribd/` = `_incoming/scribd/` (see §6).
`youtube/` = `_incoming/youtube/` (verbatim transcriptions of solved-assignment videos; `[x]` = uploader's pick, unverified unless the file says otherwise; dated candidates in `youtube/_candidates_dated.tsv`).

| Session | Weekly quiz | Prog. assignments | Exam | Best source |
|---|---|---|---|---|
| Jul-2018 | ✅ PDF; ✅ **youtube Wk1, Wk2** (unverified ticks; Wk2 Q1 missing from the video) | – | – | `Question Papers/JOC 2018.pdf`, `youtube/JOC Jul-2018 Wk*` |
| Jan-2019 | ✅ **youtube Wk3–12** (Wk1–2 not found) | Wk3 (3, 100/100), Wk6 (code for PA-1/PA-2; PA-2 is squares, not cubes), Wk8 (3, 100/100) | – | `youtube/JOC Jan-2019 Wk*`, `youtube/_candidates_dated.tsv` |
| Jul-2019 | Wk0 (likely, scribd); ✅ **youtube Wk1–12**, now **officially verified** (`noc19_cs41` review page: accepted answers, instructor solutions and private test cases in every file) | ✅ Wk2–9, 12 (statements, code, test cases) | – | `scribd/JOC Jul-2019 (likely) Wk0 answers.pdf`, `youtube/JOC Jul-2019 Wk*` |
| Jan-2020 | ✅ PDF | statements Wk2–7 (likely) | – | `Question Papers/JOC Jan-Aug 2020.pdf`, `scribd/JOC Jan-2020 (likely) Wk2-7 PA statements.pdf` |
| Sep-2020 | ✅ PDF + typed answer sheets with explanations | – | – | `Question Papers/JOC Sep-Dec 2020.pdf`, `scribd/…decoded text of NptelQuizzes.txt` |
| Jan-2021 | ✅ PDF (text) + md | ✅ `.py` | online test `.py` | `4th repo/…/1. Joc 2021…pdf`, `second repo/Week*` |
| Jul-2021 | ✅ md | ✅ `.py` | online test (morning/evening) | `second repo/Aug - Dec 2021 JOC Course` |
| Jan-2022 | ✅ md (+ Wk1 printout) | ✅ `.py` | – | `second repo/Jan - Apr 2022 JOC Course` |
| 2022 H2 (?) | ✅ scanned PDF | – | – | `Question Papers/JOC_2022_APRIL_DEC.pdf` |
| Jul-2022 | ✅ **youtube Wk0–12** (Wk0 & Wk2 verified by score pages) | – | – | `youtube/JOC Jul-2022 Wk*` |
| Jan-2023 | ✅ **youtube Wk0–12** (Wk0 verified 10/10) | – | – | `youtube/JOC Jan-2023 Wk*` |
| Jul-2023 | ✅ notebook screenshots + md + Wk1–6 printout; ✅ **youtube Wk7–12** (unscored author ticks) | partial | pattern only | `third repo`, `Assignments/`, `scribd/JOC Jul-2023 Wk1-6 quiz+PA.pdf`, `youtube/JOC Jul-2023 Wk*` |
| Jan-2024 | ✅ **youtube Wk0–12** (Wk0 verified 10/10); also Wk3, Wk11 scribd (+ W4, W9 in 5th repo) | – | – | `youtube/JOC Jan-2024 Wk*`, `scribd/JOC Jan-2024 …`, `5th repo` |
| Jul-2024 | ✅ PDF: portal review printout, Wk0–12, "Accepted Answers" present for every week (re-checked; the old "Wk1, Wk4 unanswered" note was wrong) | – | – | `JOY-OF-COMPUTING-USING-PYTHON.pdf` |
| Jan-2025 | ✅ PDF ×2 + Wk2–6 printouts (2–3 copies each) | statements Wk2–6 | – | `Python-NPTEL.pdf`, `…JAN-2025.pdf`, `scribd/JOC Jan-2025 …` |
| Jul-2025 | ✅ Wk1–12 (Wk5 from **youtube**, 30 Qs) (answers + explanations); Wk4/6/7/11 printouts | statements Wk6/7/11 | – | `scribd/JOC Jul-2025 Wk1-12 (no Wk5) answers+explanations.pdf` |
| Jan-2026 | ✅ **youtube Wk1–12** (15 Qs/week incl. case-study text); also Wk2, 5 (answered); Wk7, 10–12 (Wk7 not submitted, no answers; Wk10–12 show the uploader's own picks, unverified) | Wk2 solutions (unconfirmed), statements Wk5/10–12 | – | `scribd/JOC Jan-2026 …`, `5th repo` |
| Jul-2026 | — excluded by request — | | | |
| undated | IMP Qs (48), final-exam 34 Qs, 25-Q practice bank, 20 exam topics | | | root PDFs, `scribd/JOC practice …` |

**Gaps:** Jan-2019 Wk1–2, Jan-2019 PAs for Wk4, 5, 7, 9–12, Jul-2020, verified answers for most YouTube weeks, any official final-exam papers.

"own submission, unverified" = printout made before the due date. It shows the uploader's selected options, not NPTEL's "Accepted Answers".

---

## 4. Proposed independent layout

```
README.md                  # what this is, coverage table, how to use, credits
EXAM_PATTERN.md            # merged from second repo + third repo
CONTRIBUTING.md            # how to add a term (template below)
quizzes/
  2018/            JOC-2018.pdf
  2020-jan-apr/    quiz.pdf
  2020-sep-dec/    quiz.pdf
  2021-jan-apr/    quiz.pdf, week-00.md … week-12.md
  2021-jul-dec/    week-00.md … week-12.md
  2022-jan-apr/    week-00.md … week-12.md
  2022-jul-dec/    quiz-scanned.pdf
  2023-jul-dec/    week-00.md … week-12.md, img/
  2024-jul-dec/    quiz.pdf
  2025-jan-apr/    quiz.pdf, assignments-typed.pdf
  2025-jul-dec/    week-01.md …
  2026-jan-apr/    week-01.md …
programming-assignments/
  2021-jan-apr/ 2021-jul-dec/ 2022-jan-apr/   week-NN-pa-N.py (+ problem statement as header comment)
exams/
  online-programming-test-2021/
  final-exam-recollection-34q.pdf
practice/
  imp-questions-part-1..3.pdf
  (NptelQuizzes.pdf after OCR)
sources.md                 # every upstream repo/URL, author, licence
```

One markdown format for every week so it is diffable and searchable:

```markdown
### Q3. What will be the output of the following code?
![](img/2023-w07-q3.png)
- [ ] a, b, c
- [x] c, d, e
> Source: swayam noc23_csXX W7 · verified ✓
```

---

## 5. What makes it "unique / independent" (action list)

1. **Detach from the fork network.** It is a fork of `gxuxhxm/...` (remote `upstream`). Either ask GitHub Support to detach, or create a fresh repo and push the cleaned tree (optionally squash history so 126 MB of deleted blobs don't ride along).
2. **Delete everything that isn't Q&A** (§2 🧹): lecture code, data corpora, images, `chromedriver.exe`, `.DS_Store`, `.vscode`. Optionally keep `NOTES/` as `notes/`.
3. **De-duplicate PDFs** to one canonical copy per term (§3); drop the scanned 2021 copy in favour of the text one.
4. **Reorganise by term** (§4) — the main thing no source repo offers: one repo spanning 2018 → 2026, organised by run.
5. **Make PDFs searchable:** OCR `NptelQuizzes.pdf`, `JOC_2022_APRIL_DEC.pdf`, `34 questions…pdf`, `JOC Jan-Apr 2021.pdf` (e.g. `ocrmypdf`), and ideally convert PDF quizzes to the markdown format above.
6. **Fix broken content:** recover the 64 missing `Pasted image` embeds in `Assignments/` from `third repo` screenshots; mirror the ~465 hot-linked swayam images into the repo.
7. **Strip spam/branding** from `5th repo` text and watermark notes; keep only Q, options, answer.
8. **Add value no one else has:**
   - a **topic index** (e.g. all "turtle output" / "magic square" / "dictionary" questions across years) — the course reuses questions heavily;
   - a **"repeat frequency"** tag showing which questions recur across terms;
   - a verified/unverified flag per answer (5th-repo and ChatGPT-converted answers are unverified).
9. **Licence & credits:** both code sources are MIT (Goutham S K 2023, Kishan Kumar Rai 2021) — keep their copyright lines in `sources.md`/LICENSE. Quiz PDFs/screenshots are NPTEL course material and third-party compilations (getpythoncode, Coding Buddies, Scribd uploaders); credit them and don't relicense their content as your own.

---

## 6. Scribd harvest (2026-10-09)

- **Search:** Scribd's JSON search endpoint, 20 keyword variants × 4 pages → 547 docs, 231 matched the keywords. I skipped certificates, hall tickets and payment lists (they contain other people's personal data), course lists and ebooks.
- **Downloaded:** 46 docs via `scribd-downloader.py` (headless embed→PDF), plus the 1 test doc, all into `_incoming/scribd/`, then renamed `JOC <Session> Wk<range> <kind>.pdf`. Mapping and source URL for each file: `_incoming/_sources.tsv`.
- `_incoming/scribd/_duplicates/` (9): re-download of NptelQuizzes, a printout of the kishanrajput23 repo, a 2018 page already in `JOC 2018.pdf`, and 2020 pages already in `JOC Jan-Aug 2020.pdf` (3 of these have scrambled text).
- `_incoming/scribd/_junk/` (1): answer-site spam.
- **Image-only** (no text layer, need OCR; Tesseract isn't installed): Jan-2026 Wk2 & Wk7, Jan-2024 Wk3, Jan-2022 Wk1, Jul-2025 Wk4.
- **Scribd URLs of existing root PDFs:** NptelQuizzes → `521374064`, Joy-Jan-Aug-2020 → `586667343`, JOY-OF-COMPUTING-USING-PYTHON → `789154999`, Python-NPTEL → `858004300`, JAN-2025 → `857620689`, PART-1/2/3 → `722017600` / `722017595` / `722017598` (all `https://www.scribd.com/document/<id>/`). The scanned `JOC Jan-Apr 2021.pdf` and `JOC_2022_APRIL_DEC.pdf` did not turn up on Scribd.
- **Same scrambling elsewhere:** Scribd docs `445754236`, `488197995`, `493926873` use different substitution keys. All three are Jan-2020 duplicates, so I didn't decode them.

---

## 7. `JRG JOC/` (2026-10-11)

New subfolder holding the cleaned, term-organised copy. Originals were left untouched; see `JRG JOC/README.md`, `JRG JOC/_manifest.tsv` and `JRG JOC/inventory.tsv`. Jul-2026 is taken only from `2026 Assignments/`.

Done from §5: step 4 (portal printouts of 2018, Jan-2020, Sep-2020, Jan-2021, Jul-2024, Jan-2025 parsed into `week-NN.md` with page crops; Jul-2026 PDFs converted; image-only/scanned PDFs OCR'd to `*.ocr.txt` with RapidOCR, because Tesseract is not installed) and step 6 (all 273 hot-linked swayam images mirrored into `quizzes/<term>/img/`). Step 8 brief for the topic index / repeat frequency / verified flag is `JRG JOC/STEP3_INSTRUCTIONS.md`. Still open: parse the remaining OCR text, licence decision, fork detach.
