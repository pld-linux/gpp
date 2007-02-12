Summary:	GPP - Generic Preprocesor
Summary(pl.UTF-8):   GPP - ogólny preprocesor
Name:		gpp
Version:	2.24
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	http://nothingisreal.com/gpp/%{name}-%{version}.tar.bz2
# Source0-md5:	f04c2a23312ab3d0c462c7972d1c6aa6
URL:		http://nothingisreal.com/gpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Provides:	cpp
Obsoletes:	cpp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPP is a general-purpose preprocessor with customizable syntax,
suitable for a wide range of preprocessing tasks. Its independence
from any one programming language makes it much more versatile than
the C preprocessor (cpp), while its syntax is lighter and more
flexible than that of GNU m4. There are built-in macros for use with
C/C++, LaTeX, HTML, XHTML, and Prolog files.

%description -l pl.UTF-8
GPP jest preprocesorem ogólnego przeznaczenia z dostosowywalną
składnią, przeznaczonym do szerokiego zastosowania w zadaniach
preprocesingu. Jako niezależny od jakichkolwiek języków programowania
jest znacznie bardziej wszechstronny od preprocesora C (cpp),
natomiast jego składnia jest lżejsza i bardziej elastyczna niż GNU m4.
Zawiera wbudowane makra do wykorzystania z C/C++, LaTeX, HTML, XHTML i
plikami Prologu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/gpp $RPM_BUILD_ROOT/lib/cpp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
/lib/cpp
