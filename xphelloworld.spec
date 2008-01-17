Name: xphelloworld
Version: 1.0.1
Release: %mkrel 5
Summary: Sends a test page to an Xprint printer
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libxaw-devel		>= 1.0.4
BuildRequires: libxprintapputil-devel	>= 1.0.1

%description
Xphelloworld is a utility for Xprint, the printing system for the X Window
system. It sends a test page to the specified printer (or the default printer,
if none is specified).

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
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
