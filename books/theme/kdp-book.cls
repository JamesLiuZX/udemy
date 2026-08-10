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

\widowpenalty=10000
\clubpenalty=10000
\brokenpenalty=10000
\frenchspacing

% --- Brand accent (chapter furniture only; interior stays print-safe B&W
%     unless a book explicitly buys KDP's colour-interior product) --------
\definecolor{bookaccent}{HTML}{1B4F8F}
\definecolor{bookflag}{HTML}{C1741A}
\definecolor{bookflagtint}{HTML}{F7EEDD}

% Visible marker for unresolved [AUTHOR-INPUT: ...] text, so a draft PDF
% shows the gap on the page, not only in qc.py's terminal output. build.py
% rewrites the bracket syntax into this macro after Pandoc conversion.
\newcommand{\authorinput}[1]{%
  \par\medskip\noindent
  \fcolorbox{bookflag}{bookflagtint}{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \small\bfseries\color{bookflag}AUTHOR INPUT NEEDED\par\smallskip
      \normalfont\normalsize\color{black}#1%
    }%
  }%
  \par\medskip
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
\setsecheadstyle{\normalfont\Large\bfseries\raggedright}
\setsubsecheadstyle{\normalfont\large\bfseries\raggedright}

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
    Copyright \copyright\ #2\ #1\par
    \vspace{0.6\baselineskip}
    #3\par
    \vspace{0.6\baselineskip}
    #4\par
    \vspace{0.6\baselineskip}
    #5\par
  }
  \clearpage
}

\newcommand{\dedicationpage}[1]{%
  \thispagestyle{empty}
  \begin{center}
    \vspace*{0.35\textheight}
    {\normalfont\itshape #1\par}
  \end{center}
  \clearpage
}

\endinput
