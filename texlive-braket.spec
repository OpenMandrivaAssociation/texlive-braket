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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides macros to typeset bra-ket notation, as well as set specifiers,
with a single ("|") or a double ("||" or ("\|") vertical bar specifier
in between two bracketed parts. Each macro comes in a fixed-size version
and an expanding version. If the package finds itself operating under
e-tex, it uses the extended primitive \middle for more reliable results

