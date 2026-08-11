% kdp-book.cls
% A memoir-based document class for KDP paperback interiors.
%
% Trim size and margins are NOT set here. build.py computes them per book
% (trim size + KDP's page-count-scaled gutter table) and writes a config.tex
% that \input's before this class loads, defining:
%   \BookTrimWidth \BookTrimHeight \BookGutter \BookOuter \BookTop \BookBottom
% Sane 6x9 defaults apply if a macro is missing, so the class still loads
% standalone (e.g. for a quick test compile) without a config.tex.
%
% Fonts are loaded by relative path from the repo root. Always invoke
% xelatex/latexmk with cwd = repo root (build.py does this); the paths
% below assume it.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{kdp-book}[2026/01/01 KDP paperback interior class]

\newif\if@kdpdraft
\DeclareOption{draft}{\@kdpdrafttrue}
% zh: Simplified Chinese interior. Loads xeCJK and Noto Serif/Sans CJK SC,
% and swaps the class's hard-coded English box labels, TOC name, chapter
% numeral style, and copyright-line wording for Chinese ones. Everything
% else (trim/margin geometry, box colours, widow/orphan control, running
% head mechanics) is language-agnostic and applies unchanged to both
% variants. Never disturbs the English path: a book that doesn't pass
% this option gets exactly the class's original behaviour.
\newif\if@kdpzh
\DeclareOption{zh}{\@kdpzhtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{memoir}}
\ProcessOptions\relax

\LoadClass[twoside,openright,10.5pt]{memoir}
% twoside: a KDP paperback is printed on both sides of the sheet and bound,
% so recto and verso pages need mirrored margins, the gutter has to land on
% the binding side on *every* page, not just odd ones. openright forces
% chapter openers onto a recto page (memoir inserts a blank verso if needed).

\RequirePackage{fontspec}
\RequirePackage{microtype}
\RequirePackage{xcolor}
\RequirePackage[english]{babel}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{longtable}
\RequirePackage{booktabs}
\RequirePackage{array}
\RequirePackage{calc}

% Pandoc emits longtable rows separated only by a bare `\\`, which gives
% zero gap between rows. Fine for short one-line cells; as soon as any
% cell wraps to two or more lines, the next row's text sits flush against
% it with no visual break, table row spacing is set uniformly here.
\setlength{\extrarowheight}{7pt}

% Pandoc's fragment output (no --standalone) assumes a handful of macros
% its own default template would otherwise define. Provide them here so
% chapter .tex fragments compile without pulling in pandoc's preamble.
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}

% --- Trim size and margins ---------------------------------------------
\providecommand{\BookTrimWidth}{6in}
\providecommand{\BookTrimHeight}{9in}
\providecommand{\BookGutter}{0.625in}
\providecommand{\BookOuter}{0.75in}
\providecommand{\BookTop}{0.75in}
\providecommand{\BookBottom}{0.75in}

% KDP needs the PDF page itself to BE the trim size, not a trimmed region
% floating inside a larger default stock (memoir defaults stock to Letter
% if it's never set, which is what silently produced an 8.5x11 PDF with the
% 6x9 content marooned off-centre in it). Stock = trim here: no separate
% offset-print stock sheet, no crop marks.
\setstocksize{\BookTrimHeight}{\BookTrimWidth}
\settrimmedsize{\BookTrimHeight}{\BookTrimWidth}{*}
\settrims{0pt}{0pt}
% setlrmarginsandblock takes (spine, edge, ratio): spine is the binding-side
% margin (BookGutter) and mirrors automatically between recto/verso under
% twoside; edge is the outer margin (BookOuter). Passing these in the wrong
% order puts the gutter on the outside edge, wrong on every page.
\setlrmarginsandblock{\BookGutter}{\BookOuter}{*}
\setulmarginsandblock{\BookTop}{\BookBottom}{*}
\checkandfixthelayout

% --- Typography -----------------------------------------------------------
% Single-spaced LaTeX defaults read tight for a printed trade book; this is
% the single biggest lever for a page feeling "squished" versus "edited".
% Placed before \setmainfont so the font's \selectfont picks it up.
\linespread{1.14}

