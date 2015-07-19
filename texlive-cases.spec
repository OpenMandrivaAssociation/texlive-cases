# revision 17123
# category Package
# catalog-ctan /macros/latex/contrib/cases
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license pd
# catalog-version 2.5
Name:		texlive-cases
Version:	2.5
Release:	10
Summary:	Numbered cases environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cases
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cases.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cases.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/cases/cases.sty
%doc %{_texmfdistdir}/doc/latex/cases/cases.pdf
%doc %{_texmfdistdir}/doc/latex/cases/cases.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5-2
+ Revision: 749978
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5-1
+ Revision: 718010
- texlive-cases
- texlive-cases
- texlive-cases

