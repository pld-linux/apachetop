Summary:	Apache top-like display
Summary(pl):	Podobny do topa program pokazuj±cy pracê Apache'a
Name:		apachetop
Version:	0.7
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://clueful.shagged.org/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	775fa87ae957eeb2033428330cb8b33a
URL:		http://clueful.shagged.org/apachetop/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses-based top-like display for Apache information, including
requests per second, bytes per second, most popular URLs, etc.

%description -l pl
Oparty na curses podobny do topa program pokazuj±cy informacje o pracy
Apache'a, w³±czaj±c w to zapytania na sekundê, bajty na sekundê,
najbardziej popularne URL-e, itp.

%prep
%setup -q

%build
%configure
%{__make} \
	CXXFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
