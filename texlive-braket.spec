Name:		texlive-braket
Version:	17127
Release:	2
Summary:	Dirac bra-ket and set notations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/braket
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braket.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braket.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides macros to typeset bra-ket notation, as well as set
specifiers, with a single ("|") or a double ("||" or ("\|")
vertical bar specifier in between two bracketed parts. Each
macro comes in a fixed-size version and an expanding version.
If the package finds itself operating under e-tex, it uses the
extended primitive \middle for more reliable results.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/braket/braket.sty
%doc %{_texmfdistdir}/doc/latex/braket/braket.pdf
%doc %{_texmfdistdir}/doc/latex/braket/braket.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
