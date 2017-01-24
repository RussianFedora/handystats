Summary:	C++ library for collecting user-defined in-process run-time statistics
Name:		handystats
Version:	1.11.3
Release:	4%{?dist}

License:	GPLv3
URL:		https://github.com/yandex/handystats
Source0:	https://github.com/yandex/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix build on gcc 5 and higer
# https://github.com/bioothod/handystats/commit/cf9f66c12998024833d9ef93ee4df176c1241754
Patch0:		handystats-1.13.3-gcc5.patch
Patch1:		handystats-1.13.3-license.patch
Patch2:		handystats-1.13.3-license-fix0.patch
Patch3:		handystats-1.13.3-license-fix1.patch
Patch4:		handystats-1.13.3-debianisazation-refactoring.patch
Patch5:		handystats-1.13.3-multiarch-buildfix.patch

BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	gtest-devel

%description
Handystats is a C++ library for collecting user-defined in-process
run-time statistics with low overhead.

%package devel
Summary:	Development package for %{name}
Requires:	%{name}%{_isa} = %{version}-%{release}

%description devel
Handystats is a C++ library for collecting user-defined in-process 
run-time statistics with low overhead.


%prep
%autosetup -p 1


%build
%{cmake} .
%make_build


%check
%make_build check


%install
%{make_install}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc README.md AUTHORS
%{_libdir}/lib%{name}.so.*


%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Tue Jan 24 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.11.3-5
- fix build with non x86_64 arches

* Wed Jan 11 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.11.3-4
- refactoring debianization

* Wed Jan 11 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.11.3-3
- use standart path and names for library

* Tue Jan 10 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.11.3-2
- fix requires

* Tue Jan 10 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.11.3-1
- initial build
