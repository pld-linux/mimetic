Summary:	Email library (MIME)
Name:		mimetic
Version:	0.9.6
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://codesink.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	f853036fddf3a89cdd66659776d2dbea
URL:		http://codesink.org/mimetic_mime_library.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mimetic is a free, MIT licensed, Email library (MIME) written in C++
designed to be easy to use and integrate but yet fast and efficient.

%package devel
Summary:	Header files and more to develop using mimetic
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and more to develop using mimetic.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libmimetic.so.0.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimetic.so
%{_libdir}/libmimetic.la
%{_includedir}/mimetic
