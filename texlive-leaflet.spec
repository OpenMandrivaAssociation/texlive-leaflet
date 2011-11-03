# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/leaflet
# catalog-date 2008-01-04 22:30:39 +0100
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-leaflet
Version:	1.0c
Release:	1
Summary:	Create small handouts (flyers)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leaflet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leaflet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leaflet.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leaflet.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A document class to create small hand-outs (flyers) that fit on
a single sheet of paper which is then folded twice. Pages are
rearranged by LaTeX so that they print correctly on a single
sheet -- no external script is necessary. (Works with
PostScript and PDF.) This is a complete reimplementation with
permission of the original author Jurgen Schlegelmilch.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
