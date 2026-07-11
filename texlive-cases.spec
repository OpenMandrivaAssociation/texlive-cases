%global tl_name cases
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	Numbered cases environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cases
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cases.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cases.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX environment "numcases" to produce multi-
case equations with a separate equation number for each case. There is
also a "subnumcases" environment which numbers each case with the
overall equation number plus a letter [8a, 8b, etc.].