% TeX Gyre Schola: same family as the video course (theme/vendor/fonts),
% a Century Schoolbook cut drawn for long-form reading.
\setmainfont{texgyreschola}[
  Path = theme/vendor/fonts/,
  Extension = .otf,
  UprightFont = *-regular,
  ItalicFont = *-italic,
  BoldFont = *-bold,
  BoldItalicFont = *-bolditalic,
]

\setmonofont{IBMPlexMono}[
  Path = theme/vendor/fonts/,
  Extension = .ttf,
  UprightFont = *-Regular,
  BoldFont = *-SemiBold,
  Scale = 0.92,
]

% --- CJK (Simplified Chinese editions only) --------------------------------
% Two system packages, neither vendored, needed before building a
% \documentclass[zh]{kdp-book} title:
%   apt-get install -y fonts-noto-cjk texlive-lang-chinese
% fonts-noto-cjk ships four .ttc files (~92MB total) bundling five CJK
% language subsets each, far larger than this repo's usual small per-face
% vendored files; fontconfig exposes "Noto Serif CJK SC" / "Noto Sans CJK
% SC" as addressable family names once installed, Regular and Bold both,
% so fontspec's ordinary system-font lookup (no explicit Path/Extension,
% same as looking up any installed OS font) resolves weights
% automatically. texlive-lang-chinese provides xeCJK.sty itself, which
% TeX Live's base install does not include. See
% books/one-person-business/notes.md for the full context.
%
% xeCJK auto-detects CJK codepoints anywhere in the document, including
% inside \bfseries/\itshape/coloured text, and renders them with the CJK
% family below instead of the Latin \setmainfont, entirely automatically;
% \setmainfont above still handles every Latin letter, digit, and piece of
% English (product names, pasted prompts) that appears inside CJK prose.
% CJK has no italic tradition, so xeCJK silently renders \itshape CJK text
% upright rather than faking a slant, which is the typographically correct
% behaviour, not a bug, for the \pullquote box below.
\if@kdpzh
  \RequirePackage{xeCJK}
  \setCJKmainfont{Noto Serif CJK SC}
  \setCJKsansfont{Noto Sans CJK SC}
  \setCJKmonofont{Noto Sans Mono CJK SC}
  \xeCJKsetup{CJKspace=true}
\fi

\widowpenalty=10000
\clubpenalty=10000
\brokenpenalty=10000
\frenchspacing

% memoir defaults twoside documents to \flushbottom, stretching interline
% and interparagraph glue so every page's last line lands on the same
% baseline. That's fine for uniform running prose; it looks broken the
% moment a page mixes plain paragraphs with a pull quote, a callout box,
% or a table, none of which stretch, so all the slack piles into whatever
% paragraph glue is left, as one or two huge gaps rather than a page's
% worth of small, invisible ones. Ragged bottom is the standard trade
% nonfiction answer once a book has any non-uniform content on the page.
\raggedbottom

% --- Brand accent (chapter furniture only; interior stays print-safe B&W
%     unless a book explicitly buys KDP's colour-interior product) --------
% Same semantic palette as the video course's theme/deck.css (--accent,
% --good), so the two product lines read as one design system.
\definecolor{bookaccent}{HTML}{1B4F8F}
\definecolor{bookaccenttint}{HTML}{EAF1F8}
\definecolor{bookflag}{HTML}{C1741A}
\definecolor{bookflagtint}{HTML}{F7EEDD}
\definecolor{bookgood}{HTML}{1C6B4C}
\definecolor{bookgoodtint}{HTML}{E7F2EC}

% Both callout boxes below share this interior padding. LaTeX's fboxsep
% default (3pt) reads as cramped once a box holds a bold label plus a full
% paragraph rather than a single short word; this is the fix for both at
% once rather than a per-box patch.
\setlength{\fboxsep}{11pt}

