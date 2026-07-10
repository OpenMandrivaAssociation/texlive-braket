%global tl_name braket
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Dirac bra-ket and set notations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/braket
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braket.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braket.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides macros to typeset bra-ket notation, as well as set specifiers,
with a single ("|") or a double ("||" or ("\|") vertical bar specifier
in between two bracketed parts. Each macro comes in a fixed-size version
and an expanding version. If the package finds itself operating under
e-tex, it uses the extended primitive \middle for more reliable results

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/braket
%dir %{_datadir}/texmf-dist/tex/latex/braket
%doc %{_datadir}/texmf-dist/doc/latex/braket/braket.pdf
%doc %{_datadir}/texmf-dist/doc/latex/braket/braket.tex
%{_datadir}/texmf-dist/tex/latex/braket/braket.sty
