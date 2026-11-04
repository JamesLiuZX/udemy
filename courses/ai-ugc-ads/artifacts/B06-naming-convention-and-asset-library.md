# B06 · Naming Convention + Asset Library Standard

Part of *AI UGC Video Ads*. Built in lecture 7.3, on the export naming pattern from
lecture 5.4. The companion file is `B06-asset-library-record.csv`, an empty record
with one row per ad set. It opens in any spreadsheet. Use them to be able to find
what worked in month six, and to know what happened to it.

Every ad you make is easy to find the week you made it. A filename that made sense
in the moment tells you nothing once you are looking at your two-hundredth export.

---

## 1. How to use this

1. **Adopt the filename convention (section 2) before the first export,** not after
   the folder is already a mess.
2. **Keep a linked record, one row per ad set** (section 3 and the CSV), starting the
   day you build the test, not the day you read the results.
3. **Fill the record at three moments:** when the ad is cleared (B05), when the test
   starts, and when the decision is made. Do not leave "what happened" to memory.
4. **Never put results in the filename.** Names say what the file is. The record says
   what happened to it.
5. **Write the decision back every time.** Every winner, loser or noise call from the
   results review (Section 8) goes into this record. The "iterate or new angle"
   question in Section 8.4 cannot be answered about a variant if nobody remembers
   testing its predecessor.

Skipping this costs nothing today. It costs you that question later.

| | |
| --- | --- |
| Product | |
| Library owner (a name) | |
| Where the library lives (folder path or tool) | |
| Where the record lives | |
| Date set up | |

## 2. Job one: finding the file (the filename)

The convention, from lecture 5.4:

```text
<brand>_<angle>_<version>_<placement>.<extension>
```

Examples of the shape, using the course's running example:

```text
harlan_houreleven_v1_9x16.mp4
harlan_houreleven_v1_4x5.mp4
harlan_houreleven_v1_tiktok.mp4
harlan_houreleven_v1_instream.mp4
```

| Part | Rule | Your rule |
| --- | --- | --- |
| brand | One short lowercase slug for the product or brand | |
| angle | One lowercase slug, no spaces, hyphens or capitals, matching a row of your angle map (B01) | |
| version | `v` plus a number. A new version is any change that could change the result (hook, proof, cut, caption). Never "final" or "new" | |
| placement | The format or destination from your cross-platform matrix (for example 9x16, 4x5, tiktok, instream). Confirm each platform's current specs before every campaign | |
| extension | The file type | |

**Angle slugs.** One list, one place, so the same angle is never spelled two ways.

| Angle (B01 row) | Slug | Notes |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |
| | | |

**A checker you can run.** This pattern accepts lowercase letters and digits in the
brand and angle, a numeric version and a listed placement. Edit the placement list
to match your own matrix. It is a regular expression, usable in a spreadsheet, a
script or a folder-rename tool:

```text
^[a-z0-9]+_[a-z0-9]+_v[0-9]+_(9x16|4x5|1x1|16x9|tiktok|instream)\.(mp4|png|jpg|mov)$
```

It accepts `harlan_houreleven_v1_9x16.mp4`. It rejects a name with capitals, a hyphen
in the angle, `final` in place of a version number, or no placement.

## 3. Job two: knowing what happened (the linked record)

Results, dates and decisions do not belong in a filename. They live in a record
linked to the file, one row per ad set.

| Field | What goes in it |
| --- | --- |
| ad_set_id | A unique id for the test cell |
| filename | The exact filename from section 2 |
| angle, version, placement | Parsed from the filename, for filtering |
| predecessor_filename | The version this one iterates on, if any, so the lineage is not lost |
| angle_map_row_b01 | The row of your angle map it came from |
| hook_pattern_b02 | The hook pattern it uses |
| source_asset_b03_b04 | The batch or video brief it was built from |
| preflight_cleared_by_and_date_b05 | Who cleared it and when |
| campaign | Where it ran |
| tested_start_date, tested_end_date | When |
| budget_and_kill_rule_ref_b07 | The budget and the kill rule decided before the test, and where they are written |
| spend | What it actually cost |
| result | winner, loser or noise |
| decision | scaled, killed or retested |
| decision_date | When the call was made |
| why_in_one_line | The reason, in a sentence |
| notes | Anything else |

The essentials are the four fields lecture 7.3 names: the angle, when it was tested,
the result, and the decision. The other columns make the library searchable and let
you trace a winner back to its brief, its hook pattern and its clearance.

Rules for the record:

| Rule | Why |
| --- | --- |
| One row per ad set, never one per file | The result belongs to the test cell |
| Result is one of winner, loser or noise, and the decision is one of scaled, killed or retested | Free text cannot be filtered or counted |
| The decision is written the day it is made | Memory is not a record |
| A retest links to its predecessor | Otherwise a second look reads as a first |
| Nothing is deleted. A killed ad stays in the library with its record | You learn from the losers too |

## 4. The library

| Item | Your answer |
| --- | --- |
| Folder structure (for example by angle, then version, then placement) | |
| Master files and exports kept where | |
| Who may add, rename or retire a file (a name) | |
| What gets archived, when, and where | |
| How you search it six months from now (the question you expect to ask) | |

## 5. Link to the rest of the system

| Where | What this record feeds |
| --- | --- |
| B01 angle map | Each angle's row gets a column for tested versions and results |
| B02 hook matrix | Its test log can be filled from this record |
| B05 pre-flight | The record holds who cleared each ad and when |
| Section 7 testing and kill criteria (B07) | The budget and kill rule are referenced per ad set |
| Section 8 results and iterate-or-new-angle | Every decision is written back here |
| Section 9 swipe file | Built from a library that is actually searchable |

## 6. Honest test

- Could you find the version of a specific angle you ran six months ago, in under a
  minute?
- Does any filename carry a result, a date or the word "final"?
- Does every tested ad set have a result and a decision, or only the memorable ones?
- Is the decision recorded on the day it was made?
- If a winner starts to tire, can you trace it back to its brief and its hook?

## 7. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |
