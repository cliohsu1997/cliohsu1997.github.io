# -*- coding: utf-8 -*-
"""
Fill Yamanashi Gakuin iCLA CV from the blank template.
Rules (from the form wording):
- Name blanks: plain text, no parentheses
- Education: each Entered/Graduated row gets a date + status choice;
  University / Graduate School / Major goes on the detail row
  (and Enter rows also show the degree stage + school so the row is not empty)
- Work: Research Assistant only; Current org = present affiliation (HKUST PhD)
- Research area: ONE line (cell is short)
- Educational Activities:
  1) awards/evaluations only
  2) list of teaching SUBJECTS (one subject per line; not admin roles)
  7) other (TA Coordinator)
"""
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = r"C:\Users\birdy\Desktop\cliohsu1997.github.io\application\faculty\Japan\Yamanashi Gakuin University\CV-and-Achievement-in-Education-and-Research-for-2027.docx"
OUT = r"C:\Users\birdy\Desktop\cliohsu1997.github.io\application\faculty\Japan\Yamanashi Gakuin University\CV_HSU_Ke_Cheng_Yamanashi_Gakuin_iCLA_2027.docx"


def tcs(table, ri):
    return table._tbl.tr_lst[ri].tc_lst


def paragraphs(tc):
    return list(tc.iterchildren(qn("w:p")))


def runs(p):
    return list(p.iterchildren(qn("w:r")))


def set_para(p, text):
    rs = runs(p)
    if not rs:
        r = OxmlElement("w:r")
        t = OxmlElement("w:t")
        t.text = text
        if text[:1].isspace() or text[-1:].isspace():
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r.append(t)
        p.append(r)
        return
    # write into first run, clear rest
    for t in rs[0].findall(qn("w:t")):
        t.text = ""
    ts = rs[0].findall(qn("w:t"))
    if ts:
        ts[0].text = text
        if text[:1].isspace() or text[-1:].isspace() or "\u3000" in text:
            ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    else:
        t = OxmlElement("w:t")
        t.text = text
        rs[0].append(t)
    for r in rs[1:]:
        p.remove(r)


def make_para(text, size=9):
    p = OxmlElement("w:p")
    pPr = OxmlElement("w:pPr")
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "20")
    sp.set(qn("w:after"), "20")
    sp.set(qn("w:line"), "240")
    sp.set(qn("w:lineRule"), "auto")
    pPr.append(sp)
    ind = OxmlElement("w:ind")
    ind.set(qn("w:left"), "40")
    ind.set(qn("w:right"), "40")
    pPr.append(ind)
    p.append(pPr)
    r = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    rPr.append(sz)
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), "Times New Roman")
    fonts.set(qn("w:hAnsi"), "Times New Roman")
    fonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    rPr.append(fonts)
    r.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    if text[:1].isspace() or text[-1:].isspace():
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    r.append(t)
    p.append(r)
    return p


def clear_write(tc, lines, size=9):
    # Remove paragraphs AND nested tables (form hides MM/YY placeholders in nested tbl)
    for child in list(tc):
        if child.tag != qn("w:tcPr"):
            tc.remove(child)
    if not lines:
        tc.append(make_para("", size))
        return
    for line in lines:
        tc.append(make_para(line, size))


def write_value_over_placeholder(tc, value):
    """Replace '(   )' placeholder with plain value (no brackets)."""
    done = False
    for p in paragraphs(tc):
        full = "".join((t.text or "") for r in runs(p) for t in r.findall(qn("w:t")))
        if "(" in full and ")" in full:
            set_para(p, value)
            done = True
    if not done:
        clear_write(tc, [value], 11)


def set_first_para(tc, text):
    # Always rebuild cell so nested placeholder tables cannot remain
    clear_write(tc, [text], 9)


def append_lines_after_label(tc, label_key, lines, size=9):
    ps = paragraphs(tc)
    ref = None
    for p in ps:
        full = "".join((t.text or "") for r in runs(p) for t in r.findall(qn("w:t")))
        if label_key in full:
            ref = p
    if ref is None:
        ref = ps[-1] if ps else None
    for line in lines:
        np = make_para(line, size)
        if ref is not None:
            ref.addnext(np)
            ref = np
        else:
            tc.append(np)
            ref = np


doc = Document(SRC)