% Visible marker for unresolved [AUTHOR-INPUT: ...] text, so a draft PDF
% shows the gap on the page, not only in qc.py's terminal output. build.py
% rewrites the bracket syntax into this macro after Pandoc conversion.
\newcommand{\authorinputlabel}{AUTHOR INPUT NEEDED}
\if@kdpzh\renewcommand{\authorinputlabel}{作者内容待补}\fi
\newcommand{\authorinput}[1]{%
  \par\bigskip\noindent
  \fcolorbox{bookflag}{bookflagtint}{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \small\bfseries\color{bookflag}\authorinputlabel\par\medskip
      \normalfont\normalsize\color{black}#1%
    }%
  }%
  \par\bigskip
}

% A single line worth blowing up big on the page, breaking a long run of
% body paragraphs the way a magazine layout would. build.py converts
% [PULLQUOTE: ...] into this after Pandoc runs. Ragged both sides so it
% reads as set apart from justified body text, not as a wide paragraph.
% The explicit vspace is larger than a bare \bigskip: a pull quote sitting
% only a bigskip from body text still reads as a crowded paragraph, not
% as a deliberate break in the page.
\newcommand{\pullquote}[1]{%
  \par\vspace{1.4\baselineskip}\noindent
  {\centering\normalfont\Large\itshape\color{bookaccent}#1\par}
  \vspace{1.4\baselineskip}\noindent
}

% Chapter-close summary box, the visual and structural bookend to
% \authorinput: ink blue instead of flag ochre, a takeaway instead of a
% gap. build.py wraps a [TAKEAWAYS]...[/TAKEAWAYS] block's
% already-Pandoc-converted list in this after Pandoc runs.
\newcommand{\keytakeawayslabel}{KEY TAKEAWAYS}
\if@kdpzh\renewcommand{\keytakeawayslabel}{要点总结}\fi
\newcommand{\keytakeaways}[1]{%
  \par\bigskip\noindent
  \fcolorbox{bookaccent}{bookaccenttint}{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \small\bfseries\color{bookaccent}\keytakeawayslabel\par\medskip
      \normalfont\normalsize\color{black}#1%
    }%
  }%
  \par\bigskip
}

% A researched, sourced statistic or case study, standing in for a
% personal anecdote when the real author doesn't have one to give.
% Green (bookgood), the same "verified" semantic the video course uses
% for a confirmed claim, distinct from the ochre flag (a gap) and the
% blue takeaway (a summary). Two arguments: the claim, then its source
% in a smaller, quieter line, exactly the way a pull quote's attribution
% sits under the quote itself rather than competing with it. build.py
% converts [KEY-INSIGHT: claim || source] into this after Pandoc runs.
% Every claim inside one of these must be real and checked, never
% invented to sound plausible; see books/docs/02-research-and-sourcing.md.
\newcommand{\keyinsightlabel}{KEY INSIGHT}
\if@kdpzh\renewcommand{\keyinsightlabel}{关键洞察}\fi
\newcommand{\keyinsight}[2]{%
  \par\bigskip\noindent
  \fcolorbox{bookgood}{bookgoodtint}{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \small\bfseries\color{bookgood}\keyinsightlabel\par\medskip
      \normalfont\normalsize\color{black}#1\par\smallskip
      \normalfont\small\itshape\color{black!60}#2%
    }%
  }%
  \par\bigskip
}

% --- Chapter style ----------------------------------------------------------
\makechapterstyle{kdpbook}{
  \renewcommand{\chapternamenum}{\space}
  \renewcommand{\printchaptername}{%
    \raggedright\normalfont\addfontfeature{Letters=SmallCaps}%
    \fontsize{12pt}{14pt}\selectfont\color{bookaccent}\chaptername
  }
  \renewcommand{\printchapternum}{}
  \renewcommand{\printchapternonum}{}
  \renewcommand{\afterchapternum}{}
  \setlength{\beforechapskip}{4\baselineskip}
  \setlength{\midchapskip}{0.6\baselineskip}
  \setlength{\afterchapskip}{2.5\baselineskip}
  \renewcommand{\chapnumfont}{\normalfont\fontsize{40pt}{40pt}\selectfont\color{bookaccent}}
  \renewcommand{\chaptitlefont}{\normalfont\huge\bfseries\raggedright}
  \renewcommand{\printchapternum}{%
    \chapnumfont\thechapter\par
  }
}
\chapterstyle{kdpbook}
% Chinese nonfiction convention folds the chapter word and number into one
% compound label ("第3章") rather than the English pattern of a small
% word ("CHAPTER") sitting above an unrelated giant numeral; printing both
% here would just repeat the same number twice on the page. SmallCaps is a
% Latin OpenType feature with no meaning for CJK glyphs, so it's dropped
% rather than silently no-op'd on the character range it can't affect.
\if@kdpzh
  \renewcommand{\printchaptername}{}
  \renewcommand{\printchapternum}{%
    \raggedright\normalfont
    \fontsize{30pt}{34pt}\selectfont\color{bookaccent}%
    第\thechapter{}章\par
  }
