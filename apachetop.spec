#
# TODO (when upgrading): switch to .bz2 source
#
Summary:	Apache top-like display
Summary(pl):	Podobny do topa program pokazuj±cy pracê Apache'a
Name:		apachetop
Version:	0.4
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://clueful.shagged.org/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	b0258a0e771c943415717591606c909e
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
%setup -q -n ApacheTop-%{version}

%build
%{__make} linux \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
