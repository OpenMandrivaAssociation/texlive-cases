Name:		texlive-cases
Version:	54682
Release:	2
Summary:	Numbered cases environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cases
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cases.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cases.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Define the environment numcases: equations with several
alternative right-hand sides, with equation numbers for each
alternative. Also environment subnumcases, where each
alternative is a sub-number (e.g., 8a, 8b, ...) of the equation
set as a whole.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cases
%doc %{_texmfdistdir}/doc/latex/cases

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
