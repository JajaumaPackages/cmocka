BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  glibc-devel

Name:           cmocka
Version:        0.2.0
Release:        3%{?dist}

License:        ASL 2.0
Group:          Development/Tools
Summary:        Lightweight library to simplify and generalize unit tests for C
Url:            http://cmocka.cryptomilk.org/

Source0:        https://open.cryptomilk.org/attachments/download/7/%{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

Cmocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka
Group:          Development/Libraries
Summary:        Lightweight library to simplify and generalize unit tests for C

%description -n libcmocka
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

CMocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka-static
Group:          Development/Libraries
Summary:        Lightweight library to simplify and generalize unit tests for C

%description -n libcmocka-static
Static version of the cmocka library.

%package -n libcmocka-devel
Group:          Development/Libraries
Summary:        Development headers for the cmocka library
Requires:       libcmocka = %{version}-%{release}

%description -n libcmocka-devel
Development headers for the cmocka unit testing library.

%prep
%setup -q

%build
if test ! -e "build"; then
  mkdir build
fi
pushd build
%cmake \
  -DWITH_STATIC_LIB=ON \
  -DUNIT_TESTING=ON \
  %{_builddir}/%{name}-%{version}

make %{?_smp_mflags} VERBOSE=1
popd build

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post -n libcmocka -p /sbin/ldconfig

%postun -n libcmocka -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%check
pushd build
make test
popd

%files -n libcmocka
%defattr(-,root,root)
%doc AUTHORS README ChangeLog COPYING
%{_libdir}/libcmocka.so.*

%files -n libcmocka-static
%defattr(-,root,root)
%{_libdir}/libcmocka.a

%files -n libcmocka-devel
%defattr(-,root,root)
%{_includedir}/cmocka.h
%{_libdir}/libcmocka.so

%changelog
* Fri Jan 18 2013 - Andreas Schneider <asn@redhat.com> - 0.2.0-3
- Fixed typo in Source URL.

* Thu Jan 17 2013 - Andreas Schneider <asn@redhat.com> - 0.2.0-2
- Fixed Source URL.
- Fixed package groups.

* Tue Jan 15 2013 - Andreas Schneider <asn@redhat.com> - 0.2.0-1
- Initial version 0.2.0
