Name:		texlive-hithesis
Version:	64005
Release:	1
Summary:	Harbin Institute of Technology Thesis Template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hithesis
License:	lppl1.3a
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hithesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hithesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hithesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
hithesis is a LaTeX thesis template package for Harbin
Institute of Technology supporting bachelor, master, doctor
dissertations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/xelatex/hithesis
%{_texmfdistdir}/tex/xelatex/hithesis
%{_texmfdistdir}/makeindex/hithesis
%{_texmfdistdir}/bibtex/bst/hithesis
%doc %{_texmfdistdir}/doc/xelatex/hithesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