# As-of
for p in doc.paragraphs:
    if "As of" in p.text:
        for r in p.runs:
            r.text = ""
        if p.runs:
            p.runs[0].text = "(As of October 20, 2026)"
        else:
            p.add_run("(As of October 20, 2026)")

# ========== TABLE 0 Personal ==========
t0 = doc.tables[0]
r1 = tcs(t0, 1)
# Name in Chinese on label
for p in paragraphs(r1[0]):
    full = "".join((t.text or "") for r in runs(p) for t in r.findall(qn("w:t")))
    if "Name in" in full:
        set_para(p, "(Name in Chinese: 許可證)")
write_value_over_placeholder(r1[1], "HSU")
write_value_over_placeholder(r1[2], "Ke Cheng")
clear_write(r1[3], ["Male"], 10)

r4 = tcs(t0, 4)
set_first_para(r4[1], "05 12, 1997　29 years old")
clear_write(r4[3], ["Taiwan"], 10)
ps = paragraphs(r4[4])
if len(ps) >= 2:
    set_para(ps[1], "(852)")
if len(ps) >= 4:
    set_para(ps[3], "(68409753)")

clear_write(
    tcs(t0, 5)[1],
    [
        "Department of Economics, 5067 Lee Shau Kee Business Building,",
        "The Hong Kong University of Science and Technology,",
        "Clear Water Bay, Kowloon, Hong Kong",
    ],
    9,
)
clear_write(tcs(t0, 6)[1], ["khsu@connect.ust.hk"], 10)

# ========== TABLE 1 Education ==========
# Form pattern per degree:
#   Enter row: date | [degree-stage label kept OR school] | Entered
#   Detail row: date | University / School / Major | Graduated/Completed/Current student
# Fill detail rows with University / School / Major on separate lines.
# On Enter rows, keep stage label but put school name under it so the row is not "empty".
t1 = doc.tables[1]

def edu_enter(row_i, date, stage_label, status):
    r = tcs(t1, row_i)
    set_first_para(r[1], f"    {date}")
    clear_write(r[3], [stage_label], 8)
    set_first_para(r[5], status)


def edu_detail(row_i, date, lines, status):
    r = tcs(t1, row_i)
    set_first_para(r[1], f"    {date}")
    clear_write(r[3], lines, 8)
    set_first_para(r[5], status)


# Template: each degree = Entered row + University/School/Major row
edu_enter(2, "09/15", "Educational background pertaining to bachelor's degree", "Entered")
edu_detail(
    3,
    "12/19",
    ["HKUST, B.Sc. in Mathematics and Economics (Minor in Actuarial Mathematics)"],
    "Graduated",
)
edu_enter(4, "08/20", "Educational background pertaining to master's degree", "Entered")
edu_detail(5, "08/22", ["HKUST, M.Phil. in Economics"], "Completed")
edu_enter(6, "08/22", "Educational background pertaining to doctoral degree", "Entered")
edu_detail(7, "07 27 (expected)", ["HKUST, Ph.D. in Economics"], "Current student")

# Doctoral Degree box
r = tcs(t1, 8)
clear_write(r[2], ["Degree name", "Ph.D. in Economics"], 9)
clear_write(r[3], ["Conferring university", "HKUST"], 9)
clear_write(r[4], ["Date of conferment", "07 27, 2027 (expected)"], 9)

# ========== TABLE 2 Work ==========
t2 = doc.tables[2]
# Only Research Assistant
r = tcs(t2, 2)
set_first_para(r[0], "      From 01/20")
set_first_para(r[1], "To 12/20")
clear_write(r[2], ["Research Assistant for Prof. Benjamin Bernard, National Taiwan University"], 8)
clear_write(r[3], [""], 8)  # no Full time / Part time

# Clear unused job rows (leave blank — do not leave MM/YY placeholders)
for ri in range(3, 7):
    r = tcs(t2, ri)
    clear_write(r[0], [""], 8)
    clear_write(r[1], [""], 8)
    clear_write(r[2], [""], 8)
    clear_write(r[3], [""], 8)

# Current organization: leave blank (PhD belongs under Education, not Work)
r = tcs(t2, 7)
for p in paragraphs(r[0]):
    full = "".join((t.text or "") for rr in runs(p) for t in rr.findall(qn("w:t")))
    if "From" in full or "MM" in full:
        set_para(p, "      From MM/YY")
