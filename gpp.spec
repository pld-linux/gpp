Summary:	GPP - Generic Preprocesor
Summary(pl):	GPP - og�lny preprocesor
Name:		gpp
Version:	2.24
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	http://www.nothingisreal.com/gpp/%{name}-%{version}.tar.bz2
# Source0-md5:	f04c2a23312ab3d0c462c7972d1c6aa6
URL:		http://www.nothingisreal.com/gpp
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPP is a general-purpose preprocessor with customizable syntax,
suitable for a wide range of preprocessing tasks. Its independence
from any one programming language makes it much more versatile than
the C preprocessor (cpp), while its syntax is lighter and more
flexible than that of GNU m4. There are built-in macros for use with
C/C++, LaTeX, HTML, XHTML, and Prolog files.

%description -l pl
GPP jest preprocesorem og�lnego przeznaczenia z dostosowywaln�
sk�adni�, przeznaczony do szerokiego zastosowania w zadaniach
preprocesingu. Jako niezale�ny od jakichkolwiek j�zyk�w programowania
jest znacznie bardziej wszechstronny od preprocesora C (cpp),
natomiast jego sk�adnia jest l�ejsza i bardziej elastyczna ni� GNU m4.
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