\fi
\setsecheadstyle{\normalfont\Large\bfseries\raggedright\color{bookaccent}}
\setsubsecheadstyle{\normalfont\large\bfseries\raggedright}
% Memoir's default section spacing is tuned for black-on-black headings
% that don't need to visually separate themselves; the coloured heading
% above draws the eye more and reads as cramped against the preceding
% paragraph at the old spacing. More air above than below, so a heading
% stays visually attached to the text it introduces.
\setlength{\beforesecskip}{2.6\baselineskip}
\setlength{\aftersecskip}{1.1\baselineskip}
\setlength{\beforesubsecskip}{2\baselineskip}
\setlength{\aftersubsecskip}{0.8\baselineskip}

% A thin accent rule under the chapter title (number + name as one unit),
% the same furniture the video course's slide headers use, so a chapter
% opener reads as designed rather than as a Word document's Heading 1.
% afterchaptertitle is memoir's hook for "after the title, before body";
% afterchapternum fires earlier, between the numeral and the title itself.
\renewcommand{\afterchaptertitle}{%
  \par\vspace{0.5\baselineskip}
  {\color{bookaccent}\rule{0.15\linewidth}{1.2pt}}\par
  \vskip\afterchapskip
}

% --- Running heads ----------------------------------------------------------
\makepagestyle{kdpheadings}
\makeevenhead{kdpheadings}{\small\itshape\thepage}{}{\small\normalfont\booktitleshort}
\makeoddhead{kdpheadings}{\small\normalfont\leftmark}{}{\small\itshape\thepage}
\makeevenfoot{kdpheadings}{}{}{}
\makeoddfoot{kdpheadings}{}{}{}
\providecommand{\booktitleshort}{}
\pagestyle{kdpheadings}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}

% --- Front matter helpers ---------------------------------------------------
\newcommand{\halftitlepage}[1]{%
  \thispagestyle{empty}
  \begin{center}
    \vspace*{0.30\textheight}
    {\normalfont\Large #1\par}
  \end{center}
  \clearpage
}

\newcommand{\booktitlepage}[3]{% title, subtitle, author
  \thispagestyle{empty}
  \begin{center}
    \vspace*{0.22\textheight}
    {\normalfont\huge\bfseries #1\par}
    \vspace{1.2\baselineskip}
    {\normalfont\Large #2\par}
    \vspace{4\baselineskip}
    {\normalfont\large #3\par}
  \end{center}
  \clearpage
}

% args: author, year, edition-note, ai-disclosure-line, isbn-or-placeholder
\newcommand{\copyrightpage}[5]{%
  \thispagestyle{empty}
  \vspace*{\fill}
  {\small\normalfont
    \if@kdpzh 版权所有\ \copyright\ #2\ #1\else Copyright \copyright\ #2\ #1\fi\par
    \vspace{0.6\baselineskip}
    #3\par
    \vspace{0.6\baselineskip}
    #4\par
    \vspace{0.6\baselineskip}
    #5\par
  }
  \clearpage
}

% memoir/book's default TOC heading is babel[english]'s "Contents"; the
% zh variant wants the Chinese equivalent instead. \tableofcontents itself
% is invoked later, from front_matter_tex() in build.py, so overriding the
% name here (any point before that call) is enough.
\if@kdpzh\renewcommand{\contentsname}{目录}\fi

\newcommand{\dedicationpage}[1]{%
  \thispagestyle{empty}
  \begin{center}
    \vspace*{0.35\textheight}
    {\normalfont\itshape #1\par}
  \end{center}
  \clearpage
}

\endinput
