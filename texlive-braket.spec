# revision 17127
# category Package
# catalog-ctan /macros/latex/contrib/braket
# catalog-date 2010-02-23 16:09:16 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-braket
Version:	20100223
Release:	7
Summary:	Dirac bra-ket and set notations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/braket
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braket.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braket.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100223-2
+ Revision: 749886
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100223-1
+ Revision: 717983
- texlive-braket
- texlive-braket
- texlive-braket
- texlive-braket
- texlive-braket

