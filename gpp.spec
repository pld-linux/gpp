#
#
Summary:	GPP - Generic Preprocesor
Summary(pl):	GPP - 
Name:		gpp
Version:	2.24
Release:	0.1
Epoch:		0
License:	GPL
Vendor:		PLD
Group:		Compilers
Source0:	http://www.nothingisreal.com/gpp/%{name}-%{version}.tar.bz2
# Source0-md5:	f04c2a23312ab3d0c462c7972d1c6aa6
URL:		http://www.nothingisreal.com/gpp
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO

%attr(755,root,root) %{_bindir}/*

#%{_docdir}/%{name}-%{version}/*
%{_mandir}/man1/*
