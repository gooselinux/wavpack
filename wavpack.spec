Name:		wavpack
Summary:	A completely open audiocodec
Version:	4.60
Release:	1.1%{?dist}
License:	BSD
Group:		Applications/Multimedia
Url:		http://www.wavpack.com/
Source:		http://www.wavpack.com/%{name}-%{version}.0.tar.bz2
Patch0:		wavpack-wavpack_pc_in.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

%package devel
Summary:	WavPack - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Files needed for developing apps using wavpack

%prep
%setup -q -n %{name}-%{version}.0
%patch0 -p0 -b .libs

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%{__rm} -f %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/libwavpack.so.*
%doc license.txt

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libwavpack.so
%doc ChangeLog README doc/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 4.60-1.1
- Rebuilt for RHEL 6

* Mon Sep 28 2009 Peter Lemenkov <lemenkov@gmail.com> 4.60-1
- Version 4.60

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.50.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.50.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Peter Lemenkov <lemenkov@gmail.com> 4.50.1-2
- Fixes to meet the Fedora Packaging Guidelines

* Sun Aug 24 2008 Peter Lemenkov <lemenkov@gmail.com> 4.50.1-1
- Version 4.50.1

* Wed Jun 18 2008 Peter Lemenkov <lemenkov@gmail.com> 4.50-1
- Version 4.50

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.41-2
- Autorebuild for GCC 4.3

* Sat May 12 2007 Peter Lemenkov <lemenkov@gmail.com> 4.41-1
- Version 4.41
- Removed unnecessary --with-pic

* Fri Dec 15 2006 Peter Lemenkov <lemenkov@gmail.com> 4.40-1.1
- Rebuild

* Fri Dec 15 2006 Peter Lemenkov <lemenkov@gmail.com> 4.40-1
- Version 4.40

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 4.32-3%{?dist}
- Rebuild for FC6

* Sat Jul 01 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.32-2%{?dist}
- force PIC-only code

* Wed Jun 28 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.32-1%{?dist}
- Version 4.32

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.31-2%{?dist}
- rebuild

* Sat Jan 07 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.31-1
- Fixed several issues with wavpack.pc.in
- Cosmetic fixes.
- Version 4.31

* Sun Nov 13 2005 Peter Lemenkov <lemenkov@newmail.ru> 4.3-1
- Initial build for FC-Extras
- Version 4.3

