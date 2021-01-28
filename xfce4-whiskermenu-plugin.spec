#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-whiskermenu-plugin
Version  : 2.5.3
Release  : 33
URL      : https://archive.xfce.org/src/panel-plugins/xfce4-whiskermenu-plugin/2.5/xfce4-whiskermenu-plugin-2.5.3.tar.bz2
Source0  : https://archive.xfce.org/src/panel-plugins/xfce4-whiskermenu-plugin/2.5/xfce4-whiskermenu-plugin-2.5.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-whiskermenu-plugin-bin = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-data = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-lib = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-license = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-locales = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gettext-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
Patch1: 0001-Show-the-menu-label-by-default.patch

%description
Website
=======
https://docs.xfce.org/panel-plugins/xfce4-whiskermenu-plugin
About
=====

%package bin
Summary: bin components for the xfce4-whiskermenu-plugin package.
Group: Binaries
Requires: xfce4-whiskermenu-plugin-data = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-license = %{version}-%{release}

%description bin
bin components for the xfce4-whiskermenu-plugin package.


%package data
Summary: data components for the xfce4-whiskermenu-plugin package.
Group: Data

%description data
data components for the xfce4-whiskermenu-plugin package.


%package lib
Summary: lib components for the xfce4-whiskermenu-plugin package.
Group: Libraries
Requires: xfce4-whiskermenu-plugin-data = %{version}-%{release}
Requires: xfce4-whiskermenu-plugin-license = %{version}-%{release}

%description lib
lib components for the xfce4-whiskermenu-plugin package.


%package license
Summary: license components for the xfce4-whiskermenu-plugin package.
Group: Default

%description license
license components for the xfce4-whiskermenu-plugin package.


%package locales
Summary: locales components for the xfce4-whiskermenu-plugin package.
Group: Default

%description locales
locales components for the xfce4-whiskermenu-plugin package.


%package man
Summary: man components for the xfce4-whiskermenu-plugin package.
Group: Default

%description man
man components for the xfce4-whiskermenu-plugin package.


%prep
%setup -q -n xfce4-whiskermenu-plugin-2.5.3
cd %{_builddir}/xfce4-whiskermenu-plugin-2.5.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611796769
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1611796769
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-whiskermenu-plugin
cp %{_builddir}/xfce4-whiskermenu-plugin-2.5.3/COPYING %{buildroot}/usr/share/package-licenses/xfce4-whiskermenu-plugin/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd
%find_lang xfce4-whiskermenu-plugin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-popup-whiskermenu

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/16x16/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/22x22/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/24x24/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/256x256/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/32x32/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/48x48/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/64x64/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/scalable/apps/xfce4-whiskermenu.svg
/usr/share/xfce4/panel/plugins/whiskermenu.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libwhiskermenu.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-whiskermenu-plugin/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-popup-whiskermenu.1

%files locales -f xfce4-whiskermenu-plugin.lang
%defattr(-,root,root,-)

