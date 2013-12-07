# revision 32093
# category Package
# catalog-ctan /macros/latex/contrib/leaflet
# catalog-date 2013-11-07 14:52:10 +0100
# catalog-license lppl
# catalog-version 1.0e
Name:		texlive-leaflet
Version:	1.0e
Release:	4
Summary:	Create small handouts (flyers)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leaflet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leaflet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leaflet.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leaflet.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document class to create small hand-outs (flyers) that fit on
a single sheet of paper which is then folded twice. Pages are
rearranged by LaTeX so that they print correctly on a single
sheet -- no external script is necessary. (Works with
PostScript and PDF.) This is a complete reimplementation with
permission of the original author Jurgen Schlegelmilch.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/leaflet/leaflet.cls
%doc %{_texmfdistdir}/doc/latex/leaflet/README
%doc %{_texmfdistdir}/doc/latex/leaflet/leaflet-manual.pdf
%doc %{_texmfdistdir}/doc/latex/leaflet/leaflet-manual.tex
%doc %{_texmfdistdir}/doc/latex/leaflet/leaflet.pdf
#- source
%doc %{_texmfdistdir}/source/latex/leaflet/leaflet.dtx
%doc %{_texmfdistdir}/source/latex/leaflet/leaflet.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
