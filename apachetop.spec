Summary:	Apache top-like display
Summary(pl):	Podobny do top program pokazuj�cy prac� Apache'a
Name:		apachetop
Version:	0.11
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://clueful.shagged.org/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	5a83938eba950c74d117ef9ef32fef74
Patch0:		%{name}-log_location.patch
URL:		http://clueful.shagged.org/apachetop/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses-based top-like display for Apache information, including
requests per second, bytes per second, most popular URLs, etc.

%description -l pl
Oparty na curses podobny do topa program pokazuj�cy informacje o pracy
Apache'a, w��czaj�c w to zapytania na sekund�, bajty na sekund�,
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
