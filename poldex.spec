%include        /usr/lib/rpm/macros.perl
Summary:	GUI frontend to poldek
Summary(pl):	Nak³adka GUI na poldka
Name:		poldex
Version:	0.1
Release:	2
License:	GPL
Group:		Applications
Source0:	http://www.foto-color.info/poldex	
Patch0:		%{name}-warning121.patch
URL:		http://www.foto-color.info/poldex.html	
BuildRequires:	perl-Term-ReadKey
BuildRequires:	rpm-perlprov
Requires:	poldek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice GUI frontend to poldek.

%description -l pl
Przyjemna nak³adka na poldka.

%prep
%setup -qcT
cp %{SOURCE0} .
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%attr(755,root,root) %{_sbindir}/*
