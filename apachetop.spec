Summary:	Apache top-like display
Summary(pl):	Podobny do topa program pokazuj±cy pracê Apache'a
Name:		apachetop
Version:	0.12.5
Release:	1
Epoch:		1
License:	BSD
Group:		Networking/Utilities
Source0:	http://clueful.shagged.org/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	47c40c26319d57100008a2a56dcefe06
Patch0:		%{name}-log_location.patch
URL:		http://clueful.shagged.org/apachetop/
BuildRequires:	fam-devel
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	readline-devel
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
%patch0 -p1

%build
%configure
%{__make} \
	CXX=%{__cxx} \
	CXXFLAGS="%{rpmcflags} -I/usr/include/ncurses -pthread"

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
