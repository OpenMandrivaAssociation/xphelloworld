Name: xphelloworld
Version: 1.0.1
Release: %mkrel 9
Summary: Sends a test page to an Xprint printer
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0: xphelloworld-1.0.1-fix-xaw8-BR.diff
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: lesstif-devel
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: libxprintapputil-devel >= 1.0.1
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xphelloworld is a utility for Xprint, the printing system for the X Window
system. It sends a test page to the specified printer (or the default printer,
if none is specified).

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
autoconf
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xphelloworld
%{_bindir}/xpsimplehelloworld
%{_bindir}/xpxthelloworld
%{_mandir}/man1/xphelloworld.1*
%{_mandir}/man1/xpxthelloworld.1*
%{_mandir}/man1/xpsimplehelloworld.1*


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-9mdv2010.0
+ Revision: 435304
- patch 0: xaw8 is dead, let's use xaw7 instead
- BR lesstif-devel
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-8mdv2009.0
+ Revision: 262685
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-7mdv2009.0
+ Revision: 257670
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154400
- Updated BuildRequires and resubmit package.

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.1-4mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode lzma extension!!!


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:16:00 (59527)
- rebuild to fix libXaw.so.8 dependency

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