clear_write(r[1], [""], 8)
clear_write(r[2], [""], 8)
clear_write(r[3], [""], 8)  # no Full time / Part time

# ========== TABLE 3 ==========
t3 = doc.tables[3]
clear_write(
    tcs(t3, 0)[1],
    ["Industrial Organization; Digital Economics; Quantitative Marketing"],
    9,
)
# ONE line only — short cell
clear_write(
    tcs(t3, 1)[1],
    ["E-commerce return policy; consumer search; platform economics; structural estimation"],
    9,
)
lang = tcs(t3, 2)[1]
set_first_para(
    lang,
    "Native language: Mandarin Chinese　　Language(s) in which you have been given lectures in the past: English",
)

# ========== TABLE 4 Research ==========
body = tcs(doc.tables[4], 1)[0]
append_lines_after_label(
    body,
    "Master’s Thesis",
    ['"Product Design with Heterogeneous Search Costs," with Pak Hung AU, HKUST, 2022.'],
    9,
)
append_lines_after_label(
    body,
    "Doctoral Dissertation",
    [
        '"Designing Return Policy in E-Commerce: A Trade-off between Purchase and Return Efficiency" (JMP; expected 2027).',
    ],
    9,
)
append_lines_after_label(body, "List of Papers (peer-reviewed)", ["N/A"], 9)
append_lines_after_label(body, "Books", ["N/A"], 9)
append_lines_after_label(
    body,
    "Academic conference presentations",
    [
        '"Designing Return Policy in E-Commerce..." — APIOC 2026*; ESAM 2026*; China Economics Annual Conference Summer Forum 2026*; HKUST Business School PhD Conference; CEP Brownbag, HKUST.',
        '"Product Design with Heterogeneous Search Costs" — APIOC 2023; AMES 2023, NTU Singapore.',
    ],
    9,
)
append_lines_after_label(body, "Acquisition of external research funds", ["N/A"], 9)
append_lines_after_label(
    body,
    "Any other achievements",
    [
        'Working papers: "Pass-Through and Incidence with Product Returns"; "Too Much Unsold Stock?: Environmental Consequences of Price Commitment."',
    ],
    9,
)

# ========== TABLE 5 Educational Activities ==========
# Rebuild content cell from blank labels + correct answers
body = tcs(doc.tables[5], 1)[0]
for p in list(paragraphs(body)):
    body.remove(p)

edu_blocks = [
    # 1) evaluations only — do not repeat the course list here
    "Awards received for educational activities, educational evaluations (teaching awards, etc.)",
    "Lecturer, Math Camp for MSc in Economics, HKUST: 4.53/5 (2026).",
    "Teaching Assistant, Department of Economics, HKUST: average 4.72/5 (2020-2025).",
    # 2) teaching subjects — only place the course list appears
    "List of teaching subjects that you were in charge of up until now",
    "Math Camp for MSc in Economics (Lecturer, HKUST, 2026)",
    "ECON2123 Macroeconomics (Teaching Assistant, HKUST)",
    "ECON4134 Economics of Uncertainty and Information (Teaching Assistant, HKUST)",
    "ECON4999T Economics of Uncertainty and Information (Teaching Assistant, HKUST)",
    "ECON5210 Microeconomic Theory I (Teaching Assistant, HKUST)",
    "Number of students you advised on their thesis/dissertation over the last 3 years:",
    "N/A",
    "",
    "",
    "Textbooks, educational materials, reference books created",
    "N/A",
    "Presentations, lectures, etc. related to educational techniques and practices",
    "N/A",
    "Attendance of seminars, training programs, etc. related to educational techniques",
    "N/A",
    "Other items that should be specially noted with regard to educational activities",
    "Teaching Assistant Coordinator, Business School, HKUST (2025-2026).",
]
for line in edu_blocks:
    body.append(make_para(line, 9))

# ========== TABLE 6 Practical ==========
body = tcs(doc.tables[6], 1)[0]
append_lines_after_label(body, "Practical experience related to field of specialization", ["N/A"], 9)
append_lines_after_label(body, "Other items that should be specially noted about practical", ["N/A"], 9)

doc.save(OUT)
print("Saved", OUT)
