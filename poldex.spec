Summary:	GUI frontend to poldek
Summary(pl):	Nak�adka GUI na poldka
Name:		poldex
Version:	0.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.foto-color.info/poldex	
URL:		http://www.foto-color.info/poldex.html	
Requires:	perl-Term-ReadKey
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice GUI frontend to poldek.

%description -l pl
Przyjemna nak�adka na poldka.

%prep
%setup -qcT
cp %{SOURCE0} ../%{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%attr(755,root,root) %{_sbindir}/*
